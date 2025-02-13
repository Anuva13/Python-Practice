# Randomly picking a lottery ticket number with each number having the same probability for occuring
import numpy as np
def main():
      
    winning_ticket = np.random.randint(1, 1001)  # Random number between 1 and 1000  
    print(f"The winning ticket number is: {winning_ticket}")
    
if (__name__) == "__main__":
    main()

    """
    Since each number has an equal probability of being chosen, the system remains fair and unbiased.
    This same concept applies in shuffling cards, random password generation, or even load balancing in 
    servers where requests are distributed evenly across different resources.
    """