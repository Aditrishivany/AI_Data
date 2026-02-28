# churn_training.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

df = pd.read_csv("data/customer_churn.csv")

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

num_cols = df.select_dtypes(include=["int64","float64"]).columns
cat_cols = df.select_dtypes(include=["object"]).columns

df[num_cols] = df[num_cols].fillna(df[num_cols].median())
df[cat_cols] = df[cat_cols].fillna(df[cat_cols].mode().iloc[0])

df.drop(["customerID"], axis=1, errors="ignore", inplace=True)

for col in df.select_dtypes(include="object"):
    df[col] = LabelEncoder().fit_transform(df[col])

X = df.drop("Churn", axis=1)
y = df["Churn"]

model = RandomForestClassifier()
model.fit(X, y)

os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/churn_model.pkl")

# ---- generate plots ----
os.makedirs("static/plots", exist_ok=True)

# Churn Distribution
plt.figure(figsize=(6,4))
sns.countplot(x=y)
plt.title("Churn Distribution")
plt.savefig("static/plots/churn_distribution.png")
plt.close()

# Monthly Charges vs Churn
plt.figure(figsize=(6,4))
sns.boxplot(x=y, y=df["MonthlyCharges"])
plt.title("Monthly Charges by Churn")
plt.savefig("static/plots/monthly_vs_churn.png")
plt.close()

# Tenure vs Churn
plt.figure(figsize=(6,4))
sns.boxplot(x=y, y=df["tenure"])
plt.title("Tenure by Churn")
plt.savefig("static/plots/tenure_vs_churn.png")
plt.close()

# Feature Importance
importances = model.feature_importances_
features = X.columns

plt.figure(figsize=(8,6))
sns.barplot(x=importances, y=features)
plt.title("Feature Importance")
plt.savefig("static/plots/feature_importance.png")
plt.close()

print("Training complete & visual patterns generated!")