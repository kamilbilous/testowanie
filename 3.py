import cv2

img_grey = cv2.imread(r"C:\Users\Student\Desktop\testowanie\rose.jpg",cv2.IMREAD_GRAYSCALE)
if img_grey.ndim == 2:
    print(1)
else:
    print(img_grey.shape[:3])