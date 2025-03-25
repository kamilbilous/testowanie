import imutils
import cv2
image = cv2.imread('image.jpg')
rotated = imutils.rotate(image, 180)
cv2.imshow("Obrot imutils", rotated)
cv2.waitKey(0)
