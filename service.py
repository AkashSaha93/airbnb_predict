import pandas as pd
import numpy as np

dataset = pd.read_csv("./dataset/AB_US_2020.csv")
print("previous shape -->", dataset.shape)
print("checking for nans -->", dataset.isnull())

# replace null values
dataset = dataset.replace(np.nan, "", regex=True)
print("new shape -->", dataset.shape)
