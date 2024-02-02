import numpy as np

def zoom_out(imagem, escala):
    altura, largura = imagem.shape[:2]

    # Novas dimensões após o zoom out
    nova_altura = int(altura * escala)
    nova_largura = int(largura * escala)

    # Criar uma nova imagem com as dimensões reduzidas
    nova_imagem = np.zeros((nova_altura, nova_largura), dtype=np.uint8)

    # Aplicar zoom out usando média
    for i in range(nova_altura):
        for j in range(nova_largura):
            origem_i = int(i / escala)
            origem_j = int(j / escala)
            nova_imagem[i, j] = np.mean(imagem[origem_i:origem_i+2, origem_j:origem_j+2], axis=(0, 1))

    return nova_imagem

def shear(img: np.ndarray, s: float) -> np.ndarray:

    row, col = img.shape

    nimg = zoom_out(img, 0.5) 

    r, c = nimg.shape
    output = np.zeros((r, c), dtype=img.dtype)

    for i in range(r):
        for j in range(c):

            iline = round(i + s * j)
            output[min(iline, r - 1), j] = nimg[i, j]

    return output