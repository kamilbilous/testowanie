import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)
flipped_vertical = cv2.flip(image, 0)
flipped = cv2.flip(flipped_vertical, 1)
flipped_horizontal = cv2.flip(image,1)
cv2.imshow("Odwrocony", flipped_vertical)
cv2.imshow("Odwrocony2", flipped)
cv2.imshow("Odwrocony3", flipped_horizontal)
cv2.waitKey(0)