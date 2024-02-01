import numpy as np


def zoom_out(img:np.ndarray, factor:float)->np.ndarray:

    """
    Zoom out on the image and returns the results
 
    Args:
      img : (array_like Shape (m,n)) first image 
      factor: (integer number) the ampliation factor
           
    Returns
    
      output: (array_like Shape (m,n)) the output image of zoom out process
      
    """
     
    row,col,ch = img.shape
    
    new_row = int(row / factor)
    new_col = int(col / factor)


    output:np.ndarray = np.zeros((new_row,new_col,ch), dtype=img.dtype)
    
    for i in range(new_row):
        for j in range(new_col):

            origin_row = int(i * factor)
            origin_col = int(j * factor)

            origin_row = min(origin_row, row -1)
            origin_col = min(origin_col, col - 1)


            
            output[i,j,:] = img[origin_row,origin_col,:]

    
    return output 

