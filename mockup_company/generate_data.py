import pandas as pd
import numpy as np
import math

from datetime import datetime

START_FIRST_DATE = datetime(2000, 1, 1)
LAST_END_DATE = datetime(2024, 12, 31)
EMPLOYEE_SIZE = np.random.randint(10_000, 12_000)
MAX_RANK = math.ceil(math.log(EMPLOYEE_SIZE)) + 2

np.random.seed(0)
df = pd.DataFrame({"id": np.arange(start=0, stop=EMPLOYEE_SIZE)})
df.index = df["id"]
start_delay = np.random.randint(low=0, high=8_000, size=EMPLOYEE_SIZE)
df['start_date'] = START_FIRST_DATE
df['start_date'] = df['start_date'] + pd.to_timedelta(start_delay, unit='D')

last_bosses = np.zeros(MAX_RANK + 1)

this_rank = 0
for i in range(EMPLOYEE_SIZE):
    df.at[i, 'supervisor_id'] = -1 if this_rank == 0 else last_bosses[this_rank - 1]
    df.at[i, 'rank'] = this_rank
    underling_chance = this_rank / (1 * MAX_RANK)
    next_done_chance = this_rank / (20 * MAX_RANK)
    df.at[i, 'salary'] = np.random.randint(low=15_000 + (MAX_RANK - this_rank) ** 2 * 2000,
                                           high=25_000 + (MAX_RANK - this_rank) ** 2 * 2000)

    if this_rank == 0 or (np.random.rand() > underling_chance and this_rank != MAX_RANK):
        last_bosses[this_rank] = i
        this_rank += 1
    elif np.random.rand() > next_done_chance:
        this_rank -= 1

df.to_csv("employees.csv", index=False)


def generate_scores(size):
    return np.random.choice([
        1, 1, 1, 1, 1,
        2, 2, 2,
        3,
        4, 4, 4,
        5, 5, 5, 5, 5], size=REVIEW_SIZE,
        replace=True)


REVIEW_SIZE = np.random.randint(1_000_000, 1_200_000)
CUSTOMER_SIZE = np.random.randint(100_000, 120_000)
reviews = pd.DataFrame({"id": np.arange(start=0, stop=REVIEW_SIZE)})
reviews.index = reviews["id"]
reviews["customer_id"] = np.random.randint(low=0, high=CUSTOMER_SIZE, size=REVIEW_SIZE)
reviews['employee_id'] = np.random.randint(low=0, high=EMPLOYEE_SIZE, size=REVIEW_SIZE)
reviews['service_speed'] = generate_scores(REVIEW_SIZE)
reviews['service_quality'] = generate_scores(REVIEW_SIZE)
reviews['service_eagerness'] = generate_scores(REVIEW_SIZE)
reviews['product_availability'] = generate_scores(REVIEW_SIZE)
reviews['product_quality'] = generate_scores(REVIEW_SIZE)
reviews['store_parking'] = generate_scores(REVIEW_SIZE)
reviews['store_quality'] = generate_scores(REVIEW_SIZE)

reviews.to_csv("reviews.csv", index=False)

REPORT_SIZE = np.random.randint(low=1000, high=2000)
reports = pd.DataFrame({"id": np.arange(start=0, stop=REPORT_SIZE)})
reports.index = reports["id"]

reports['type'] = np.random.choice(["customer", "customer", "customer", "customer", "customer", "customer",
                                    "employee"], size=reports.size, replace=True)
reports["person_id"] = np.random.randint(low=0, high=CUSTOMER_SIZE, size=REPORT_SIZE)
reports.loc[(reports["type"] == "employee") & (reports["person_id"] > EMPLOYEE_SIZE), "type"] = "customer"

reports.to_csv("reports.csv", index=False)
