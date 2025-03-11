import pandas as pd
def main():
    
    data = {
            'A': [1, 2, None], 
            'B': [4, None, 6]}
    
    df = pd.DataFrame(data)
    print(df)
    
    # Sum will return NaN if values are missing
    # Convert the sum to a string before concatenation
    print('Sum=' + str(df['B'].sum()))
    
    
if (__name__) == "__main__":
    main()