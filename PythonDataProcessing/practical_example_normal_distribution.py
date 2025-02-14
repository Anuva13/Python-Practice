import numpy as np
import matplotlib.pyplot as plt

def main():
    
    simulating_height()
    simulating_IQ_score()      

def simulating_height():
    # Generate 10,000 random heights with a normal distribution
    heights = np.random.normal(loc=170, scale=10, size=10000)

    # Plot the histogram
    plt.hist(heights, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title("Distribution of Human Heights")
    plt.xlabel("Height (cm)")
    plt.ylabel("Frequency")
    plt.show()
    
def simulating_IQ_score():
    #Generate 5000 IQ scores i.e. IQ scores are normally distributed with a mean of 100 and a standard deviation of 15.
    iq_scores = np.random.normal(loc=100, scale=15, size=50000)
    
    # Plot the histogram
    plt.hist(iq_scores, bins=30, density=True, alpha=0.6, color='b', edgecolor='black')
    plt.title("Distribution of Human IQ Scores")
    plt.xlabel("IQ Score")
    plt.ylabel("Density")
    plt.show()
    
if (__name__)== "__main__":
    main()
