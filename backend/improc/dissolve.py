import numpy as np

"""
dissolve.py
    functions common to all dissolve processing
""" 

def non_uniform_cross_dissolve(f:np.ndarray, g:np.ndarray, t:np.ndarray) -> np.ndarray:
    """
    Apply the uniform closs dissolve with two image in a output one
 
    Args:
      f : (array_like Shape (m,n)) fist image 
      g : (array_like Shape (m,n)) second image 
      t : (array_like Shape (m,n))      
    Returns
      output: (array_like Shape (m,n)) the image output of uniform closs dissolve process
                                  
    """

    if f.shape != g.shape:
        raise ValueError("images don't have the same size")
    
    row, col = f.shape
    output: np.ndarray = np.zeros((row, col), dtype = f.dtype)

    for i in range(row):
        for j in range(col):    
            
            output[i, j] = (1 - t[i,j])  * f[i,j] + t[i,j] * g[i,j]
    
    return output

def uniform_closs_dissolve(f: np.ndarray, g: np.ndarray, t: float) -> np.ndarray:
    """
    Apply the uniform closs dissolve with two image in a output one
 
    Args:
      f : (array_like Shape (m,n)) fist image 
      g : (array_like Shape (m,n)) second image 
      t : (scalar float [0, 1])    constant value for dissolve process      
    Returns
      output: (array_like Shape (m,n)) the image output of uniform closs dissolve process
                                  
    """

    if f.shape != g.shape:
        raise ValueError("images don't have the same size")

    row, col = f.shape

    output: np.ndarray = np.zeros((row, col), dtype=f.dtype)

    for i in range(row):
        for j in range(col):
            output[i, j] = (1 - t) * f[i, j] + t * g[i, j]

    return output

    