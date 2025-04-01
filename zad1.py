import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
flipped_horizontal = cv2.flip(image, 1)
cv2.imshow("Odwrocony", flipped_horizontal)
cv2.waitKey(0)