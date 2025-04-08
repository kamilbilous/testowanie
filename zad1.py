import numpy as np
import cv2

triangle = np.zeros((300, 300), dtype="uint8")
pts = np.array([[0, 300], [300, 300], [150, 0]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.fillPoly(triangle, [pts], 255)
cv2.imshow("Triangle",triangle)


circle = np.zeros((300, 300), dtype = "uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

and_result = cv2.bitwise_and(triangle, circle)
or_result = cv2.bitwise_or(triangle, circle)
xor_result = cv2.bitwise_xor(triangle, circle)
not_triangle = cv2.bitwise_not(triangle)
not_circle = cv2.bitwise_not(circle)

cv2.imshow('Trójkąt', triangle)
cv2.imshow('Okrąg', circle)
cv2.imshow('AND', and_result)
cv2.imshow('OR', or_result)
cv2.imshow('XOR', xor_result)
cv2.imshow('NOT Trójkąt', not_triangle)
cv2.imshow('NOT Okrąg', not_circle)

cv2.waitKey(0)