""" def main():

   
    a = "Anuva"
    l = len(a)
    #print("The length of the string is:", l)
    print(1,2,3,4, sep=".")

if __name__ == "__main__":
    main()
"""
"""   
# Checking the installation of openpyxl package
import importlib.util

def main():

    if importlib.util.find_spec("openpyxl") is not None:
        print("openpyxl is installed")
    else:
        print("openpyxl is NOT installed")
    
if (__name__) == "__main__":
    main()
    
"""


# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():

    # Creating an empty dataframe to store the randomly generated column values
    df = pd.DataFrame()

    # set a sample size
    N = 5000
    
    """
    rand_col_4 Models the number of random events in a fixed time interval
    generates 5000 numbers having a mean of 5
    """
    df['rand_col_4'] = np.random.RandomState(1).poisson(5, size=N)

    # plots the histogram for all the four columns
    df.hist(bins=10,  edgecolor='black')
    plt.show()
    
if (__name__) == "__main__":
    main()