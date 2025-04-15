import cv2

image = cv2.imread('letters.png', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

erosion = cv2.erode(binary, kernel, iterations=1)
dilation = cv2.dilate(binary, kernel, iterations=1)


opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('Erozja', erosion)
cv2.imshow('Dylatacja', dilation)
cv2.imshow('Otwarcie', opening)
cv2.imshow('Zamknięcie', closing)
cv2.imshow('Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
