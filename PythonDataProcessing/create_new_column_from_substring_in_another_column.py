import pandas as pd
from io import StringIO
def main():
    
    Str= """Product,Price
        au-apple-1,2.5
        au-apple-2,5.356
        au-peach-1,4.99
        au-peach-2,3.99
        au-grape-2,3.99"""
        
    df = pd.read_csv(StringIO(Str))
    df['Is Apple'] = df['Product'].apply(lambda x: 'Y' if 'apple' in x else 'N')
    print(df)
    
if (__name__) == "__main__":
    main()
