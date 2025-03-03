import pandas as pd
from io import StringIO
def main():
    
    str_data = """date,weather
                2018-01-01,cloudy
                2018-01-02,sunny
                2018-01-03,sunny
                2018-01-04,sunny
                2018-01-06,sunny
                2018-01-07,sunny
                2018-01-08,sunny
               """
               
    df = pd.read_csv(StringIO(str_data), parse_dates=['date'], index_col='date')
    print(df)
    # Extract the year correctly
    print(df.index.year)
     # Extract the month correctly
    print(df.index.month)
     # Extract the day correctly
    print(df.index.day)
    # Extract week number correctly
    print(df.index.isocalendar().week)
    # Extract  weekday number correctly
    print(df.index.isocalendar().day)
    # Extract weekday name correctly
    print(df.index.day_name())  
    
if (__name__) == "__main__":
    main()