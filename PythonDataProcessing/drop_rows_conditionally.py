import pandas as pd
from io import StringIO
def main():
    
    # data
    data = """
    date,variable,value
    2000-01-03,A,0.469112
    2000-01-04,A,-0.282863
    2000-01-05,A,-1.509059

    2000-01-03,B,-1.135632
    2000-01-04,B,1.212112
    2000-01-05,B,-0.173215

    2000-01-03,C,0.119209
    2000-01-04,C,-1.044236
    2000-01-05,C,-0.861849

    2000-01-03,D,-2.104569
    2000-01-05,D,1.071804
    """
    
    # create dataframe
    df = pd.read_csv(StringIO(data))
    
    # delete some rows
    cond = df['variable'] != 'A'
    df_cond = df[cond]
    print(df_cond)
    print("\n")
    
    # use drop to delete rows
    df.drop(df[df['variable'] == 'B'].index, inplace = True)
    print(df)
    print("\n")
      
if (__name__)=="__main__":
    main()