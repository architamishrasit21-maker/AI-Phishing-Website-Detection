import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("dataset/dataset_small.csv")

X = data.drop("phishing", axis=1)
y = data["phishing"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "phishing_model.pkl")

print("Model saved successfully!")