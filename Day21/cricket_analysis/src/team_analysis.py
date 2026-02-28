import matplotlib.pyplot as plt

def team_analysis(df):
    team_runs = df.groupby("Team")["Runs"].sum()
    team_avg = df.groupby("Team")["BattingAverage"].mean()
    team_wkts = df.groupby("Team")["Wickets"].sum()

    print("\nTOTAL RUNS PER TEAM:\n", team_runs)
    print("\nAVERAGE BATTING AVERAGE PER TEAM:\n", team_avg)
    print("\nTOTAL WICKETS PER TEAM:\n", team_wkts)

    team_runs.plot(kind="bar")
    plt.title("Team vs Total Runs")
    plt.ylabel("Runs")
    plt.show()

    team_wkts.plot(kind="bar")
    plt.title("Team vs Total Wickets")
    plt.ylabel("Wickets")
    plt.show()