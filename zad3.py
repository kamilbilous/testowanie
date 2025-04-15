import cv2
import numpy as np

image = cv2.imread("image3.jfif")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
kernel_sizes = [2, 3, 4]
opened_images = []

for size in kernel_sizes:
    kernel = np.ones((size, size), np.uint8)

    opened = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    opened_images.append(opened)

cv2.imshow("Obraz z szumem", image)

for i, opened in enumerate(opened_images):
    cv2.imshow(f"Otwarcie {kernel_sizes[i]}x{kernel_sizes[i]}", opened)


cv2.waitKey(0)

#skutecznosc słaba