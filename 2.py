import cv2

image = cv2.imread(r"C:\Users\Student\Desktop\testowanie\red_rose.jpg")
(h,w,c) = image.shape[:3]
print(f'channels {c}')

