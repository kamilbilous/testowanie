import cv2
import imutils

image = cv2.imread('image.jpg')

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
im2 = imutils.rotate(image,90)

for i in range(3):
    M = cv2.getRotationMatrix2D((cX, cY), 30 , 1.0)
    image = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Obrot o 90 stopni",im2)
cv2.imshow("Obrot sekwencyjny", image)
cv2.waitKey(0)

#Obrot taki sam, ale obraz przyciety dziwinie przez wiele obrotow