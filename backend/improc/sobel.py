import numpy as np

"""
sobel.py
    functions to processing sobel filter for edge detection
""" 

def sobel(f: np.ndarray, t: int) -> np.ndarray:
    """
    Apply the sobel filter
 
    Args:
      f: (array_like Shape (m,n)) input image in grayscale
      t: (scalar) the threshold
    Returns
      output: (array_like Shape (m,n)) the image output in grayscale
                                  
    """

    f = f.astype(np.float64)

    row, col = f.shape

    mx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    my = [[-1,-2,-1],[-0,0,0],[1,2,1]]

    output:np.ndarray = np.zeros((row,col), dtype=f.dtype)

    for i in range(1, row - 2):
        for j in range(1, col - 2):
            
            gx = np.sum(np.sum(mx * f[i - 1:i + 2, j - 1:j + 2]))
            gy = np.sum(np.sum(my * f[i - 1:i + 2, j - 1:j + 2]))

            output[i + 1, j + 1] = np.sqrt(np.power(gx, 2) + np.power(gy, 2))

            if np.max(output[i, j]) < t:
                output[i, j] = 0
            
    return output.astype(np.uint8)
