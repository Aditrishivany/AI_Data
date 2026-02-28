import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Project Started...")

#Load Dataset
df = pd.read_csv("netflix_titles.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

#Data Cleaning

print("\nMissing Values:")
print(df.isnull().sum())

df.fillna("Unknown", inplace=True)

#Basic Analysis
print("\nMovies vs TV Shows:")
print(df['type'].value_counts())

print("\nMost Common Release Year:")
print(df['release_year'].mode())
#GroupBy Analysis
year_trend = df.groupby('release_year').size()

print("\nYear Trend:")
print(year_trend.tail())
#visualization trends
#barchart
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.savefig("bar_chart.png")
plt.close()
#release trend
year_trend.plot()
plt.title("Content Release Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.savefig("trend.png")
plt.close()
#histogram
df['release_year'].plot(kind='hist', bins=20)
plt.title("Release Year Distribution")
plt.savefig("histogram.png")
plt.close()
#Advanced Pandas Operations
df['title_length'] = df['title'].apply(len)

df_sorted = df.sort_values(by='release_year', ascending=False)

pivot = pd.pivot_table(df, index='type', columns='release_year', aggfunc='size')

print("\nPivot Table:")
print(pivot.head())

#Statistical Analysis
print("\nStatistical Summary:")
print(df['release_year'].describe())

average_year = np.mean(df['release_year'])
print("\nAverage Release Year:", average_year)

#Save Processed Data
df.to_csv("netflix_analysis_output.csv", index=False)
print("Analysis saved to CSV.")