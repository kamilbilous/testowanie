import cv2

image = cv2.imread("image.jpg")

flip_type = int(input("Enter flip type (0,1,-1)): "))
flipped_user_choice = cv2.flip(image, flip_type)
cv2.imshow(f"Flip user choice ({flip_type})", flipped_user_choice)
cv2.waitKey(0)