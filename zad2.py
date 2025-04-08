import cv2
import numpy as np

image = cv2.imread("cl.jpg")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (480, 250), (700, 300), 255, -1)
inverse_mask = cv2.bitwise_not(mask)
masked = cv2.bitwise_and(image, image, mask=inverse_mask)

cv2.imshow("Masked Image", masked)
cv2.waitKey(0)
