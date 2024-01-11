import numpy as np
import cv2 as cv


test = "/home/andrey/PDI_project/imagens/legumes.tiff"
img = cv.imread(test)

def rotation(f:np.ndarray, angle:int):
    row = f.shape[0]
    col = f.shape[1]
    ch = f.shape[2]

    ic = row / 2
    jc = col / 2

    output:np.ndarray = np.zeros((row,col,ch), dtype=f.dtype)


    angle_r = np.radians(angle)

    for i in range(row):
        for j in range(col):
            
            il = int(np.round((i - ic) * np.cos(angle_r)) - ((j - jc) * np.sin(angle_r)) + ic)
            jl = int(np.round((i - ic) * np.sin(angle_r)) + ((j - jc) * np.cos(angle_r)) + jc)

            print(np.degrees(np.cos(angle)))

            if (il <= row-1 and il > 0) and (jl <= col-1 and jl > 0):
                output[il,jl] = f[i,j]
        
    output = np.uint8(output)
    return output

output = rotation(img,45)

cv.imshow("image",img)
cv.imshow("Output",output)
cv.waitKey(0)
cv.destroyAllWindows()