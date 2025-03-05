import pandas as pd
from io import StringIO
def main():
    
    str_data = """gender,age
                female,20
                female,nan
                male,21
                male,22
                male,23
                female,21
                male,nan
                female,22
               """
               
    df = pd.read_csv(StringIO(str_data))
    print(df)
    print("\n")
    
    df['age'].fillna(df.groupby(['gender'])['age'].transform('mean'), inplace = True)
    print("Tranformed data:")
    print(df)
    print("\n")    
    
if (__name__) == "__main__":
    main()