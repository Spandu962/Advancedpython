import cv2
import numpy as np

drawing = False
ix, iy = -1, -1

# Create white image
img = np.ones((500, 700, 3), np.uint8) * 255

def draw_rectangle(event, x, y, flags, param):
    global drawing, ix, iy, img

    # Mouse button pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # Mouse moved while pressing
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp = img.copy()
            cv2.rectangle(temp, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("Rectangle", temp)

    # Mouse button released
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)

# Create window
cv2.namedWindow("Rectangle")
cv2.setMouseCallback("Rectangle", draw_rectangle)

# Display window
while True:
    cv2.imshow("Rectangle", img)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC key
        break

cv2.destroyAllWindows()