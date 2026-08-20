import cv2
import numpy as np

height = 400
width = 600

image = np.zeros((height, width, 3), dtype=np.uint8)

stripe_width = width // 6

colors = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255)
]

for i, color in enumerate(colors):
    start = i * stripe_width
    end = (i + 1) * stripe_width

    image[:, start:end] = color

cv2.imshow("Color Stripes", image)

cv2.waitKey(0)
cv2.destroyAllWindows()