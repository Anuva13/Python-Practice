import pandas as pd
from io import StringIO
def main():
    
    string = """
        date, weather
        2018-03-04, cloudy
        2018-03-05, sunny
        2018-03-06, rain
        """
        
    df = pd.read_csv(StringIO(string))
    print(df)
    
if (__name__) == ("__main__"):
    main()