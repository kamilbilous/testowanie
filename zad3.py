import cv2
image = cv2.imread("image.jpg")
cv2.imshow("Original",image)

params = [(20, 40, 60), (10, 20, 30), (15, 45, 80),(30,60,90)]
for (a, b, c) in params:
    blurred = cv2.bilateralFilter(image, a, b, c)
    cv2.imshow(f"Bilateral {a} x {b} x {c}", blurred)
    cv2.waitKey(500)
cv2.waitKey(0)

#Bardzo dobrze redukuje szum
#Lepiej zachowuje krawędzie
#30x60x90 dają najlepszy wynik
