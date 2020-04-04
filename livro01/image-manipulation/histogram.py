#Abrir imagem em tons de cinza
import cv2
imageGrey=cv2.imread("../imagens/frutas.png", cv2.IMREAD_GRAYSCALE)
imageColored=cv2.imread("../imagens/frutas.png")


#Gerar Histograma em tons de cinza

from matplotlib import pyplot as grafico


def histogram_grey(imageGrey):
    # ravel converte matriz em vetor unidimensional
    # 256 é a quantidade de valores distintos
    # [0,256] é o intervalo de valores do histograma
    grafico.hist(imageGrey.ravel(), 256, [0, 256])
    grafico.figure()
    grafico.show()


# histogram_grey()

#Histograma de imagem colorida
def histogram_rgb(imageColored):
    blue, green, red = cv2.split(imageColored) #BGR pq é o padrão do opencv

    # ravel converte matriz em vetor unidimensional
    # 256 é a quantidade de valores distintos
    # [0,256] é o intervalo de valores do histograma

    #Histograma do azul
    grafico.hist(blue.ravel(), 256, [0, 256], color='b')
    grafico.figure()

    # Histograma do verde
    grafico.hist(green.ravel(), 256, [0, 256], color='g')
    grafico.figure()


    # Histograma do vermelho
    grafico.hist(red.ravel(), 256, [0, 256], color='r')
    grafico.figure()
    grafico.show()

histogram_rgb(imageColored)

#calculo manual
def calc_histogram(image):

    histogram=[]

    for i in range(256):
        histogram.append(int(0))

    for linhas in range(len(image)):
        for colunas in range(len(image[0])):
            histogram[image[linhas,colunas]]+=1
    return histogram