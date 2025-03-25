import imutils
import cv2

image = cv2.imread('image.jpg')

for i in range(0,361,15):
    rotated = imutils.rotate(image,i)
    cv2.imshow("Obrot",rotated)
    cv2.waitKey(500)
cv2.waitKey(0)


