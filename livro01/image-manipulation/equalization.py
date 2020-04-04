import cv2
from matplotlib import pyplot as grafico

#Equalizacao só pode em um canal, equalização em tons de cinza
def equalization_image_grey():
    image = cv2.imread("../imagens/low-contrast.png", cv2.IMREAD_GRAYSCALE)
    imageEqualizada = cv2.equalizeHist(image)

    cv2.imshow("Original", image)  # Imagem com pouca nitidez, muita nevoa
    cv2.imshow("Equalizada", imageEqualizada)  # imagem equalizada com maior nitidez
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    grafico.title("Histograma Original")
    grafico.hist(image.ravel(), 256, [0, 256])
    grafico.figure()
    grafico.title("Histograma Equalizada")
    grafico.hist(imageEqualizada.ravel(), 256, [0, 256])
    grafico.figure()
    grafico.show()

# equalization_image_grey()

#Equalização em RGB é diferente, necessita conversão em HSV e utiliza o canal Value
def equalization_image_rgb():
    image = cv2.imread("../imagens/low-contrast-rgb.jpg") #Imagem RGB

    imageHSV= cv2.cvtColor(image,cv2.COLOR_RGB2HSV) #Converto em HSV
    hue,saturation,value=cv2.split(imageHSV) #Divido os canais

    # o value controla as condições de luminosidade da imagem, por isso é utilizado
    canalValueEqualizado = cv2.equalizeHist(value)

    #junto novamente os canais para obter a imagem Equalizada
    imageHSV=cv2.merge((hue,saturation,canalValueEqualizado))

    #converto a imagem HSV para RGB
    imageEqualizada=cv2.cvtColor(imageHSV,cv2.COLOR_HSV2RGB)

    cv2.imshow("Original", image)  # Imagem com pouca nitidez, muita nevoa
    cv2.imshow("Equalizada", imageEqualizada)  # imagem equalizada com maior nitidez
    cv2.waitKey(0)
    cv2.destroyAllWindows()

equalization_image_rgb()



