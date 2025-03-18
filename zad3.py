import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

blue = (255,0,0)
red = (0,0,255)

cv2.circle(canvas,(50,50),40,blue,3)
cv2.circle(canvas,(150,150),60,red,3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)