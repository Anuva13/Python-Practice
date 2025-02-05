import pandas as pd
def main():

    create_series()
    custom_index()
   
def create_series():
    # Creating a simple Series
    data = [10, 20, 30, 40, 50]
    series = pd.Series(data)
    print(series)
    
def custom_index():
    # Creating a series with custom index
    series_custom = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
    print(series_custom)


if __name__ == "__main__":
    main()