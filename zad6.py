import cv2

image = cv2.imread('image5.jpg', cv2.IMREAD_GRAYSCALE)
_, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

opening = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Otwarcie - Tablica', opening)
cv2.imshow('Zamknięcie - Tablica', closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
