import pandas as pd

df = pd.read_excel("Online Retail.xlsx")

# filter out missing/bad data.  Not sure of the implications here
df = df.dropna()

# for some reason CustomerID is interpreted as float.  Change to int
df['CustomerID'] = df['CustomerID'].astype(int)

df.to_csv("Online_Retail.csv", index=False)
