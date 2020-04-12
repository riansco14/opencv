import cv2
import numpy as np
imagem=cv2.imread("card.jpg")


rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, ( 5,13))
squareKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
regions = []

# Converte a imagem em escala de cinza e aplica a operação blackhat
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)

# Encontra regiões na imagem que sejam leves
light = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, squareKernel)
light = cv2.threshold(light, 80, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("Imagem Light 1", light)

# Calcula a representação de gradiente de Scharr da imagem do blackhat na direção x e dimensiona a imagem resultante na faixa [0, 255]
gradX=cv2.Laplacian(blackhat,cv2.CV_8U)
# gradX = cv2.Sobel(blackhat, ddepth=cv2.CV_32F , dx=1, dy=0, ksize=-1)
# gradX = np.absolute(gradX)
# (minVal, maxVal) = (np.min(gradX), np.max(gradX))
# gradX = (255 * ((gradX - minVal) / (maxVal - minVal))).astype("uint8")
cv2.imshow("Imagem Laplace", gradX)

# Blur da representação do gradiente, aplica uma operação de fechamento e threshold a imagem usando o método de Otsu
gradX = cv2.GaussianBlur(gradX, (5, 5), 0)
gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv2.imshow("Imagem Limiar 1", thresh)

# Realiza uma série de erosões e dilatações na imagem
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)
cv2.imshow("Imagem Erosao 1", thresh)

# Obtém o bitwise 'e' entre as regiões 'light' da imagem, então executa outra série de erosões e dilatação
thresh = cv2.bitwise_and(thresh, thresh, mask=light)
thresh = cv2.dilate(thresh, None, iterations=2)
thresh = cv2.erode(thresh, None, iterations=1)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)),iterations=4)

cv2.findContours(thresh,cv2.INTER_LINEAR)

cv2.imshow("ImagemErosao 2", thresh)
cv2.imshow("Imagem", gray)


cv2.waitKey(0)
cv2.destroyAllWindows()