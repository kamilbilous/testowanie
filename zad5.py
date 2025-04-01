import cv2

image = cv2.imread("image.jpg")
height, width, _ = image.shape
center_image = image[height//4:3*height//4, width//4:3*width//4]
flipped_center = cv2.flip(center_image, -1)
image[height//4:3*height//4, width//4:3*width//4] = flipped_center
cv2.imshow("Flip Center", image)
cv2.waitKey(0)