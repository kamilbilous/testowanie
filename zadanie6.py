import imutils
import cv2
image = cv2.imread('image.jpg')
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Obrot imutils", rotated)
cv2.waitKey(0)
