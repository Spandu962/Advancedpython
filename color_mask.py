import cv2
import numpy as np

image = cv2.imread("image.jpg")

if image is None:
    print("Image not found")
    exit()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_blue = np.array([100, 100, 50])
upper_blue = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("Color Mask", mask)
cv2.imshow("Detected Color", result)

cv2.waitKey(0)
cv2.destroyAllWindows()