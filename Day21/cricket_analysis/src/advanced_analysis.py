import numpy as np
import matplotlib.pyplot as plt

def advanced(df):

    df["RunStd"] = df.groupby("Player")["Runs"].transform(np.std)
    consistent = df.nsmallest(10, "RunStd")[["Player", "RunStd"]]
    print("\nMOST CONSISTENT BATSMEN:\n", consistent)

    df["Impact"] = df["Wickets"] * (1 / (df["Economy"] + 0.1))
    impactful = df.nlargest(10, "Impact")[["Player", "Impact"]]
    print("\nMOST IMPACTFUL BOWLERS:\n", impactful)

    plt.boxplot(df["BattingAverage"])
    plt.title("Batting Average Distribution")
    plt.show()

    role_counts = df["Role"].value_counts()
    plt.pie(role_counts, labels=role_counts.index)
    plt.title("Player Role Distribution")
    plt.show()

    numeric_df = df.select_dtypes(include=np.number)
    corr = np.corrcoef(numeric_df.T)

    plt.imshow(corr, cmap="viridis")
    plt.colorbar()
    plt.title("Correlation Matrix")
    plt.show()