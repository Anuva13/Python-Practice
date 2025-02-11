import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def main():

    data = np.random.choice(['sunny', 'rain', 'cloudy', 'windy'], 1000, p=[1/4.0, 1 / 4.0, 1 / 4.0, 1/4.0])
    df = pd.DataFrame(data=data, columns=['weather'])

    df['weather'].value_counts().plot(kind='bar')
    plt.show()

if (__name__) == "__main__":
    main()