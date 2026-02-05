import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")
plt.figure()
plt.barh(df["product"], df["price"])
plt.xlabel("price")
plt.ylabel("product")
plt.title("Product Price Comparison")
plt.show()