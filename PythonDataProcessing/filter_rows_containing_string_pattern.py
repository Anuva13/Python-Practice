import pandas as pd
from io import StringIO
def main():
    
    str_data = """date,language,example_complete
            2025-01-01,python,1
            2025-01-02,python,3
            2025-01-03,python,5

            2025-01-01,r,2
            2025-01-02,r,4
            2025-01-03,r,6
            """
    
    df = pd.read_csv(StringIO(str_data))
    df.set_index(['date'], inplace=True)
    df.sort_index(inplace=True)
    
    #Insert None
    df.iloc[0, 0]= None
    print(df)
    
    #Filtering
    mask= df['language'].str.contains('python', na=False)
    print(df[mask])
    
if (__name__)=="__main__":
    main()    