import pandas as pd
import importlib.util

def main():

    if importlib.util.find_spec("openpyxl") is not None:
        print("openpyxl is installed")
    else:
        print("openpyxl is NOT installed")
    
    readcsv()
    parameters()

def readcsv():
     # Load CSV file into a DataFrame
    df = pd.read_csv("./ExampleCSV/I_Sample3.csv")
    print(df)
    
def parameters():
    # Read CSV with specified parameters
    df = pd.read_csv("./ExampleCSV/I_Sample3.csv", 
                 sep=";",        # Uses semicolon as delimiter
                 header=None,    # No headers in file
                 index_col=0,    # Use first column (ID) as index
                 usecols=[1, 2], # Load only columns Name and Age
                 nrows= 4)       # Load only first 4 rows

    # Display the DataFrame
    print(df)
    



if (__name__) == "__main__":
    main()