import pandas as pd
from io import StringIO

def main():
    str_data = """
date,weather
20250304,cloudy
20250305,sunny
20250306,rain
"""
    
    # Read CSV into DataFrame
    df = pd.read_csv(StringIO(str_data))
    print(df)
    print(df.dtypes)
    print("\n")
    
    # Convert 'date' column to datetime (correct method)
    df['date'] = pd.to_datetime(df['date'], format="%Y%m%d")
    
    print(df)
    print(df.dtypes)

if __name__ == "__main__":
    main()
