import cv2

image = cv2.imread("image.jpg")
startX = 230
endX = 450
startY = 75
endY = 300
roi_dynamic = image[startY:endY, startX:endX]
cv2.imshow("Face",roi_dynamic)
cv2.waitKey(0)

