import cv2

image = cv2.imread("image.jpg")
cropped_image = image[0:300, 200:500]
cv2.imwrite("cropped_image.jpg", cropped_image)
cv2.imshow("Crop",cropped_image)
cv2.waitKey(0)
