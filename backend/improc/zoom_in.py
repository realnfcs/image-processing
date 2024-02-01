import numpy as np
import cv2 as cv

def zoom_in_replication(img:np.ndarray, factor:float)->np.ndarray:
    row,col,ch = img.shape
    
    new_row = int(row * factor)
    new_col = int(col * factor)


    output:np.ndarray = np.zeros((new_row,new_col,ch), dtype=img.dtype)
    
    for i in range(new_row):
        for j in range(new_col):

            origin_row = int(i / factor)
            origin_col = int(j / factor)

            origin_row = min(origin_row, row -1)
            origin_col = min(origin_col, col - 1)


            
            output[i,j,:] = img[origin_row,origin_col,:]

    
    return output      

img = cv.imread("./images/lena_gray_256.tif")
output = zoom_in_replication(img,3)

cv.imshow("image",img)
cv.imshow("Output",output)
cv.waitKey(0)
cv.destroyAllWindows()
