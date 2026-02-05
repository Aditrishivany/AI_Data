import pandas as pd

#load and inspect
df=pd.read_csv("student_data.csv")
#print(df)

#print(df.isnull())
df['Marks'].fillna(df['Marks'].mean(),inplace=True)
print(df)
df_clean=df.dropna()
print(df_clean)