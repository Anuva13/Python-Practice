import pandas as pd
def main():
    
    # Creating a DataFrame
    data = pd.read_csv("./ExampleCSV/I_Sample5.csv")

    # Converting categorical variables into dummy variables (canonical variables
    data_encoded = pd.get_dummies(data, columns=["Income_Level", "Preferred_Store"], drop_first=True)
    print(data_encoded)
    
if (__name__) == "__main__":
    main()