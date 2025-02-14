import numpy as np
import matplotlib.pyplot as plt
def main():

    #manufacturing()
    medical_trial()

def manufacturing():
    n, p, size = 100, 0.05, 5000  # 100 bulbs, 5% defect rate, 5000 simulations
    data = np.random.binomial(n, p, size)

    plt.hist(data, bins=15, edgecolor="black", alpha=0.7)
    plt.xlabel("Number of Defective Bulbs in 100")
    plt.ylabel("Frequency")
    plt.title("Binomial Distribution - Defective Light Bulbs")
    plt.show()
    
def medical_trial():
    patients, success_rate, size = 500, 0.8, 5000  #500 patients, 80% success rate, 5000 simulations
    data = np.random.binomial(patients, success_rate, size)
    
    #plotting the histogram
    plt.hist(data, bins=30, density=True, alpha=0.6, color='purple', edgecolor='black')
    plt.xlabel("Number of Successful Trials in 500 patients")
    plt.ylabel("Success Rate")
    plt.title("Binomial Distribution - Successful Drug Trials")
    plt.show()

if (__name__)=="__main__":
    main()
