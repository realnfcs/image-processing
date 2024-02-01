import numpy as np

def histogram_expansion(f:np.ndarray) -> np.ndarray:
    """
    Apply the histogram expansion to the histogram of the inserted image
 
    Args:
      f : (array_like Shape (m,n)) first image    
    Returns
      output: (array_like Shape (m,n)) the output image of histogram expansion process
                                  
    """
    
    L = 256 -1

    rmin = np.min(f)
    rmax = np.max(f)

    row,col = f.shape

    output:np.ndarray = np.zeros((row,col), dtype=f.dtype)

    for i in range(row):
        for j in range(col):

            output[i,j] = np.round(((f[i,j] - rmin)/(rmax - rmin)) * L)
            
    
    return output

