import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
flipped_vertical = cv2.flip(image, 0)
flipped = cv2.flip(flipped_vertical, 1)

cv2.imshow("Odwrocony", flipped)
cv2.waitKey(0)