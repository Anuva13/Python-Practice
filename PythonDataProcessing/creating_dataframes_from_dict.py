import pandas as pd
def main():
    
    create_csv_to_df()
    create_api_json_data_to_df()
    create_user_input_to_df()

    
def create_csv_to_df():
    
    list_of_dicts = [
        {
            'date': '2018-03-04',
            'weather': 'cloudy'
        },
        {
            'date': '2018-03-05',
            'weather': 'sunny'
        },
        {
            'date': '2018-03-06'
        },
        {
            'date': '2018-03-07',
            'weather': 'rain'
        }
    ]
    df = pd.DataFrame(list_of_dicts)
    print(df)
    print("\n")

def create_api_json_data_to_df():
    
    # Simulated API JSON response (list of dicts)
    data =[{"name": "Lessie", "age": 35, "city": "New Jersey"},
           {"name": "Bani", "age": 33, "city": "Omaha"},
           {"name": "Kat", "age": 31, "city": "California"}]
    
    df = pd.DataFrame(data)
    print(df)
    print("\n")
    
def create_user_input_to_df():
    users = []
    users.append({"ID": 1, "Name": "John", "Score": 85})
    users.append({"ID": 2, "Name": "Emily", "Score": 92})
    users.append({"ID": 3, "Name": "Mike", "Score": 78})

    df = pd.DataFrame(users)
    print(df)
    print("\n")
    

    
if (__name__) == ("__main__"):
    main()