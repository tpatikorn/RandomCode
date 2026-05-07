import pandas as pd
import numpy as np
import os
from datetime import date, datetime

for filename in os.listdir("review_csv"):
    print(filename)
    data = pd.read_csv(os.path.join("review_csv", filename))
    employees = pd.read_csv(os.path.join("employee_csv", filename))
    employee_ids = np.unique(data.employee_id)
    group_low = []
    group_med = []
    group_high = []
    for e in employee_ids:
        employee_score = data.loc[data.employee_id == e,
                                  ["service_score_1", "service_score_2", "service_score_3"]]
        sum_scores = np.sum(np.sum(employee_score, axis=0))
        average_score = sum_scores / (employee_score.shape[0] * employee_score.shape[1])
        this_employee = employees[employees.id == e]
        employee_name = f"{e},{this_employee.FirstName.values[0]}"
        # print(e, average_score)
        if average_score < 3:
            group_low.append((employee_name, average_score))
        elif average_score < 4:
            group_med.append((employee_name, average_score))
        else:
            group_high.append((employee_name, average_score))

        # print(e, employee_name, average_score)
    company_code = filename.replace(".", "")[0:2].upper()
    print("low", company_code, len(group_low), *min(group_low, key=lambda _: _[1]), *max(group_low, key=lambda _: _[1]), sep=",")
    print("med", company_code, len(group_med), *min(group_med, key=lambda _: _[1]), *max(group_med, key=lambda _: _[1]), sep=",")
    print("high", company_code, len(group_high), *min(group_high, key=lambda _: _[1]), *max(group_high, key=lambda _: _[1]), sep=",")

    #print("low", company_code, len(group_low))
    #print("med", company_code, len(group_med))
    #print("high", company_code, len(group_high))
