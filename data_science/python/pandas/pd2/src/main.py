import pandas as pd
import numpy as np

df = pd.read_csv(
    "../input/datasets/book_sales.csv",
    index_col='Date',
    parse_dates=['Date'],
).drop('Paperback', axis=1)

df['Time'] = np.arange(len(df.index))

print(df.head())