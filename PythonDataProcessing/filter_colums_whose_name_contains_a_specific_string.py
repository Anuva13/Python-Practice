import pandas as pd
from tabulate import tabulate
def main():
    
    # data
    data = {
    'spike-2': [1, 2, 3],
    'hey spke': [4, 5, 6],
    'spiked-in': [7, 8, 9],
    'no': [10, 11, 12]
    }
    
    df = pd.DataFrame(data=data)
    print(tabulate(df, headers='keys', tablefmt='psql'))
    
    #filter
    df_filtered = df.filter(regex='spike')
    print("Filtered:")
    print(tabulate(df_filtered, headers='keys', tablefmt='psql'))
       
if (__name__) == "__main__":
    main()