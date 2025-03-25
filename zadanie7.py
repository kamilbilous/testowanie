import cv2
import imutils

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated_warpAffine = cv2.warpAffine(image, M, (w, h))

rotated_imutils = imutils.rotate(image, 60)

cv2.imshow("Obrot warpAffine", rotated_warpAffine)
cv2.imshow("Obrot imutils", rotated_imutils)
cv2.waitKey(0)
