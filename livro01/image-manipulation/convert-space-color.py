import cv2

image=cv2.imread("../imagens/frutas.png")
imageGray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

imageHSV=cv2.cvtColor(image,cv2.COLOR_RGB2HSV)

cv2.imshow("Original",image)
cv2.imshow("Gray",imageGray)
cv2.imshow("Original",imageHSV)

cv2.waitKey(0)
cv2.destroyAllWindows()

