import numpy as np


def pow_transformation(f:np.ndarray, c:int, y:float) -> np.ndarray:

    """
    Apply the power transform to the image and returns the result
 
    Args:
      f : (array_like Shape (m,n)) first image 
      c: (integer number) adjustment parameter
      y: (float number) power parameter

    Returns

      output: (array_like Shape (m,n)) the output image of power transform process
      
    """

    row, col = f.shape

    output:np.ndarray = np.zeros((row,col), dtype=f.dtype)

    for i in range(row):
        for j in range(col):

            output[i,j] = c * np.power(f[i,j], y)
    
    return output
