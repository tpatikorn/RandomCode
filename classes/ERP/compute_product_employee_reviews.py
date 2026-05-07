import pandas as pd
import numpy as np
import os
from datetime import date, datetime

for filename in os.listdir("review_csv"):
    print("--------------------")
    print(filename)
    company_code = filename.replace(".", "")[0:2].upper()
    data = pd.read_csv(os.path.join("review_csv", filename))
    employees = pd.read_csv(os.path.join("employee_csv", filename))
    #bad_employees = list(employees.loc[employees.Year < 1980].id)
    bad_employees = set()
    bad_products = set()
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
        if min_score < 3:
            #print(product_id, f"{min_score:.2f}", *min_ids)
            #print(",",product_id, sep="",end="")
            bad_products.add(product_id)
        bad_employees = bad_employees.union(set(min_ids))
    bad_employees = list(bad_employees)
    bad_employees = sorted(bad_employees)
    #print(company_code, *bad_products, sep=",")
    #print(company_code, *bad_employees, sep=",")

    print(company_code, len(bad_products), len(bad_employees))