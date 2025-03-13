import pandas as pd
from dateutil.relativedelta import relativedelta, FR 
"""
    * 'relativedelta' allows you to perform date and time calculations with flexibility (e.g., adding or subtracting specific time units).
    * FR is a constant representing Friday, which is used to calculate the closest previous or next Friday.
"""
def main():
    
    data = [
            {
                'date': '2025-03-01',
                'weather': 'cloudy'
            },
            {
                'date': '2025-03-02',
                'weather': 'sunny'
            },
            {
                'date': '2025-03-03'
            },
            {
                'date': '2025-03-04',
                'weather': 'rain'
            }
           ]

    df = pd.DataFrame(data)
    print(df)
    print("\n")
    
    #Converts the 'date' column from a string to pandas datetime objects
    df['date'] = pd.to_datetime(df['date'])
    print(df)
    print("\n")
    
    df['last_friday'] = df['date'].apply(lambda x: x + relativedelta(weekday=FR(-1)))
    print(df)
    
if (__name__) == "__main__":
    main()