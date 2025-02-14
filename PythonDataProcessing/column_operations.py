import pandas as pd
import numpy as np
def main():
    
    # add some columns
    df1 = pd.DataFrame(np.random.randint(0, 10, (2,3)), columns=list(['A', 'B', 'C']))
    df1['D'] = df1['A'] + df1['C']
    print(df1)
    print("\n")
    
    # add some columns
    df2 = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list(['A', 'B', 'C']))
    df2['D'] = df2[['A', 'C']].sum(axis=1)
    print(df2)
    print("\n")
    
    # add a new row with column-wise sums
    df3 = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list(['A', 'B', 'C']))
    df3.loc['Total'] = df3.sum()
    print(df3)
    print("\n")
    
    # add a new row with column-wise sums without using df.sum()
    df4 = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list(['A', 'B', 'C']))    
    df4.loc['Total'] = df4.iloc[:, :].sum(axis=0).values
    print(df4)
    print("\n")
    
    # add all the columns
    df5 = pd.DataFrame(np.random.randint(0, 10, (4, 3)), columns=list(['A', 'B', 'C']))
    df5['D'] = df5[list(df5.columns)].sum(axis=1)
    print(df5)
    print("\n")
    
    # use lambda
    df6 = pd.DataFrame(np.random.randint(0,10,(4,3)), columns=list(['A', 'B', 'C']))
    df6['D'] = df6.apply(lambda x: x['A']*100 + x['B']/2, axis=1)
    print(df6)
    print("\n")   
    
if (__name__) == "__main__":
    main()