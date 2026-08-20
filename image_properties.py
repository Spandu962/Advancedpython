import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found")
    exit()

height, width, channels = image.shape

print("Image Properties")
print("----------------")
print("Width:", width)
print("Height:", height)
print("Channels:", channels)
print("Data Type:", image.dtype)
print("Total Pixels:", width * height)

cv2.imshow("Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()