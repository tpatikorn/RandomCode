import pandas as pd
import numpy as np
import os
from datetime import date, datetime

for filename in os.listdir("employee_csv"):
    # print(filename)
    data = pd.read_csv(os.path.join("employee_csv", filename),
                       parse_dates=['DoB'], date_format={'DoB': '%Y-%m-%d'})
    company_code = filename.replace(".","")[0:2].upper()
    print("sum of salary ", company_code, sum(data["Salary"]), sep="")
    print("mean of height ", company_code, f"{sum(data["Height"])/len(data["Height"]):.2f}", sep="")
    print("min max of weight ", company_code, min(data["Weight"]), " ", company_code, max(data["Weight"]), sep="")
    data["BMI"] = data["Weight"] / (data["Height"] * data["Height"] / 10000)
    data_fn_n = data[data["FirstName"].str.startswith("N")]
    #print("BMI of FirstName N", np.mean(data_fn_n["BMI"]))
    data_bmi_20 = data[data["BMI"] >= 20]
    data["Today"] = datetime(year=2023, month=11, day=28)
    #print("count A for BMI >= 20", sum(_ == "A" or _ == "a" for _ in ("".join(data_bmi_20["LastName"]))))
    data["Age"] = data["Today"].dt.year - data["DoB"].dt.year
    bad_month = data["Today"].dt.month < data["DoB"].dt.month
    bad_day_month = (data["Today"].dt.month == data["DoB"].dt.month) & (data["Today"].dt.day < data["DoB"].dt.day)
    data.loc[bad_month | bad_day_month, "Age"] = data.loc[bad_month | bad_day_month, "Age"] - 1
    for position in ["director", "team leader", "senior", "junior"]:
        data_this_pos = data[data["Position"] == position]
        #print(position, np.mean(data_this_pos["Age"]))
    print()
