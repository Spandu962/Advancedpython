import cv2

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found")
    exit()

# Resize
resized = cv2.resize(image, (500, 400))

# Rotate 90 degrees
rotated = cv2.rotate(
    image,
    cv2.ROTATE_90_CLOCKWISE
)

cv2.imshow("Original", image)
cv2.imshow("Resized", resized)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()