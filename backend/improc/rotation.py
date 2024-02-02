import numpy as np

def rotation(f:np.ndarray, angle:int):

    """
    Apply the rotation in the image and returns the result
 
    Args:
      f : (array_like Shape (m,n)) first image 
      angle: (integer number) the parameter that defines the angulation of the rotation
    Returns

      output: (array_like Shape (m,n)) the output image of rotation process
      
    """

    row = f.shape[0]
    col = f.shape[1]

    ic = row / 2
    jc = col / 2

    output:np.ndarray = np.zeros((row,col), dtype=f.dtype)


    angle_r = np.radians(angle)

    for i in range(row):
        for j in range(col):
            
            il = int(np.round((i - ic) * np.cos(angle_r)) - ((j - jc) * np.sin(angle_r)) + ic)
            jl = int(np.round((i - ic) * np.sin(angle_r)) + ((j - jc) * np.cos(angle_r)) + jc)

            if (il <= row-1 and il > 0) and (jl <= col-1 and jl > 0):
                output[il,jl] = f[i,j]
        
    output = np.uint8(output)
    return output

