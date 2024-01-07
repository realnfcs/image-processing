import numpy as np
import cv2 as cv


test = "/home/andrey/PDI_project/imagens/fisico.tif"
img = cv.imread(test)

def log_transformation(f:np.ndarray, c:float) -> np.ndarray:

    """
    Applies the logarithmic transform to the image and returns the result
 
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

output = log_transformation(img,  40)

cv.imshow("image",img)
cv.imshow("output",output)
cv.waitKey(0)
cv.destroyAllWindows()