import numpy as np


def log_transformation(f:np.ndarray, c:float) -> np.ndarray:

    """
    Apply the logarithmic transform to the image and returns the result
 
    Args:
      f : (array_like Shape (m,n)) first image 
      c: (float number) adjustment parameter

    Returns
    
      output: (array_like Shape (m,n)) the output image of logarithmic transform process
      
    """
    
    row, col, _ = f.shape

    output:np.ndarray = np.zeros((row, col, 3), dtype=f.dtype)
    

    for i in range(row):
        for j in range(col):
            output[i, j]= c * np.log1p(f[i,j])

    return output

