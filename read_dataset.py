import pandas as pd

data = pd.read_csv("dataset/dataset_small.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)