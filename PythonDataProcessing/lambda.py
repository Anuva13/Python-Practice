import pandas as pd

def main():
    # apply_lambda_on_column()
    apply_lambda_on_column_using_index()
    

def apply_lambda_on_column():
    df = pd.read_csv("./ExampleCSV/I_Sample1.csv")
    
    df['Department'] = df['Department'].apply(lambda x: x.lower())
    df['Age'] = df['Age'].apply(lambda x: x+5)
    print(df)

    
def apply_lambda_on_column_using_index():
    """
    Since the aim of this method is to select columns using there indices instead of the column names:
    (i) we need to make the header none while loading csv to the dataframe which will eliminate column names values and replace it with integers
    which can be used for selecting column values
    (ii) we also need to skip the first row as the first row holds the column names
    
    """
    df = pd.read_csv("./ExampleCSV/I_Sample1.csv", header = None, skiprows=1)
    df[3] = df[3].apply(lambda x: x.lower())
    df[1] = df[1].apply(lambda x: x+5)
    print(df)
    
    
if __name__ == "__main__":
    main()