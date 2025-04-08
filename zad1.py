import cv2
import numpy as np

image = cv2.imread("cl.jpg")

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (570, 250), 225, 255, -1)
masked = cv2.bitwise_or(image, image, mask=mask)

cv2.imshow("masekd",masked)
cv2.waitKey(0)
