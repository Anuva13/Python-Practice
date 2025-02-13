"""import numpy as np
import matplotlib.pyplot as plt

def main():
    
    simulating_height()      


def simulating_height():
    # Generate 10,000 random heights with a normal distribution
    heights = np.random.normal(loc=170, scale=10, size=10000)

    # Plot the histogram
    plt.hist(heights, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title("Distribution of Human Heights")
    plt.xlabel("Height (cm)")
    plt.ylabel("Frequency")
    plt.show()
    
if (__name__)== "__main__":
    main()
