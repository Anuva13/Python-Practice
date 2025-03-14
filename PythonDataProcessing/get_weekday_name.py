import pandas as pd
from io import StringIO
def main():
    
    str_data = """date, weather
            2025-03-04, cloudy
            2025-03-05, sunny
            2025-03-06, rain
            """
    
    # Read CSV data into DataFrame
    df=pd.read_csv(StringIO(str_data))
    print(df)
    
    # Convert 'date' column to datetime
    df['date']=pd.to_datetime(df['date'])
    # Get the day name
    df['weekday']=df['date'].dt.day_name()  
    print(df)
    
if (__name__) == "__main__":
    main()