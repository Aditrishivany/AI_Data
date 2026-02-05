import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("studentreport.csv")

print("Original Data:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df["City"] = df["City"].str.strip().str.title()

print("\nCleaned Data:")
print(df)

avg_marks = df["Marks"].mean()
print("\nAverage Marks:", avg_marks)

top_student = df.loc[df["Marks"].idxmax()]
print("\nTop Scoring Student:")
print(top_student)

below_70 = df[df["Marks"] < 70]
print("\nStudents scoring below 70:")
print(below_70)

plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Marks vs Students")
plt.show()