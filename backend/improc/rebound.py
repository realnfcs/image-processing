import numpy as np
import cv2 as cv

def rebound(f:np.ndarray,type:int) -> np.ndarray:

    """
    Apply the rebound in the image and returns the result
 
    Args:
      f : (array_like Shape (m,n)) first image 
      type: (integer number) the parameter that defines the type of the rebound
    Returns

      output: (array_like Shape (m,n)) the output image of rebound process
      
    """
      
    row = f.shape[0]
    col = f.shape[1]

    output:np.ndarray = np.zeros((row,col), dtype=f.dtype)

    for i in range(row):
        for j in range(col):
            if type == 1:
                il = j
                jl = row - 1 - i
                output[il,jl] = f[i,j]
            
            elif type == 2:
                output[j,i] = f[i,j]
            
            else:
                print("error")

    output = np.uint8(output)
    return output 
