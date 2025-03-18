import cv2
import numpy as np

image = cv2.imread("image.jpg")

tx = int(input("Przesuniecie os x: "))
ty = int(input("Przesuniecie os Y: "))

M = np.float32([[1, 0, tx], [0, 1, ty]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imshow("Original", image)
cv2.imshow(f"Shifted by ({tx}, {ty})", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()

