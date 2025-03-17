import pandas as pd
from io import StringIO
def main():
    
    data = """date,col_1
            2025-02-26,1
            2025-03-05,1
            2025-03-12,1
            2025-03-19,1
            2025-03-26,1
            2025-04-01,1
            2025-04-02,1
            """
            
    df = pd.read_csv(StringIO(data), parse_dates = ['date'])
    
    # Set 'date' as index for grouping
    df.set_index('date', inplace=True)
    table = df.groupby(pd.Grouper(freq='ME')).sum()
    print(table)
    
if (__name__) == '__main__':
    main()