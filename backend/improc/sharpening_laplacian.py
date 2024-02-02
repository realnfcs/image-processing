from typing import Tuple
import numpy as np

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
