import cv2
import numpy as np
imageGrey = cv2.imread("images/u2dark.png", cv2.IMREAD_GRAYSCALE)


# question 1.(a)
smallest = np.amin(imageGrey)
# smallest=imageGrey.min(axis=0).min(axis=0)
# se tirar um min(axis=0) lista todos menores por linha .min(axis=0)
biggest = np.amax(imageGrey)
# biggest = imageGrey.max(axis=0).max(axis=0)
average = np.mean(imageGrey)
# average = imageGrey.mean(axis=0).mean(axis=0)

print(smallest,biggest,average)
print(imageGrey.shape)

#question 1.(b)
imageGreyResult = np.copy(imageGrey)
for row in range(len(imageGreyResult)):
    for column in range(len(imageGreyResult[0])):
        if(imageGreyResult[row, column]==smallest):
            imageGreyResult[row, column]=0
        if(imageGreyResult[row, column]==biggest):
            imageGreyResult[row, column]=255

#question 1.(c)
imageGreyResult2=np.copy(imageGreyResult)
for row in range(len(imageGreyResult)):
    for column in range(len(imageGreyResult[0])):
        imageGreyResult2[row,column]=np.uint8((2*(imageGreyResult2[row,column]-128)+128))


cv2.imshow("Original", imageGrey)
cv2.imshow("Result", imageGreyResult)
cv2.imshow("ResultContrast", imageGreyResult2)
cv2.waitKey(0)
cv2.destroyAllWindows()
