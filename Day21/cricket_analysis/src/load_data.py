import pandas as pd
import numpy as np

def load_dataset(path):
    df = pd.read_csv(path)
    return df

def basic_info(df):
    print("FIRST 10 ROWS:\n", df.head(10))
    print("\nLAST 5 ROWS:\n", df.tail(5))
    print("\nSHAPE:", df.shape)
    print("\nCOLUMNS:", df.columns.tolist())
    print("\nDATA TYPES:\n", df.dtypes)

    print("\nMISSING VALUES:\n", df.isnull().sum())
    print("\nDUPLICATES:", df.duplicated().sum())

    numeric_cols = df.select_dtypes(include=np.number).columns
    print("\nTOTAL NUMERIC COLUMNS:", len(numeric_cols))

    col = numeric_cols[0]
    data = df[col].dropna().values

    print("\nNUMPY STATS FOR:", col)
    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Std Dev:", np.std(data))