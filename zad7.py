import cv2

image = cv2.imread("image.jpg")
height, width = image.shape[:2]
grid_size = 3
grid_height = height // grid_size
grid_width = width // grid_size

for i in range(grid_size):
    for j in range(grid_size):
        grid_piece = image[i*grid_height:(i+1)*grid_height, j*grid_width:(j+1)*grid_width]
        cv2.imshow(f"Grid {i+1}-{j+1}", grid_piece)
        cv2.waitKey(500)
cv2.waitKey(0)