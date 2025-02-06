# Imported the Pandas package and aliased it as pd
import pandas as pd

""" 
    I have imported only Decimal class from decimal module so as to operate with decimal numbers.
    I have not imported the entire decimal module as it would result in poor performce 
    and also have a name space issue and enaballing cleaner coding.  
"""
from decimal import Decimal

def main():
    
    # Loading csv file in a data frame
    df = pd.read_csv("./ExampleCSV/I_Sample2.csv")
    
    #Creating a new column label to display the output of the function create_price_label
    df['label'] = df.apply(create_price_label, axis=1)
    
    # Saving the concatenated data in a new csv O_Sample2.csv
    df.to_csv("./ExampleCSV/O_Sample2.csv", index=False)
    
 
# Creating new label by concatinating the value of each row  
def create_price_label(row):
    price = Decimal(row['price'])
    price = round(price, 2)
    return row['name'].title() + " $" + str(price)

if __name__ == "__main__":
    main()   
        
