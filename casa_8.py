import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")

print("Column Names:", df.columns)

print("\n--- Iterating using iterrows() ---")
for index, row in df.iterrows():
    print(f"Country: {row['name']}, Date: {row['date']}, Price: {row['local_price']}")
    if index == 4:
        break

print("\n--- Iterating using apply() ---")
def print_row(row):
    print(f"Country: {row['name']}, Date: {row['date']}, Price: {row['local_price']}")

df.apply(print_row, axis=1)