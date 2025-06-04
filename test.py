from pyarc import CBA, TransactionDB
import pandas as pd

data_train = pd.read_csv("iris.csv")
data_test = pd.read_csv("iris.csv")

txns_train = TransactionDB.from_DataFrame(data_train)
txns_test = TransactionDB.from_DataFrame(data_test)


cba = CBA(support=0.20, confidence=0.5, algorithm="m1")
cba.fit(txns_train)

accuracy = cba.rule_model_accuracy(txns_test)