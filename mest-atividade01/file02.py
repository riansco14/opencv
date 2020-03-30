import cv2
import numpy as np
import scipy.ndimage as ndimage

image = cv2.imread("images/gradient.jpg", cv2.IMREAD_GRAYSCALE)
print(image.shape)
# imageEdge = cv2.Sobel(image, cv2.CV_8U, 1, 0) bordas horizontais
# imageEdge = cv2.Sobel(image, cv2.CV_8U, 0, 1) #bordas verticais

# imageEdgeBlur = cv2.blur(imageEdge, ksize=(2, 2))



smallest = np.amin(image)
biggest = np.amax(image)

imageEdgeCalculationHorizontal = np.zeros(image.shape)
rowsLen=len(imageEdgeCalculationHorizontal)
columnsLen=len(imageEdgeCalculationHorizontal[0])
for row in range(rowsLen):
    for column in range(columnsLen):
        pass
        a=0
        if(not (row+1>=rowsLen)):
            a = image[row + 1, column]
        else:
            continue
        aMinus=0
        if(not(row-1<0)):
            aMinus=image[row-1, column]
        else:
            continue
        imageEdgeCalculationHorizontal[row,column]=a-aMinus
        imageEdgeCalculationHorizontal[row,column]=(((imageEdgeCalculationHorizontal[row,column]-smallest)/(biggest-smallest))*255)


for row in range(rowsLen):
    for column in range(columnsLen):
        pass
cv2.imshow("Original", image)
# cv2.imshow("Sobel", imageEdge)
# cv2.imshow("Sobel Blur", imageEdgeBlur)
cv2.imshow("Gradient Manual", ndimage.convolve(image,[[0,1,0],[0,-1,0],[0,0,0]]))
cv2.imshow("Gradient Manual 2 ", imageEdgeCalculationHorizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
