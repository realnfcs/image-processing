import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

test = "/home/andrey/PDI_project/imagens/lena_gray_512.tif"
img = cv.imread(test)

grayscale_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

def histogram_equalization(f:np.ndarray) -> np.ndarray:
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
            output[i,j] = eqh[f[i,j]] #o erro está no f[i,j] quando a imagem tem mais de 256 pixels na linha o codigo nao funciona
    
    
    return output


output = histogram_equalization(grayscale_img)

hist_img = cv.calcHist([img],[0],None,[256],[0,256])
hist_output = cv.calcHist([output],[0],None,[256],[0,256])

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(hist_img, color='blue')
axs[0].set_title('Histograma Original')
axs[1].plot(hist_output, color='red')
axs[1].set_title('Histograma Equalizado')

plt.tight_layout()
plt.show()

cv.imshow("image",grayscale_img)
cv.imshow("output",output)
cv.waitKey(0)
cv.destroyAllWindows()


