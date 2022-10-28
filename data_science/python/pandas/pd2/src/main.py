import pandas as pd

df = pd.read_csv(
    "../input/datasets/book_sales.csv",
    index_col='Date',
    parse_dates=['Date'],
).drop('Paperback', axis=1)

print(df.head())