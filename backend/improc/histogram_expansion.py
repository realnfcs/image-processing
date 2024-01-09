import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#normalizar a imagem antes de mandá-la para a função
test = "/home/andrey/PDI_project/imagens/macaco.tiff"
img = cv.imread(test)

grayscale_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)


def histogram_expansion(f:np.ndarray) -> np.ndarray:
    
    L = 256 -1

    rmin = np.min(f)
    rmax = np.max(f)

    row,col = f.shape

    output:np.ndarray = np.zeros((row,col), dtype=f.dtype)

    for i in range(row):
        for j in range(col):

            output[i,j] = np.round(((f[i,j] - rmin)/(rmax - rmin)) * L)
            
    
    return output

output = histogram_expansion(grayscale_img)
#output = np.uint8(output)

hist_img = cv.calcHist([img],[0],None,[256],[0,256])
hist_output = cv.calcHist([output],[0],None,[256],[0,256])

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(hist_img, color='blue')
axs[0].set_title('Histograma Original')

axs[1].plot(hist_output, color='red')
axs[1].set_title('Histograma Expandido')

plt.tight_layout()
plt.show()

print('histograma mostrado')
