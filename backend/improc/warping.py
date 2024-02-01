import numpy as np


def warping(img:np.ndarray,xp:int ,yp:int, xq:int, yq:int, xpl:int, ypl:int, xql:int, yql:int) -> np.ndarray:
    """
    Apply the warping in the image and returns the result
 
    Args:
      img : (array_like Shape (m,n)) first image 

      First vector:
        xp: (integer number) the first cordinate(first point)
        yp: (integer number) the second cordinate(first point)
        xq: (integer number) the first cordinate(second point)
        yq: (integer number) the second cordinate(second point)
    
     Second vector:
        xpl: (integer number) the first cordinate(first point)
        ypl: (integer number) the second cordinate(first point)
        xql: (integer number) the first cordinate(second point)
        yql: (integer number) the second cordinate(second point)
           
    Returns
    
      output: (array_like Shape (m,n)) the output image of warping process
      
    """

    row,col,ch = img.shape

    output:np.ndarray = np.zeros((row,col,ch), dtype=img.dtype)

    for i in range(row):
        for j in range(col):
            
            u = calculate_u(i,j,xp,yp,xq,yq)
            v = calculate_v(i,j,xp,yp,xq,yq)


            Xl = []

            
            Xl = np.array([xpl, ypl]) + u * np.array([xql - xpl, yql - ypl]) + v * np.array([yql - ypl, xpl - xql]) / np.sqrt((xql - xpl) ** 2 + (yql - ypl) ** 2)

            Xl = np.round(Xl)

            if (Xl[0] > 0 and Xl[0] < row) and (Xl[1] > 0 and Xl[1] < 512):
                output[i,j] = img[int(Xl[0]),int(Xl[1])]
    
    return output
           



def calculate_u(x:int ,y:int ,xp:int ,yp:int ,xq:int ,yq:int) -> float:


    u = ( ((x - xp) * (xq - xp)) + ((y - yp) * (yq - yp)) ) /( ((xq - xp)** 2) + ((yq - yp)**2) )

    return u

def calculate_v(x:int ,y:int ,xp:int ,yp:int ,xq:int ,yq:int) -> float:

    v = ( ((x - xp) * (yq - yp)) + ((y - yp) * (xp - xq)) ) / ((((xq - xp) ** 2) + ((yq - yp) ** 2)) ** 0.5)

    return v



    