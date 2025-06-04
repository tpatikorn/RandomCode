import pandas as pd
import numpy as np
import os
from datetime import date, datetime

for filename in os.listdir("generated_data/review_csv"):
    print(filename)
    data = pd.read_csv(os.path.join("generated_data/review_csv", filename))
    employees = pd.read_csv(os.path.join("generated_data/employee_csv", filename))
    bad_employees = list(employees.loc[employees.Year < 1980].id)
    data = data.loc[~data.employee_id.isin(bad_employees)]
    product_ids = np.unique(data.product_id)
    group_low = []
    group_med = []
    group_high = []
    for product_id in product_ids:
        product_score = data.loc[data.product_id == product_id,
                                  ["product_score_1", "product_score_2", "product_score_3"]]
        sum_scores = np.sum(np.sum(product_score))
        average_score = sum_scores / (product_score.shape[0] * product_score.shape[1])
        print(product_id, average_score)
        if average_score < 3:
            group_low.append((product_id, average_score))
        elif average_score < 4:
            group_med.append((product_id, average_score))
        else:
            group_high.append((product_id, average_score))

        # print(e, employee_name, average_score)
    if len(group_low) > 0:
        print("low", len(group_low), min(group_low, key=lambda _: _[1]), max(group_low, key=lambda _: _[1]))
    if len(group_med) > 0:
        print("med", len(group_med), min(group_med, key=lambda _: _[1]), max(group_med, key=lambda _: _[1]))
    if len(group_high) > 0:
        print("high", len(group_high), min(group_high, key=lambda _: _[1]), max(group_high, key=lambda _: _[1]))