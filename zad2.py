import numpy as np
import cv2

triangle = np.zeros((300, 300), dtype="uint8")
pts = np.array([[0, 300], [300, 300], [150, 0]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle, [pts], 255)
cv2.imshow("Triangle",triangle)

triangle2 = np.zeros((300, 300), dtype="uint8")
pts = np.array([[20, 280], [280, 280], [150, 20]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle2, [pts], 255)
cv2.imshow("Triangle2",triangle2)
diff_image = cv2.bitwise_xor(triangle, triangle2)
cv2.imshow('Różnice między obrazami', diff_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
