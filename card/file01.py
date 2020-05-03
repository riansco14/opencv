import cv2

imagem=cv2.imread("card4.jpg")

imagemCinza=cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
ret,imagemBinaria=cv2.threshold(imagemCinza, 135,255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel=cv2.getStructuringElement(cv2.MORPH_RECT, (6,6))
# imagemBinaria=cv2.erode(imagemBinaria, kernel,iterations=3)
# imagemBinaria=cv2.dilate(imagemBinaria, kernel,iterations=5)


imagemHSV=cv2.cvtColor(imagem,cv2.COLOR_RGB2HSV)
hue,sat,value=cv2.split(imagemHSV)
# cv2.imshow("Original 1",hue)
# cv2.imshow("Original 2",sat)
# cv2.imshow("Original 3",value)

ret,imagemBinaria= cv2.threshold(imagemCinza, 120,200,cv2.THRESH_BINARY)
imagemBinaria = cv2.morphologyEx(imagemBinaria, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2)),iterations=1)
cv2.imshow("Original 2",imagemBinaria)
imagemBinaria = cv2.erode(imagemBinaria, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)),iterations=1)
imagemBinaria = cv2.dilate(imagemBinaria, cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3)),iterations=1)

# imagemBinaria = cv2.morphologyEx(imagemBinaria, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)),iterations=4)

contornos, hierarquia = cv2.findContours (imagemBinaria, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
# print(len(contornos))
cv2.drawContours(imagem, contornos, -1, (0,255,0), 3)

# contornos = sorted(contornos, key=cv2.contourArea, reverse=True)

contornos_poly = [None] * len(contornos)
boundRect = [None] * len(contornos)
centers = [None] * len(contornos)
radius = [None] * len(contornos)
cropedImages=list()
for i, c in enumerate(contornos):
    area = cv2.contourArea(c)
    perimetro=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c, perimetro*0.1,True)
    # if area >100000.0:
    if len(approx)==4 and area >100000.0:
        x,y,w,h = cv2.boundingRect(approx)
        # print(int(boundRect[i][0]), int(boundRect[i][1]),int( boundRect[i][2]), int( boundRect[i][3]))
        cv2.rectangle(imagem, (int(x), int(y)), \
                      (int(x+w), int(y+h)), (255,0,0), 2)
        cropedImages.append(imagem[y:y+h,x:x+w])

for indexCrop in range(len(cropedImages)):
    cv2.imshow(str(indexCrop),cropedImages[indexCrop])
# imagemBinaria=cv2.erode(imagemBinaria,None, iterations=1)
# imagemBinaria=cv2.dilate(imagemBinaria,None, iterations=2)
# cv2.imshow("Original",imagemCinza)
cv2.imshow("Original",imagem)
cv2.imshow("Original 3",imagemBinaria)

cv2.waitKey(0)
cv2.destroyAllWindows()