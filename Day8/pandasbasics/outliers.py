import pandas as pd
df=pd.read_csv('salary_unreal.csv')
print(df.describe())
df_clean=df[df['salary']>20000]
print(df_clean)