import cv2
import numpy as np

# Create a simple image
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Draw shapes
cv2.rectangle(image, (100, 100), (500, 300), (255, 0, 0), -1)
cv2.circle(image, (300, 200), 80, (0, 255, 0), -1)

# Save image
cv2.imwrite("image.jpg", image)

print("image.jpg created successfully!")