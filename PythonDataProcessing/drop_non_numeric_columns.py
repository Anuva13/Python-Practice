import pandas as pd
import numpy as np
from io import StringIO
from pandas.testing import assert_frame_equal
def main():
    
    data = """date,numeric_col_1,non-numeric_col,numeric_col_2
            2025-06-10,0,NaN,NaN
            2025-06-11,1,NaN,1
            2025-06-12,NaN,a,2
            2025-06-13,3,b,NaN
            2025-06-14,NaN,x,3
            2025-06-15,NaN,c,5
            2025-06-16,6,d,7
           """
    
    df = pd.read_csv(StringIO(data), 
                     index_col = ['date'], 
                     parse_dates = True, 
                     date_format ='%Y-%m-%d')
    print(df)
    #creating a copy of the data frame
    df_copy = df.copy()
    
    # use private method
    df = df._get_numeric_data()
    print(df)
    
    # use select_dtypes
    df_copy = df_copy.select_dtypes([np.number])
    print(df_copy)
    
    assert_frame_equal(df, df_copy)
    
if (__name__) == "__main__":
    main()