import numpy as np

"""
filter.py
    functions common to all filter processing
""" 

def avg(img: np.ndarray) -> np.ndarray:
    """
    Apply the average filter in the input image
 
    Args:
      img: (array_like Shape (m,n)) input image 
    Returns
      output: (array_like Shape (m,n)) the image output of average filter process
                                  
    """

    row, col, cchannel = img.shape

    output = np.zeros((row, col, cchannel), dtype=np.float32)

    mask = np.ones((3, 3), dtype=np.float32) / 9

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            output[i - 1, j - 1] = (
                img[i - 1, j - 1] * mask[0, 0] + img[i - 1, j] * mask[0, 1] + img[i - 1, j + 1] * mask[0, 2] + 
                img[i, j - 1]     * mask[1, 0] + img[i, j]     * mask[1, 1] + img[i, j + 1]     * mask[1, 2] + 
                img[i + 1, j - 1] * mask[2, 0] + img[i + 1, j] * mask[2, 1] + img[i + 1, j + 1] * mask[2, 2]
            )

    return output.astype(img.dtype)

def _median(neighborhood: np.ndarray, i: int, j: int) -> np.float32:
    """
    Auxiliary function to apply the median operation with neighborhood algorithm
 
    Args:
      img: (array_like Shape (m,n)) input image 
      i:   (scalar) the row index
      j:   (scalar) the column index
    Returns
      output: (array_like Shape (m,n)) the image output of average filter process
                                  
    """

    temp = [
                neighborhood[i - 1, j - 1], neighborhood[i - 1, j], neighborhood[i - 1, j + 1], 
                neighborhood[i, j - 1],     neighborhood[i, j],     neighborhood[i, j + 1],
                neighborhood[i + 1, j - 1], neighborhood[i + 1, j], neighborhood[i + 1, j + 1]
            ]
        
    temp = np.sort(temp)

    l = len(temp)

    if l % 2 == 0: return (temp[(l // 2) - 1] + temp[l // 2]) / 2
    else:          return (temp[l // 2])


def median(img: np.ndarray) -> np.ndarray:
    """
    Apply the median filter in the input image
 
    Args:
      img: (array_like Shape (m,n)) input image 
    Returns
      output: (array_like Shape (m,n)) the image output of average filter process
                                  
    """

    row, col, cchannel = img.shape

    r, g, b = img[:, :, 0], img[:, :, 1], img[:, :, 2]

    output = np.zeros((row, col, cchannel), dtype=np.float32)

    output_r, output_g, output_b = np.zeros(r.shape, dtype=np.float32), np.zeros(g.shape, dtype=np.float32), np.zeros(b.shape, dtype=np.float32)

    for i in range(1, row - 1):
        for j in range(1, col - 1):
            output_r[i, j] = _median(r, i, j)
            output_g[i, j] = _median(g, i, j)
            output_b[i, j] = _median(b, i, j)
    
    output = np.dstack((output_r, output_g, output_b))

    return output.astype(img.dtype)