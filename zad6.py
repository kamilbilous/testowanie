import cv2
import numpy as np

image = cv2.imread("sunflower.jpg")
cv2.imshow("og",image)
mask = np.zeros(image.shape[:2],dtype=np.uint8)
blurred_background = cv2.GaussianBlur(image, (21, 21), 0)

height, width = mask.shape

cv2.circle(mask,((width//2) + 100,height//2 +60),120,255,-1)
masked = cv2.bitwise_and(image, image, mask=mask)
inverse_mask = cv2.bitwise_not(mask)
background = cv2.bitwise_and(blurred_background,blurred_background,mask=inverse_mask)
res = cv2.add(masked,background)
cv2.imshow("result", res)
cv2.waitKey(0)