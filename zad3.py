import cv2
import numpy as np

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

h, w = image.shape[:2]

M = np.float32([[1, 0, w//2 + 50], [0, 1, h//2 + 50]])
shifted = cv2.warpAffine(image, M, (w, h))

cv2.imshow("Przesuniete", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
