import numpy as np

def clean_dataset(df):
    df = df.drop_duplicates()
    df = df.fillna(0)

    if 'Runs' in df.columns and 'Balls_Faced' in df.columns:
        df['StrikeRate'] = np.where(df['Balls_Faced'] > 0,
                                    (df['Runs'] / df['Balls_Faced']) * 100,
                                    0)
    if 'Runs' in df.columns and 'Innings' in df.columns:
        df['BattingAverage'] = np.where(df['Innings'] > 0,
                                        df['Runs'] / df['Innings'],
                                        0)
    if 'Runs_Given' in df.columns and 'Overs' in df.columns:
        df['Economy'] = np.where(df['Overs'] > 0,
                                 df['Runs_Given'] / df['Overs'],
                                 0)

    return df