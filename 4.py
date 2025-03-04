import cv2

img_grey = cv2.imread(r"C:\Users\Student\Desktop\testowanie\red_rose.jpg",cv2.IMREAD_GRAYSCALE)
path = r"C:\Users\Student\Desktop\testowanie\gray_rose.jpg"
cv2.imwrite(path, img_grey)
print(f"Obraz zapisany w  {path}")