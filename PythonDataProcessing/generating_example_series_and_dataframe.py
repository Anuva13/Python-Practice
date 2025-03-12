import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():
    
    #Generating a series object in pandas having 50 random values
    s = pd.Series(np.random.randn(50))
    print(s.head())
    print("\n")
    #Plotting the generated series
    s.hist(bins=10)
    plt.show()
    
    #Creating a dataframe of 20 values containing numbers between 0-10
    np.random.seed(0)
    df = pd.DataFrame(np.random.randint(0, 10, (20, 3)), columns = list("ABC"))
    print(df)
    print("\n")
    
    #Sampling 70% of the total rows from the DataFrame. As replace =True rows can be repeated.
    df_sampled = df.sample(frac=0.7, replace=True, random_state=3)
    print(df_sampled)
    
if (__name__) == "__main__":
    main()