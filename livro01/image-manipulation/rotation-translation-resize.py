import cv2

image = cv2.imread("../imagens/frutas.png")

def rotation(image):
    # operacao de rotação
    linhas, colunas, _ = image.shape
    # matriz de rotacao
    # 1 parametro: centro da imagem  através das colunas e linhas (inverteu)
    # 2 parametro: angulo
    # 3 parametro: escala (tamanho)
    matriz = cv2.getRotationMatrix2D((colunas / 2, linhas / 2), 90, 1)
    # gerar a imagem rotacionada com Warpaffine
    # 1- imagem 2-matriz de rotação 3-tamanho da imagem
    # colunas e linhas (inverteu)
    imagemRotacionada = cv2.warpAffine(image, matriz, (colunas, linhas))
    cv2.imshow("Rotacionada", imagemRotacionada)
    # cv2.imshow("Original", image)
    print(imagemRotacionada.shape, image.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# rotation(image)

#Movimentar a imagem
def translation(image):
    import numpy as np
    # operacao de translação(Mover a imagem no canvas)
    linhas, colunas = image.shape[:2]
    # matriz de rotacao
    # rotacao na horizontal  eixo x/colunas [1,0] 50 pixels -> [0,1, 200]
    # rotacao na vertical  eixo y/linhas [0,1] 50 pixels -> [0,1, 50]
    matriz = np.float32([[1, 0, 200], [0, 1, 50]])
    # gerar a imagem rotacionada com Warpaffine
    # 1- imagem 2-matriz de movimentação 3-tamanho da imagem
    # colunas e linhas (inverteu)
    imagemRotacionada = cv2.warpAffine(image, matriz, (colunas, linhas))
    cv2.imshow("Rotacionada", imagemRotacionada)
    # cv2.imshow("Original", image)
    print(imagemRotacionada.shape, image.shape)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

translation()


def resize(image):
    # mudando o tamanho - resize
    # 1 - imagem original
    # 2 - imagem destino
    # 3 - tamanho fx   0.5 -> metade  1 -> tamanho original   2->dobro ...
    # 3 - tamanho fy   0.5 -> metade  1 -> tamanho original   2->dobro ...
    # 4 - interpolation (algoritmo utilizado na mudança de tamanho)
    imageResized = cv2.resize(image, None, 1, 0.25, cv2.INTER_LINEAR)
    print(imageResized.shape)
    cv2.imshow("Imagem Alterada", imageResized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# resize(image)