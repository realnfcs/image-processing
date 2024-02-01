import numpy as np


def sobel_gradient(f:np.ndarray, t:int) -> np.ndarray:

    """
    Implements the sobel gradient and returns the result
 
    Args:
      f : (array_like Shape (m,n)) first image 
      t: (integer number) the parameter that defines the threshold
    Returns

      output: (array_like Shape (m,n)) the output image of rotation process
      
    """

    f = f.astype(np.float64)
    row,col = f.shape

    mx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    my = [[-1,-2,-1],[-0,0,0],[1,2,1]]

    print(mx)
    print(my)

    output:np.ndarray = np.zeros((row,col), dtype=f.dtype)

    for i in range(1,row-2):
        for j in range(1,col-2):
            

            gx = np.sum(np.sum(mx * f[i-1:i+2, j-1:j+2]))
            gy = np.sum(np.sum(my * f[i-1:i+2, j-1:j+2]))

            output[i+1,j+1] = np.sqrt(np.power(gx,2) + np.power(gy,2))

            if np.max(output[i,j]) < t:
                output[i,j] = 0
            
            else:
                output[i,j] = 255
            

    #output = np.uint8(output)

    return output


