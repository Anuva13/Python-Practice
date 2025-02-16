import pandas as pd
import numpy as np
def main():
    
    #creating_tensor()
    convert_3d_to_2d_array()
    
def creating_tensor():
    tensor = np.random.randint(0, 10, size=(2,3,4))
    print(tensor)
    
def convert_3d_to_2d_array():
    # Create a 3D NumPy array (2 blocks of 3×4 matrices)
    tensor = np.random.randint(0,10, size = (2,3,4))
    # Reshape 3D (2, 3, 4) → 2D (6, 4) to fit in DataFrame
    reshaped_tensor = tensor.reshape(-1,4)
    # Convert to DataFrame
    df=pd.DataFrame(reshaped_tensor, columns = ("A","B","C","D"))
    print(df)   

if (__name__) == "__main__":
    main()    
