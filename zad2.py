import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original",image)

kernelSizes = [(3, 3),(5,5), (9, 9), (15, 15)]

for(kx,ky) in kernelSizes:
    blurred = cv2.blur(image,(kx,ky))
    cv2.imshow(f"Blur {kx} x {ky}",blurred)
    cv2.waitKey(500)



for (kx, ky) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kx, ky), 0)
    cv2.imshow(f"Gaussian Blur ({kx}x{ky})", blurred)
    cv2.waitKey(500)


for k in [3,5, 9, 15]:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Median Blur ({k}x{k})", blurred)
    cv2.waitKey(500)

params = [(3, 3, 3), (5, 5, 5), (9, 9, 9),(15,15,15)]
for (a, b, c) in params:
    blurred = cv2.bilateralFilter(image, a, b, c)
    cv2.imshow(f"Bilateral {a} x {b} x {c}", blurred)
    cv2.waitKey(500)


cv2.waitKey(0)

#Im większe kernel tym mocniejsze rozmycie
#Optymalny 5x5 lub 9x9