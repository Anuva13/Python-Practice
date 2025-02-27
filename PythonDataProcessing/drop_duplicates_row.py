import pandas as pd
def main():
    
    data = {
            'A': [1, 1, 2, 3, 3],
            'B': ['apple', 'apple', 'grape', 'banana', 'banana'],
            'C': [1, 1, 3, 4, 4]
           }
    
    df = pd.DataFrame(data)
    print(df)
    print("\n")
    
    # Dropping the duplicate rows and keeping the first occurence copy of the duplicated row
    df_no_duplicates = df.drop_duplicates(keep = 'first')
    # Rearranging the index after dropping the duplicate rows
    df_no_duplicates.reset_index(drop=True, inplace=True) 
    print(df_no_duplicates)
    print("\n")    
    
if (__name__) == "__main__":
    main()
    
    