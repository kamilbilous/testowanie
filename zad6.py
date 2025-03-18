import cv2

image = cv2.imread("jp2.jpeg")

eye1, eye2 = (330,290),(450,310)
mouth = (380,440)
face_center = (390,280)

eye_radius = 50
mouth_width = 130
mouth_height = 50
face_radius = 240
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)

cv2.circle(image, eye1, eye_radius, red, -1)
cv2.circle(image, eye2, eye_radius, red, -1)

cv2.rectangle(image,(mouth[0] - mouth_width // 2, mouth[1] - mouth_height // 2),(mouth[0] + mouth_width // 2, mouth[1] + mouth_height // 2),green,-1)

cv2.circle(image,face_center,face_radius,blue,3)

cv2.imshow("Zamazany obraz", image)
cv2.waitKey(0)
cv2.destroyAllWindows()