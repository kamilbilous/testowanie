import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original",image)

kernelSizes = [(3, 3), (9, 9), (15, 15)]

for(kx,ky) in kernelSizes:
    blurred = cv2.blur(image,(kx,ky))
    cv2.imshow(f"Blur {kx} x {ky}",blurred)
    cv2.waitKey(500)
    # Mocno rozmywa krawedzie
    # Dobrze usuwa szum


for (kx, ky) in kernelSizes:
    blurred = cv2.GaussianBlur(image, (kx, ky), 0)
    cv2.imshow(f"Gaussian Blur ({kx}x{ky})", blurred)
    cv2.waitKey(500)
    #Lepsze zachowanie szczegółów niz blur()

for k in [3, 9, 15]:
    blurred = cv2.medianBlur(image, k)
    cv2.imshow(f"Median Blur ({k}x{k})", blurred)
    cv2.waitKey(500)
    #Bardzo rozmywa szczegóły
    #Dobra do redukcji szumu sól i pieprz

params = [(10, 20, 5), (11, 41, 21), (11, 61, 39)]
for (a, b, c) in params:
    blurred = cv2.bilateralFilter(image, a, b, c)
    cv2.imshow(f"Bilateral {a} x {b} x {c}", blurred)
    cv2.waitKey(500)
    #Słabo radzi sobie z efektem sol i pieprz
    #Słabe rozmycie

cv2.waitKey(0)