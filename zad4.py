import cv2
image = cv2.imread("lego.png")
cv2.imshow("Original",image)

kernelSizes = [(3, 3), (9, 9), (15, 15)]

for(kx,ky) in kernelSizes:
    blurred = cv2.blur(image,(kx,ky))
    cv2.imshow(f"Blur {kx} x {ky}",blurred)
    cv2.waitKey(500)

for (kx, ky) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kx, ky), 0)
    cv2.imshow(f"Gaussian Blur ({kx}x{ky})", blurred)
    cv2.waitKey(500)

for k in [3, 9, 15]:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Median Blur ({k}x{k})", blurred)
    cv2.waitKey(500)

params = [(10, 20, 5), (40, 100, 50), (30, 60, 90)]
for (a, b, c) in params:
    blurred = cv2.bilateralFilter(image, a, b, c)
    cv2.imshow(f"Bilateral {a} x {b} x {c}", blurred)
    cv2.waitKey(500)

cv2.waitKey(0)

#Rozmycie medianowe rozmywa do stanu niemożliwego do rozpoznania
#Metody gaussowska oraz dwustronna pozostawiaja czytelne logo
