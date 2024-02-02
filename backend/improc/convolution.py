import numpy as np

def convolution(image: np.ndarray, kernel: np.ndarray):

    row, col = image.shape
    krow, kcol = kernel.shape

    output: np.ndarray = np.zeros((row - krow + 1, col - kcol + 1), dtype=image.dtype)

    for i in range(output.shape[0]):
        for j in range(output.shape[1]):
            output[i, j] = np.sum(image[i:i + krow, j:j + kcol] * kernel)

    return output
