import pandas as pd
from io import StringIO

def main():
    """
    Concepts Covered:
    Reading CSV data from a string.
    Using multi-indexing in Pandas (date and language).
    Sorting a multi-indexed DataFrame.
    Index-based slicing using .loc[]:
    Retrieving all records for a given date.
    Retrieving a specific record for a date-language pair.
    
    """
    
    
    
    str_data = """date,language,ex_complete
2017-01-01,python,6
2017-01-02,python,5
2017-01-03,python,10
2017-01-01,r,8
2017-01-02,r,8
2017-01-03,r,8
"""
    
    df = pd.read_csv(StringIO(str_data))
    
    #Sets a multi-index using date and language
    df.set_index(['date', 'language'], inplace=True)
    #Sorts the DataFrame by the multi-index to ensure proper slicing
    df.sort_index(inplace=True)

    print(df.index)

    # Slice for all languages on a specific date
    s = df.loc['2017-01-02']
    print(s)

    # Slice for a specific date and language
    s = df.loc[('2017-01-02', 'r')]
    print(s)

if __name__ == "__main__":
    main()
