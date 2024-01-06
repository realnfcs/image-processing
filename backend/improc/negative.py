import numpy as np
import cv2 as cv

img = "/home/andrey/PDI_project/imagens/legumes.tiff"
img_test = cv.imread(img)

def negative(f:np.ndarray) -> np.ndarray:

    row, col, _ = f.shape
    l = np.max(f)

    output:np.ndarray = np.zeros((row, col, 3), dtype = f.dtype)

    for i in range(row):
        for j in range(col):

            output[i,j] = l - 1 - f[i,j]

    return output

output = negative(img_test)

cv.imshow("image",img_test)
cv.imshow("Output",output)
cv.waitKey(0)
cv.destroyAllWindows()



