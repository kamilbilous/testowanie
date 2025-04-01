import cv2

image = cv2.imread("image.jpg")

crop = image[50:150, 50:150]
image[200:300, 200:300] = crop
cv2.imshow("Crop", image)
cv2.waitKey(0)