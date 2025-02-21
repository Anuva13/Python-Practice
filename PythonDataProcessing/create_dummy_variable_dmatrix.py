import pandas as pd
from patsy.highlevel import dmatrix
def main():
    """
    https://towardsdatascience.com/the-dummys-guide-to-creating-dummy-variables-f21faddb1d40
    https://www.youtube.com/watch?v=WRxHfnl-Pcs
    """

    url = './ExampleCSV/I_Sample_Employee_Data1.dat'
    df = pd.read_csv(url, sep="\t", engine="python")
    print(df["id"])

    # use pandas
    dummy = pd.get_dummies(df["id"])
    print(dummy.head())

    df = pd.concat([df, dummy], axis=1)
    print(df.head())

    # use patsy
    dummy = dmatrix("id", df, return_type='dataframe')
    df = pd.concat([df, dummy], axis=1)
    print(df.head())
    
if (__name__) == "__main__":
    main()

