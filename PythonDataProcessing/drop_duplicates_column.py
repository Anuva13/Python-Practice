import pandas as pd
def main():
    
    data = { 'A': [1, 1, 2, 3, 3],
            'B': ['apple', 'grape', 'apple', 'banana', 'grape'],
            'C': [1, 2, 3, 4, 5]
           }
    
    df = pd.DataFrame(data)
    print(df)
    print("\n")
    
    df = df.drop_duplicates(['A'])
    print(df)
    print("\n")
    
    df = df.drop_duplicates(['B'])
    print(df)
    print("\n")
    
    df.reset_index(drop=True, inplace=True)
    print(df)
    print("\n") 
    
if (__name__) == "__main__":
    main()