import numpy as np

def main():
    
    roulette_spin()
    data_augmentation()
    stockprice_variance()
    randomised_AB_testing()
    
def roulette_spin():
    # Simulating a roulette wheel (0-36, equally likely)
    roulette_spin = np.random.uniform(0, 37, size=1).astype(int)
    print(roulette_spin)
    
def data_augmentation():
    # Random brightness adjustment factor between 0.8 and 1.2
    brightness_factor = np.random.uniform(0.8, 1.2, size=1)
    print(brightness_factor)
    
def stockprice_variance():
    # Random daily stock price changes between -2% and +2%
    price_changes = np.random.uniform(-0.02, 0.02, size=10)
    print(price_changes)
    
def randomised_AB_testing():
    # Randomly assign 1000 users to group A (50%) or group B (50%)
    user_groups = np.random.uniform(0, 1, size=1000) < 0.5
    print(sum(user_groups), "users in Group A")
    print(1000 - sum(user_groups), "users in Group B")

if (__name__) == "__main__":
    main()
