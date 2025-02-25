import pandas as pd
from io import StringIO

def main():
    data = """date,col_a,col_b,col_c
2018-05-20,1,2,3
2018-05-21,3,4,6
2018-05-22,5,6,9
"""
    
    df = pd.read_csv(
        StringIO(data),
        index_col='date',
        parse_dates=['date'],  # Pass list of columns to parse as dates
        date_format='%Y-%m-%d'  # Use date_format instead of deprecated date_parser
    )

    assert isinstance(df.index, pd.DatetimeIndex), "Index is not a DatetimeIndex!"
    print(df)
    
    df.drop(['col_a'], axis=1, inplace=True)
    print(df)
    
    df.drop(['col_b', 'col_c'], axis=1, inplace=True)
    assert not df.empty, "Expecting an empty dataframe"
    
if __name__ == "__main__":
    main()
