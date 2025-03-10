import numpy as np
def main():

    # Define the coefficient matrix (A)
    A = np.array([[2, 3, -1, 4],
                [1, -2, 3, 1],
                [4, 1, 2, -3],
                [3, -1, 4, 2]])

    # Define the constants matrix (B)
    B = np.array([10, 5, 8, 12])

    # Solve for [x, y, z, w]
    solution = np.linalg.solve(A, B)

    # Print the solution
    x, y, z, w = solution
    print(f"Solution:\n x = {x}\n y = {y}\n z = {z}\n w = {w}")

if (__name__) == "__main__":
   main() 
