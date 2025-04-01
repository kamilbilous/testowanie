import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

width = image.shape[1]
right_half = image[:, width//2:]
cv2.imshow("Right Half", right_half)
cv2.waitKey(0)