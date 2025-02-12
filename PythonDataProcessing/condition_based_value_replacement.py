import numpy as np
import pandas as pd

"""
https://en.wikipedia.org/wiki/Quantile

"""
def main():
    
    filtering()
    replacing()

def filtering():
    
    #flitering and printing dataframe for all values in the csv for which the "Age" column is greater than 30
    df = pd.read_csv("./ExampleCSV/I_Sample1.csv")
    df_filtered = df[df["Age"] > 30]
    print(df_filtered)
    
    #categorising csv dataall values in the csv for which the "Age" column is greater than 30
    df["Category"] = ["Senior" if age > 30 else "Junior" for age in df["Age"]]
    print(df)
    
    #replacing missing values
    df["Salary"].fillna(df["Salary"].mean(), inplace=True)
    print(df)


def replacing():
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
    
if (__name__) == "__main__":
    main()