import pandas as pd
def main():

    create_series()
    custom_index()
    create_dataframe()
    sampling_dataframe()
    sampling_using_loc()
   
def create_series():
    # Creating a simple Series
    data = [10, 20, 30, 40, 50]
    series = pd.Series(data)
    print(series)
    print("\n")
    
def custom_index():
    # Creating a series with custom index
    series_custom = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
    print(series_custom)
    print("\n")
    
def create_dataframe():
    # Creating a DataFrame
    data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    print(df)
    print("\n")    
    
def sampling_dataframe():
    data = {
    'Name': ['Apple', 'Banana', 'Guava'],
    'Qty': ['1kg', '3dozens', '6pieces'],
    'Price': ['$3.8', '$4.5', '$2,3']   
    }
    df = pd.DataFrame(data)
    #Printing a single column
    print(df['Name'])
    print("\n")
    #Printing multiple columns
    print(df[['Name','Price']])
    print("\n")

def sampling_using_loc():
    data = {
    'Name': ['Apple', 'Banana', 'Guava'],
    'Qty': ['1kg', '3dozens', '6pieces'],
    'Price': ['$3.8', '$4.5', '$2.3']   
    }
    #df = pd.DataFrame(data)
    df = pd.DataFrame(data, index=['a','b','c'])
    # selecting and printing the second row
    print(df.loc['a'])
    print("\n")
    # selecting and printing the third row
    print(df.iloc['a'])
    print("\n")

if __name__ == "__main__":
    main()