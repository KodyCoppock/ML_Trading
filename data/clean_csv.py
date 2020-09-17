import pandas

df = pandas.read_csv("C:\\Users\\kodyc\\combined_stock_data.csv")

df = df[df.X1 != "date"]
df["file_name"] = df["file_name"].str.replace(r'.*/', '')

df["file_name"] = df["file_name"].str.replace('.csv', '')

df = df.drop(["Unnamed: 0"], axis=1)

df = df.rename(columns={"file_name": "symbol", "X1": "date", "X2": "volume", "X3": "open", "X4": "high", "X5": "low",
                        "X6": "close", "X7": "adjclose"})

df.to_csv(r'D:\\clean_data.csv', index=False)
