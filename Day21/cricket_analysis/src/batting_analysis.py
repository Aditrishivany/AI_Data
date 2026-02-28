import numpy as np
import matplotlib.pyplot as plt

def batting_analysis(df):
    print("\nTOP 10 BY RUNS:\n", df.nlargest(10, "Runs")[["Player", "Runs"]])
    print("\nTOP 10 BY AVERAGE:\n", df.nlargest(10, "BattingAverage")[["Player", "BattingAverage"]])
    print("\nTOP 10 BY STRIKE RATE:\n", df.nlargest(10, "StrikeRate")[["Player", "StrikeRate"]])

    plt.hist(df["Runs"], bins=30)
    plt.title("Runs Distribution")
    plt.xlabel("Runs")
    plt.ylabel("Count")
    plt.show()

    plt.scatter(df["Runs"], df["StrikeRate"])
    plt.title("Runs vs Strike Rate")
    plt.xlabel("Runs")
    plt.ylabel("Strike Rate")
    plt.show()

    plt.scatter(df["Matches"], df["Runs"])
    plt.title("Matches vs Runs")
    plt.xlabel("Matches")
    plt.ylabel("Runs")
    plt.show()

    print("Mean Runs:", np.mean(df["Runs"]))
    print("Median Strike Rate:", np.median(df["StrikeRate"]))
    print("Std Dev Batting Avg:", np.std(df["BattingAverage"]))