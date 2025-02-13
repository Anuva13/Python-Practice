# Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():

    # Creating an empty dataframe to store the randomly generated column values
    df = pd.DataFrame()

    # set a sample size
    N = 5000
    
    # rand_col_1 generates 5000 numbers between 0 and 1 having equal probability of occurrence
    df['rand_col_1'] = np.random.RandomState(0).uniform(0, 1, size=N)
    
    # rand_col_2 generates 5000 numbers from normal distribution with mean=0 and standard deviation=1
    df['rand_col_2'] = np.random.RandomState(0).normal(0, 1, size=N)
    
    """
       rand_col_3 generates 5000 numbers having 10 trials with each trial 
       having a success rate of 0.7
       i.e. a biased coin when tossed 10 times will have the probability of 
       70% getting heads and 30% tails
    """
    df['rand_col_3'] = np.random.RandomState(0).binomial(10, 0.7, size=N)
    
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