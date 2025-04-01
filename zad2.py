import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

height = image.shape[0]
bottom_half = image[height//2:, :]
cv2.imshow("Bottom Half", bottom_half)
cv2.waitKey(0)