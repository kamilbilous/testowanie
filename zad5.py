import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

centerX, centerY = canvas.shape[1] // 2, canvas.shape[0] // 2
white = (255, 255, 255)

for size in range(20, 240, 20):
    cv2.rectangle(canvas, (centerX - size // 2, centerY - size // 2),(centerX + size // 2, centerY + size // 2), white, 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

