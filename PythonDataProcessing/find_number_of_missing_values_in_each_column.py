import pandas as pd
from io import StringIO
def main():
    
    str_data = """
            date,open,sales,store
            2018-01-01,N,23,1
            2018-01-02,,44,1
            2018-01-03,Y,,1

            2018-01-01,N,33,2
            2018-01-02,,150,2
            2018-01-03,Y,233,2

            2018-01-01,N,3,3
            2018-01-02,Y,14,3
            2018-01-03,Y,125,3
            """
    
    df= pd.read_csv(StringIO(str_data), parse_dates=True, date_format='%Y%m%d')
    print(df)
    
    print(df.isnull())
    print(df.isnull().sum())
    
if (__name__) == "__main__":
    main()