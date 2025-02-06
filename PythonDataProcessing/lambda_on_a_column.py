import pandas as pd

def main():
    simple_addition()
    lambda_with_map()
    lambda_with_filter()
    lambda_sorting()
    apply_lambda_on_column()
    apply_lambda_on_column_using_index()
    
def simple_addition():
    # Adding two integers
    add = lambda x, y: x+y
    print(add(5,3))
    
def lambda_with_map():
    # Perform operations on list using map() to cube all elements of a list
    numbers = [1,2,3,4,5,6,7,8,9,10]
    cubes = list(map(lambda x:x** 3, numbers))
    print(cubes)

def lambda_with_filter():
    #Perform fliter operation on list
    numbers = [1, 2, 3, 4, 5, 6]
    odd = list(filter(lambda x: x % 2 != 0, numbers))
    print(odd)
    
def lambda_sorting():
    #Perform sort on list
    data = [(1, 'banana'), (3, 'apple'), (2, 'cherry')]
    sorted_data = sorted(data, key=lambda x: x[1])  # Sort by fruit name
    print(sorted_data)

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
    
    
if (__name__) == "__main__":
    main()