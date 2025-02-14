import pandas as pd
import numpy as np
import array as arr
def main():
    
    creating_array()
    array_operations()
    
def creating_array():
    #creating array using the array module 
    a = arr.array('i', [1,2,3,4,5]) #i denoting the integer type
    print(a)
    
    #creating array using NumPy arrays
    b = np.array([1,2,3,4,5])
    print(b)

def array_operations():
    #Element-wise Addition & Multiplication
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a + b)   # [5 7 9]
    print(a * b)   # [4 10 18]
    print("\n")

    #Reshaping an Array
    matrix = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
    print(matrix)
    print("\n")
    
    #Generating random arrays
    random_arr = np.random.randint(1, 10, size=(3, 3))  # 3x3 matrix with random integers
    print(random_arr)
    print("\n")
    
if (__name__) == ("__main__"):
    main()