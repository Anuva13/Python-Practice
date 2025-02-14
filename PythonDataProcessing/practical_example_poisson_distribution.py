import numpy as np
import matplotlib.pyplot as plt
def main():
    
    #customer_visit()
    website_traffic()
    
def customer_visit():
    lam, size = 10, 5000  # Average 10 customers per hour
    data = np.random.poisson(lam, size)

    plt.hist(data, bins=20, edgecolor="black", alpha=0.7)
    plt.xlabel("Number of Customers Per Hour")
    plt.ylabel("Frequency")
    plt.title("Poisson Distribution - Customer Arrivals")
    plt.show()

def website_traffic():
    lam, size = 300, 5000  # Average 300 requests per minute
    data = np.random.poisson(lam, size)

    plt.hist(data, bins=20, edgecolor="black", alpha=0.7)
    plt.xlabel("Number of Requests per minute")
    plt.ylabel("Frequency")
    plt.title("Poisson Distribution - Website Traffic")
    plt.show()

if (__name__) == "__main__":
    main()
