import cv2
import numpy as np
import time

# Open camera
cap = cv2.VideoCapture(0)

# Check camera
if not cap.isOpened():
    print("Camera not found. Try changing 0 to 1.")
    exit()

# Drawing variables
drawing = False
ix, iy = -1, -1
canvas = None

def draw(event, x, y, flags, param):
    global drawing, ix, iy, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (ix, iy), (x, y), (0, 255, 0), 5)
            ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# Create window
cv2.namedWindow("Camera Drawing")
cv2.setMouseCallback("Camera Drawing", draw)

start_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot read camera frame.")
        break

    frame = cv2.flip(frame, 1)

    # Create canvas once
    if canvas is None:
        canvas = np.zeros_like(frame)

    # Add drawing to camera
    output = cv2.add(frame, canvas)

    # Running time
    elapsed = int(time.time() - start_time)
    minutes = elapsed // 60
    seconds = elapsed % 60

    cv2.putText(
        output,
        f"Time: {minutes:02d}:{seconds:02d}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.putText(
        output,
        "Draw: Mouse | Clear: C | Exit: Q",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 255, 255),
        2
    )

    cv2.imshow("Camera Drawing", output)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('c'):
        canvas = np.zeros_like(frame)

cap.release()
cv2.destroyAllWindows()