import cv2

image = cv2.imread("image.jpg")
height, width = image.shape[:2]
roi_width = 250
roi_height = 250
for x in range(0, width - roi_width, 10):
    roi_move = image[0:roi_height, x:x+roi_width]
    cv2.imshow("Moving ROI", roi_move)
    cv2.waitKey(0)