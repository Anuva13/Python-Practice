# Imported the Pandas package and aliased it as pd
import pandas as pd

def main():
    #same_value_detection()
    nan_value_detection()
    
def same_value_detection():
    df = pd.read_csv("./ExampleCSV/I_WeatherData1.csv")
    assert (df['weather'] == 'sunny').all(), "Values are not the same in the column"
    print (df)
    
def nan_value_detection():
     df = pd.read_csv("./ExampleCSV/I_WeatherData1.csv")
     # Checking all the columns of the dataframe if there is a null value
     print(df.isnull().any())
     
     # Checking specifically in the weather column if it has a null value
     print(df['weather'].isnull().any())

     # Replacing the NaN value in the weather column with 'cloudy'
     df.iloc[1, 1] = 'cloudy'
     print(df)
     """
        Now trying to assert that none of the columns have null value, we are doing .any() for the first time
        to check individual columns contains null or not.
        But for the asset function we need to get just one output either true/false to prevent unambiguity. So 
        we do another any() to combine all the outputs of the first any() statement
     """
     assert not (df.isnull().any().any()), "No value should be missing"
    
if __name__ == "__main__":
    main()
    