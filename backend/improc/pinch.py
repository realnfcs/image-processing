import numpy as np


def pinch(f:np.ndarray, fmax:float, ip:int ) -> np.ndarray:
    """
    Apply the histogram equalization to the histogram of the inserted image
 
    Args:
      f : (array_like Shape (m,n)) first image  
      fmax: (float number) the number that defines the intensity of the pinch
      ip: (integer number) the integer number that defines the center line that will
                           receive the pinch
    Returns
      output: (array_like Shape (m,n)) the output image of pinch process
                                  
    """

    row,col,ch = f.shape

    output:np.ndarray = np.zeros((row,col,ch), dtype=f.dtype)

    for i in range(row):
        for j in range(col):
            if i <= ip:
                nx = int(np.abs(((fmax - 1) / (row - 1 - ip)) * (i - ip) + fmax))
                

            else:
                nx = int(np.abs((-(fmax - 1) / (row - 1 - ip)) * (i - ip) + fmax))
                


    
    return output.astype(f.dtype)
