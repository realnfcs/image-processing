import numpy as np



def thresholding(f:np.ndarray, t:int) -> np.ndarray:

    """
    Apply the thresholding to the image and returns the result
 
    Args:
      f : (array_like Shape (m,n)) first image 
      t: (integer number) the threshold number
           
    Returns
    
      output: (array_like Shape (m,n)) the output image of thresholding process
      
    """

    row, col = f.shape

    output:np.ndarray = np.zeros((row,col), dtype=f.dtype)

    for i in range(row):
        for j in range(col):
            if (f[i][j] < t).any():
                output[i,j] = 0
            
            else:
                output[i,j] = 255

    return output

            
