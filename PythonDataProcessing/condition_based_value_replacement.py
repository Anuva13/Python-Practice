import numpy as np
import pandas as pd

"""
https://en.wikipedia.org/wiki/Quantile

"""

df = pd.read_csv("./ExampleCSV/I_Sample4.csv")
df.set_index(['date'], inplace=True)

df['x'] = df['x'].astype(float)
df['y'] = df['y'].astype(float)

df_copy = df.copy()

# replace - 1
print(df)
mask = (df['x'] > 0.0) & (df['x'] < 3.0)
df.loc[mask, 'x'] = -1
print(df)

# replace - 2
print(df_copy)
df_copy['x'] = np.where((df_copy['y'] == 3.0) | (df_copy['y'] == 4.0), np.nan, df_copy['x'])
print(df_copy)