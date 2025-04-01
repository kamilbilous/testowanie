import cv2

image = cv2.imread("image.jpg")
startX = int(input("Enter startX: "))
endX = int(input("Enter endX: "))
startY = int(input("Enter startY: "))
endY = int(input("Enter endY: "))
roi_dynamic = image[startY:endY, startX:endX]
cv2.imshow("Original",image)
cv2.imshow("Dynamic ROI", roi_dynamic)
cv2.waitKey(0)
