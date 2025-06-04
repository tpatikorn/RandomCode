import pandas as pd
import numpy as np
import os
from datetime import date, datetime

for filename in os.listdir("generated_data/review_csv"):
    print("--------------------")
    print(filename)
    data = pd.read_csv(os.path.join("generated_data/review_csv", filename))
    employees = pd.read_csv(os.path.join("generated_data/employee_csv", filename))
    bad_employees = list(employees.loc[employees.Year < 1980].id)
    bad_employees = []
    print(bad_employees)
    data = data.loc[~data.employee_id.isin(bad_employees)]
    product_ids = np.unique(data.product_id)
    employee_ids = np.unique(data.employee_id)
    for product_id in product_ids:
        min_ids = []
        min_score = np.inf
        for employee_id in employee_ids:
            product_score = np.mean(data.loc[(data.product_id == product_id) & (data.employee_id == employee_id), ["overall_score"]])
            if product_score == min_score:
                min_ids.append(employee_id)
            elif product_score < min_score:
                min_score = product_score
                min_ids = [employee_id]
        print(product_id, min_score, min_ids)