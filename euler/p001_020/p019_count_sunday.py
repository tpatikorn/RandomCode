days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year_start = 1901
year_end = 2001

sunday_count = 0

day_of_week = 2  # jan 1 1901 was tuesday
for year in range(year_start, year_end):
    for month in days_per_month:
        day_of_week = day_of_week + month
        if month == 28 and year % 4 == 0:
            if (year % 100 == 0) and not (year % 400 == 0):
                pass
            else:
                day_of_week = day_of_week + 1
        if day_of_week % 7 == 0:
            sunday_count = sunday_count + 1
print(sunday_count)
