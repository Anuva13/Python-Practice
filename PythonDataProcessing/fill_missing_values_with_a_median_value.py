import pandas as pd
from io import StringIO
def main():
    
    str_data = """
                date,sales
                2018-04-01,nan
                2018-04-02,40
                2018-04-03,nan
                2018-04-04,30
                2018-04-05,60
                2018-04-06,300
               """
               
    # Read CSV, handling spaces and NaN values correctly
    df = pd.read_csv(StringIO(str_data), parse_dates= True, date_format='%Y%m%d')
    print(df)
    
    # Ensure 'sales' is treated as numeric
    df['sales'] = pd.to_numeric(df['sales'])
    
    print("\nmedian = {0:.2f}".format(df['sales'].median()))
    print("mean = {0:.2f}\n".format(df['sales'].mean()))

    df['sales'].fillna(df['sales'].median(), inplace=True)
    print("\nTransformed DataFrame:")
    print(df)
    
if (__name__) == "__main__":
    main()