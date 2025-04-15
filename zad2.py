import cv2
import numpy as np

image= cv2.imread("image2.jpg")
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernel_sizes = [(3, 3), (5, 5), (7, 7)]
iterations = [1, 2, 3]

results = []

for k in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k)
    for it in iterations:
        dilated = cv2.dilate(binary, kernel, iterations=it)
        thickness = 988- (np.count_nonzero(dilated, axis=0).mean())
        results.append((k, it, thickness))

        window_name = f"Dylatacja - Kernel: {k}, Iteracje: {it}"
        cv2.imshow(window_name, dilated)
        cv2.waitKey(500)

print(f"{'Kernel':>10} | {'Iteracje':>9} | {'Grubość':>18}")
for r in results:
    print(f"{str(r[0]):>10} | {r[1]:>9} | {r[2]:>18.2f}")

