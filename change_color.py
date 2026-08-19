import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found. Check image.jpg location and name.")
    exit()

# Change to blue
blue_image = image.copy()
blue_image[:, :, 1] = 0
blue_image[:, :, 2] = 0

cv2.imshow("Original Image", image)
cv2.imshow("Blue Image", blue_image)

print("Press any key on the image window to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()