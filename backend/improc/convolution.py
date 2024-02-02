import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def convolution(image: np.ndarray, kernel: np.ndarray):

    row, col = image.shape
    krow, kcol = kernel.shape

    output: np.ndarray = np.zeros((row - krow + 1, col - kcol + 1), dtype=image.dtype)

    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i, j] = np.sum(image[i:i + krow, j:j + kcol] * kernel)

    return output

image = cv.imread("./images/lena_gray_256.tif")
kernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

output = convolution(cv.cvtColor(image, cv.COLOR_RGB2GRAY), kernel)

plt.imshow(output)
plt.axis('off')
plt.show()
