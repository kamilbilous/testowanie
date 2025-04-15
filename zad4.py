import cv2

image = cv2.imread('letters.png', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed_rect = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_rect)
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
closed_ellipse = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel_ellipse)

cv2.imshow('Zamknięcie z elementem prostokątnym', closed_rect)
cv2.imshow('Zamknięcie z elementem eliptycznym', closed_ellipse)
cv2.waitKey(0)

