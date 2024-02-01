from typing import Tuple
import numpy as np
import cv2 as cv

from sobel import sobel

def sharpening(f: np.ndarray, t:int, k: float) -> Tuple[np.ndarray, np.ndarray]:

    g = sobel(f, t)

    row, col = f.shape

    output = np.zeros((row, col), dtype=f.dtype)

    for i in range(row):
        for j in range(col):
            output[i, j] = f[i, j] + g[i, j]

    return output, g

def sharpening_laplacian(f: np.ndarray, t:int, k: float) -> Tuple[np.ndarray, np.ndarray]:

    row, col = f.shape

    output = np.zeros((row, col), dtype=f.dtype)

    g = np.zeros((row, col), dtype=f.dtype)

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            g[i - 1, j - 1] = f[i + 1, j] + f[i - 1, j] + f[i, j + 1] + f[i, j - 1] - 4 * f[i, j]

    for i in range(row):
        for j in range(col):
            if g[i, j] <= t:
                g[i, j] = 0

    
    for i in range(row):
        for j in range(col):
            output[i, j] = f[i, j] + g[i, j]

    return output, g

img = cv.imread("./images/lua.jpg")
#output, g = sharpening_laplacian(cv.cvtColor(img, cv.COLOR_RGB2GRAY), 255, 1)
output, g = sharpening(cv.cvtColor(img, cv.COLOR_RGB2GRAY), 256, 1)

cv.imshow("output", output)
cv.imshow("image", img)
cv.imshow("kernel", g)
cv.waitKey(0)
cv.destroyAllWindows()
