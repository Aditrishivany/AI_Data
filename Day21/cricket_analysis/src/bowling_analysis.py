import numpy as np
import matplotlib.pyplot as plt

def bowling_analysis(df):
    print("\nTOP 10 BY WICKETS:\n", df.nlargest(10, "Wickets")[["Player", "Wickets"]])
    print("\nTOP 10 BY ECONOMY:\n", df.nsmallest(10, "Economy")[["Player", "Economy"]])

    plt.hist(df["Wickets"], bins=30)
    plt.title("Wickets Distribution")
    plt.xlabel("Wickets")
    plt.ylabel("Count")
    plt.show()

    plt.scatter(df["Economy"], df["Wickets"])
    plt.title("Economy vs Wickets")
    plt.xlabel("Economy")
    plt.ylabel("Wickets")
    plt.show()

    print("Average Wickets:", np.mean(df["Wickets"]))
    print("Best Economy:", np.min(df["Economy"]))

    wickets = df["Wickets"].values
    economy = df["Economy"].values
    correlation = np.corrcoef(wickets, economy)[0, 1]
    print("Correlation:", correlation)