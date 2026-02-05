import pandas as pd
data = {
    "transaction_id": [1, 2, 3, 4],
    "type": ["deposit", "withdraw", "deposit", "withdraw"],
    "amount": [1000, 300, 1500, 2000]
}

df = pd.DataFrame(data)
print("Transaction Data:")
print(df)

# 1) Track deposits and withdrawals
total_deposits = df[df["type"] == "deposit"]["amount"].sum()
total_withdrawals = df[df["type"] == "withdraw"]["amount"].sum()

print("\nTotal Deposits:", total_deposits)
print("Total Withdrawals:", total_withdrawals)

# 2) Calculate final balance (assuming starting balance = 0)
final_balance = total_deposits - total_withdrawals
print("\nFinal Balance:", final_balance)

# 3) Detect high-value transactions (≥ 1000)
high_value_threshold = df["amount"].mean()  # smarter threshold
df["high_value"] = df["amount"] >= high_value_threshold

print("\nHigh Value Transactions:")
print(df[df["high_value"] == True])

print("\nFinal Data:")
print(df)
