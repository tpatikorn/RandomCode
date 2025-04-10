import xml.etree.ElementTree as eltTree
import requests
import os
import gspread
from google.oauth2.service_account import Credentials
import dotenv

dotenv.load_dotenv()

xml_url = os.getenv("METER_XML")  # source XML
sheet_id = os.getenv('SHEET_ID')  # destination Google Sheet ID
credentials_path = '../service_key.json'  # Google credential file

print(xml_url)

# Read data from source
response = requests.get(xml_url)
xml_contents = response.content.decode('windows-1252')  # Use windows-1252 encoding
root = eltTree.fromstring(xml_contents)

# Setup Google Sheet and read data
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file(credentials_path, scopes=scope)
gc = gspread.authorize(credentials)
print("reading existing data")
sheet = gc.open_by_key(sheet_id).sheet1
existing_data = sheet.get_all_values()[1:]  # remove the header row

# Write the data rows if (date, month, year) doesn't already exist
data_to_write = []
data_to_update = {}


# check float equality. Return true if the difference is bigger than tol
def float_compare(fl1, fl2, tol=0.0001):
    return abs(fl1 - fl2) > tol


def format_row(elt_row, int_rows=None):
    if int_rows is None:
        int_rows = [0, 1, 2, 3]
    elt_row = [float(e) for e in elt_row]
    for index in int_rows:
        elt_row[index] = int(elt_row[index])
    return elt_row


print("Processing")
for day in root.findall('day'):
    if day[0] == ['rec']:
        continue
    data: list[any] = format_row([tag.text for tag in day])
    existing_data = [format_row(row) for row in existing_data]
    that_date = list(filter(lambda elt: elt[1] == data[1] and elt[2] == data[2] and elt[3] == data[3],
                            existing_data))
    if len(that_date) == 0:
        data_to_write.append(data)
    else:
        for i in range(1, len(that_date[0])):  # exclude first column, it's just a running record#
            if float_compare(that_date[0][i], data[i]):
                data_to_update[(data[1], data[2], data[3])] = data

# Write data to the Google Sheet
print("writing new rows")
if data_to_write:
    rows_to_insert = [day_data for day_data in reversed(data_to_write)]  # Reverse data for correct order
    sheet.append_rows(rows_to_insert)
    print(f"Data has been written to the Google Sheet:{len(rows_to_insert)} row(s) were inserted.")
else:
    print(f"No new data has been written to the Google Sheet.")

print("updating rows")
if data_to_update:
    print(len(data_to_update.keys()), "rows to update")
    print(data_to_update)
    for i, row in enumerate(existing_data):
        this_key = (row[1], row[2], row[3])
        if this_key in data_to_update.keys():
            print("updating row:", this_key, data_to_update[this_key])
            for j, d in enumerate(data_to_update[this_key]):
                if j > 0 and float_compare(row[j], d):
                    print("updating value:", row[j], "->", d)
                    # row uses i + 2 because Sheet starts with 1, plus the header row = +2
                    # column uses j + 1  because Sheet starts with 1
                    sheet.update_cell(i + 2, j + 1, d)
print("done")
