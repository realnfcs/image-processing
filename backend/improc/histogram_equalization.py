import numpy as np
import cv2 as cv

def histogram_equalization(f:np.ndarray) -> np.ndarray:
    """
    Apply the histogram equalization to the histogram of the inserted image
 
    Args:
      f : (array_like Shape (m,n)) first image    
    Returns
      output: (array_like Shape (m,n)) the output image of histogram equalization process
                                  
    """

    bit_depth = f.dtype.itemsize * 8

    L = np.power(2,bit_depth)

    row,col = f.shape

    hist_img = cv.calcHist([f], [0], None ,[256], [0,256])

    acsum = np.cumsum(hist_img)

    eqh = np.zeros(L , dtype = hist_img.dtype)

    output:np.ndarray = np.zeros((row,col),dtype = f.dtype)

    for i in range(L):
        eqh[i] = np.round(((L-1)/(row * col)) * acsum[i])
    
    for i in range(row):
        for j in range(col):
            output[i,j] = eqh[f[i,j]] 
    
    return output





