import pandas as pd
import numpy as np
def main():
    
    creating_matrix()
    matrix_operations()
    
def creating_matrix():
    
    #Using lists of lists
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix[0][2]) # Accessing element (row 1, col 2) → Output: 6
    print("\n)")
    
    #Using numpy arrays
    matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(matrix)
    print("\n")
    
    #Using Pandas DataFrame
    matrix = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
    print(matrix)
    print("\n")
    
    #Creating Random 2D matrix  having 3 rows 4 column
    matrix = np.random.randint(0,10,(3,4))
    print(matrix)
    print("\n")
    
def matrix_operations():
    matrix_A = np.random.randint(0,10,(3,3))
    matrix_B = np.random.randint(0,10,(3,3))
    
    #Addition
    print("Addition")
    print(matrix_A + matrix_B)
    print("\n")
    
    #Subtraction
    print("Subtraction")
    print(matrix_A - matrix_B)
    print("\n")
    
    #Elementwise multiplication
    print("Multiplication")
    print(matrix_A * matrix_B)
    print("\n")
    
    #Scalar multiplication
    print("Scalar Multiplication")
    print(2 * matrix_A)
    print("\n")
    
    #Dot Product
    print("Dot Product")
    result = np.dot(matrix_A,matrix_B)
    print(result)
    print("\n")
    
    #Matrix Transposition
    print("Transpose")
    print(matrix_A)
    print("\n")
    print(matrix_A.T)
    print("\n")
    
    
if (__name__) == "__main__":
    main()
