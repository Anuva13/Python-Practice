import pandas as pd
from tabulate import tabulate
def main():
    
    # data
    data = {
                'product_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                'product_name': [
                    'Apple iPhone 13', 'Samsung Galaxy S21', 'Apple MacBook Pro', 
                    'Dell XPS 15', 'Apple Watch Series 7', 'Sony WH-1000XM4', 
                    'Apple AirPods Pro', 'Google Pixel 6', 'Apple iPad Air', 
                    'Bose QuietComfort 45'
                ],
                'category': [
                    'Electronics', 'Electronics', 'Electronics', 
                    'Laptops', 'Wearables', 'Headphones', 
                    'Audio', 'Electronics', 'Tablets', 
                    'Headphones'
                ],
                'price': [799, 699, 1299, 1199, 399, 349, 249, 599, 599, 329]
            }

    df = pd.DataFrame(data=data)
    print(tabulate(df, headers='keys', tablefmt='plsql'))
    print("\n") 
    
    #Data Cleaned to tabulate only 'apple products' from dataset
    filtered_data = df[df['product_name'].str.contains('Apple', case=False)]
    print("Only Apple Products\n")
    print(tabulate(filtered_data, headers='keys', tablefmt='plsql'))
    print("\n")
    
    #Handling categorical data to tabulate only products of category 'Headphones'
    filtered_data = df[df['category'].str.contains('Headphones', case=False)]
    print("Only Headphones\n")
    print(tabulate(filtered_data, headers='keys', tablefmt='plsql'))
    print("\n")
        
if (__name__) == "__main__":
    main()

