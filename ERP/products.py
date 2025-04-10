import math

from docx import Document
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT
from docx.enum.text import WD_BREAK, WD_ALIGN_PARAGRAPH
import random
from docx.shared import Pt, Inches
import datetime
import pandas as pd
from os import path, listdir

random.seed(2023)


def randint_plusminus(val_mid, val_min=1, val_max=5, val_range=2):
    return random.randint(max(val_mid % (val_max - val_min + 1) - val_range + val_min, val_min),
                          min(val_mid % (val_max - val_min + 1) + val_range + val_min, val_max))


for filename in listdir("generated_data/employee_csv"):
    company_name = filename[0: -4]
    data = pd.read_csv(path.join("generated_data/employee_csv", filename))
    reviews = pd.read_csv(path.join("generated_data/review_csv", filename))

    all_data = [["review_id", "product_id", "product_name", "price", "purchase_count", "promotion"]]
    print(company_name)
    adj_list = ["happy", "lucky", "sleepy", "amazing", "smart", "intelligent", "cute",
                "beautiful", "fast", "super", "hyper", "quick", "accurate", "cool",
                "strong", "sturdy", "wise", "giga", "mecha"]
    noun_list = ["zebra", "hedgehog", "hamster", "rabbit", "snake", "cat", "tiger", "lion",
                 "dog", "spider", "monkey", "fish", "panda", "horse", "sheep", "dragon"]
    products = {}
    for product_id in range(1, 21):
        products[product_id] = (
            random.sample(adj_list, 1)[0] + "-" + random.sample(noun_list, 1)[0], random.randint(5, 100) * 100)
    for i, row in reviews.iterrows():
        review_id = row["review_id"]
        promotion = random.sample(["0%", "0%", "0%", "0%", "0%", "0%", "0%", "1%", "2%", "2%", "5%", "5%", "10%", "15%"], 1)[0]
        product_name = products[row["product_id"]][0]
        price = products[row["product_id"]][1]
        purchase_count = random.randint(1, 20)
        all_data.append([review_id, row["product_id"], product_name, price, purchase_count, promotion])
    with open(f"product_csv/{company_name}.txt", "w+") as txt_file:
        for line in all_data:
            line = [str(_) for _ in line]
            txt_file.write(",".join(line) + "\n")
        txt_file.flush()
        print("done")
