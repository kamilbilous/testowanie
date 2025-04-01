import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
flipped_vertical = cv2.flip(image, 0)
cv2.imshow("Odwrocony", flipped_vertical)
cv2.waitKey(0)