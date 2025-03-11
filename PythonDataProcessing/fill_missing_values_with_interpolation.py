import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    # Sample data with missing values
    data = {'value': [1, 2, np.nan, 4, 5, np.nan, 7]}
    df = pd.DataFrame(data)

    # Option 1: Fill missing values using mean
    df['value'].fillna(df['value'].mean(), inplace=True)

    # Option 2: Fill missing values using interpolation
    df['value'].interpolate(method='linear', inplace=True)

    # Plot the data
    df['value'].plot(title="Line Plot with Filled Missing Values")
    plt.show()

if __name__ == "__main__":
    main()
