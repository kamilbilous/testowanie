import cv2
import numpy as np


image = cv2.imread("image.png")

noise = np.zeros(image.shape, np.uint8)

cv2.randn(noise, 0, 200)

noisy_image = cv2.add(image, noise)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

for(kx,ky) in kernelSizes:
    blurred = cv2.blur(noisy_image,(kx,ky))
    cv2.imshow(f"Blur {kx} x {ky}",blurred)
    cv2.waitKey(500)

for (kx, ky) in kernelSizes:
    blurred = cv2.GaussianBlur(noisy_image, (kx, ky), 0)
    cv2.imshow(f"Gaussian Blur ({kx}x{ky})", blurred)
    cv2.waitKey(500)

for k in [3, 9, 15]:
    blurred = cv2.medianBlur(noisy_image, k)
    cv2.imshow(f"Median Blur ({k}x{k})", blurred)
    cv2.waitKey(500)

params = [(10, 20, 5), (40, 100, 50), (30, 60, 90)]
for (a, b, c) in params:
    blurred = cv2.bilateralFilter(noisy_image, a, b, c)
    cv2.imshow(f"Bilateral {a} x {b} x {c}", blurred)
    cv2.waitKey(500)

cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Rozmycie dwustronne rozmywa zbyt mocno
# Najlepiej rozmycie medianowe
