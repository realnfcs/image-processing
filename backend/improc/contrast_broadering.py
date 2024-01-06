import numpy as np
import cv2 as cv

def contrast_broadering(i:np.ndarray, smin:int, smax:int) -> np.ndarray:
    """
    Applies contrast broadening to the input image and returns it with the changes
 
    Args:
      i : (array_like Shape (m,n)) first image 
      smin: (integer number[0, 255]) new minim intensity level 
      smax: (integer number[0, 255]) new maximum intensity level     
    Returns
      output: (array_like Shape (m,n)) the output image of contrast broadering process
                                  
    """
       
    rmin = np.min(i)
    rmax = np.max(i)
    print(rmin)
    print(rmax)


    r = i.astype(np.float64)

    output:np.ndarray

    output = ((smax - smin) / (rmax - rmin)) * (r - rmin) + smin
    output = np.uint8(output)

    return output



