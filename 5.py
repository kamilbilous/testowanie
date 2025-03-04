import cv2

im1 = cv2.imread(r"C:\Users\Student\Desktop\testowanie\red_rose.jpg")
im2 = cv2.imread(r"C:\Users\Student\Desktop\testowanie\gray_rose.jpg")

cv2.imshow("imagine",im1)
cv2.imshow("image",im2)

while True:
    key = cv2.waitKey(0)
    if key == ord('1'):
        cv2.destroyWindow("imagine")
    elif key == ord('2'):
        cv2.destroyWindow("image")