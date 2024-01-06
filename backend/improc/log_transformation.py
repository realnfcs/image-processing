import numpy as np
import cv2 as cv


test = "/home/andrey/PDI_project/imagens/fisico.tif"
img = cv.imread(test)

def log_transformation(f:np.ndarray, c:float) -> np.ndarray:
    
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