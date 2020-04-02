import cv2
import numpy as np

image = cv2.imread("../imagens/frutas.png")

image=cv2.cvtColor(image,cv2.COLOR_RGB2HSV) #Converto para HSV
hue,saturation,value=cv2.split(image) #dividir canais hsv

cv2.imshow("Hue", hue)
cv2.imshow("Saturation",saturation)
cv2.imshow("Value",value)


image_hsv=cv2.merge((hue,saturation,value)) #mesclo os canais novamente para ter a imagem original
image_original=cv2.cvtColor(image_hsv,cv2.COLOR_HSV2RGB) #converto os espaço de core, o monitor exibe em rgb, logo teria falhas
cv2.imshow("Original", image_original)

cv2.waitKey(0)
cv2.destroyAllWindows()