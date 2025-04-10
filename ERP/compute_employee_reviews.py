import pandas as pd
import numpy as np
import os
from datetime import date, datetime

for filename in os.listdir("generated_data/review_csv"):
    print(filename)
    data = pd.read_csv(os.path.join("generated_data/review_csv", filename))
    employees = pd.read_csv(os.path.join("generated_data/employee_csv", filename))
    employee_ids = np.unique(data.employee_id)
    group_low = []
    group_med = []
    group_high = []
    for e in employee_ids:
        employee_score = data.loc[data.employee_id == e,
                                  ["service_score_1", "service_score_2", "service_score_3"]]
        sum_scores = sum(np.sum(employee_score))
        average_score = sum_scores / (employee_score.shape[0] * employee_score.shape[1])
        this_employee = employees[employees.id == e]
        employee_name = f"{e} {this_employee.FirstName.values[0]} {this_employee.LastName.values[0]}"
        print(e, average_score)
        if average_score < 3:
            group_low.append((employee_name, average_score))
        elif average_score < 4:
            group_med.append((employee_name, average_score))
        else:
            group_high.append((employee_name, average_score))

        # print(e, employee_name, average_score)
    print("low", len(group_low), min(group_low, key=lambda _: _[1]), max(group_low, key=lambda _: _[1]))
    print("med", len(group_med), min(group_med, key=lambda _: _[1]), max(group_med, key=lambda _: _[1]))
    print("high", len(group_high), min(group_high, key=lambda _: _[1]), max(group_high, key=lambda _: _[1]))
