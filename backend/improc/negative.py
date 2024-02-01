import numpy as np

def negative(f:np.ndarray) -> np.ndarray:

    """
    Applies the negative transform to the image and returns the result
 
    Args:
      f : (array_like Shape (m,n)) first image 
           
    Returns
    
      output: (array_like Shape (m,n)) the output image of negative transform process
      
    """

    row, col, _ = f.shape
    l = np.max(f)

    output:np.ndarray = np.zeros((row, col, 3), dtype = f.dtype)

    for i in range(row):
        for j in range(col):

            output[i,j] = l - 1 - f[i,j]

    return output




