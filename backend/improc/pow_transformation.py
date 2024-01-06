import numpy as np
import cv2 as cv


test = "/home/andrey/PDI_project/imagens/fratura.png"
img = cv.imread(test)

c = 1

y = 0.4

def pow_transformation(f:np.ndarray, c:int, y:float) -> np.ndarray:

    row,col,_ = f.shape

    output:np.ndarray = np.zeros((row,col,3), dtype=f.dtype)

    for i in range(row):
        for j in range(col):

            output[i,j] = c * np.power(f[i,j], y)
    
    return output


output = pow_transformation(img , c, y)


cv.imshow("image",img)
cv.imshow("output",output)
cv.waitKey(0)
cv.destroyAllWindows()