import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def main():
    
    get_dummies()
    one_hot_encoder()
       
def get_dummies():

    # Create a DataFrame with a categorical column
    df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']})
    print(df)
    print("\n")
    df_dummies=pd.get_dummies(df, columns=['Color'])
    print(df_dummies)
    print("\n")
    
def one_hot_encoder():
    # Create a DataFrame with a categorical column
    df = pd.DataFrame({'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']})
    print(df)
    print("\n")
    encoder = OneHotEncoder(drop='first', sparse_output=False)
    encoded = encoder.fit_transform(df[['Color']])
    print(encoded)
    
if (__name__)=="__main__":
    main()

    
    
