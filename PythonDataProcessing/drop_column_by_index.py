import pandas as pd
from io import StringIO
def main():
    
    data = """,,,date,col_1
            0,a,I,2000-01-03,1
            1,b,II,2000-01-04,3
            2,c,III,2000-01-05,5
           """
          
    df = pd.read_csv(StringIO(data), index_col=['date'], parse_dates=True, date_format='%Y%m%d')
    # This is to check if the date index of the df matches with the core index of pandas
    assert not isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex), "Index is not a DatetimeIndex!"   
    print(df)
    
    df.drop(df.columns[[0]], axis=1, inplace=True)
    print(df)
    
    df.drop(df.columns[[0,1]], axis=1, inplace=True)
    print(df)
   
if (__name__)== "__main__":
    main()