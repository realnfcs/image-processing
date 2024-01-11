import numpy as np
import cv2 as cv


test = "/home/andrey/PDI_project/imagens/legumes.tiff"
img = cv.imread(test)

def rebound(f:np.ndarray,type:int) -> np.ndarray:
    row = f.shape[0]
    col = f.shape[1]
    ch = f.shape[2]

    output:np.ndarray = np.zeros((row,col,ch), dtype=f.dtype)

    for i in range(row):
        for j in range(col):
            if type == 1:
                il = j
                jl = row - 1 - i
                output[il,jl] = f[i,j]
            
            elif type == 2:
                output[j,i] = f[i,j]
            
            else:
                print("error")

    output = np.uint8(output)
    return output

output = rebound(img,2)
            


cv.imshow("image",img)
cv.imshow("Output",output)
cv.waitKey(0)
cv.destroyAllWindows()