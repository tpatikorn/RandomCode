import pandas as pd
import numpy as np
import os
from datetime import date, datetime

for filename in os.listdir("generated_data/employee_csv"):
    print(filename)
    data = pd.read_csv(os.path.join("generated_data/employee_csv", filename),
                       parse_dates=['DoB'], date_format={'DoB': '%Y-%m-%d'})
    data["BMI"] = data["Weight"] / (data["Height"] * data["Height"] / 10000)
    data_fn_n = data[data["FirstName"].str.startswith("N")]
    print("BMI of FirstName N", np.mean(data_fn_n["BMI"]))
    data_bmi_20 = data[data["BMI"] >= 20]
    data["Today"] = datetime(year=2023, month=11, day=28)
    print("count A for BMI >= 20", sum(_ == "A" or _ == "a" for _ in ("".join(data_bmi_20["LastName"]))))
    data["Age"] = data["Today"].dt.year - data["DoB"].dt.year
    bad_month = data["Today"].dt.month < data["DoB"].dt.month
    bad_day_month = (data["Today"].dt.month == data["DoB"].dt.month) & (data["Today"].dt.day < data["DoB"].dt.day)
    data.loc[bad_month | bad_day_month, "Age"] = data.loc[bad_month | bad_day_month, "Age"] - 1
    for position in ["director", "team leader", "senior", "junior"]:
        data_this_pos = data[data["Position"] == position]
        print(position, np.mean(data_this_pos["Age"]))
    print()
