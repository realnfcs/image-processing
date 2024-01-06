import numpy as np
import cv2 as cv


img = "/home/andrey/PDI_project/imagens/legumes.tiff"
img_test = cv.imread(img)

t = 100

def thresholding(f:np.ndarray, t:int) -> np.ndarray:

    row, col, _ = f.shape

    output:np.ndarray = np.zeros((row,col,3), dtype=f.dtype)

    for i in range(row):
        for j in range(col):
            if (f[i][j] < t).any():
                output[i,j] = 0
            
            else:
                output[i,j] = 255

    return output

output = thresholding(img_test,t)

cv.imshow("image",img_test)
cv.imshow("Output",output)
cv.waitKey(0)
cv.destroyAllWindows()
            
