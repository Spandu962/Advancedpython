import cv2

lines = []
drawing = False
start_point = None


def mouse_callback(event, x, y, flags, param):
    global drawing, start_point

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        lines.append((start_point, (x, y)))


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera could not be opened")
    exit()

cv2.namedWindow("Live Webcam Lines")
cv2.setMouseCallback("Live Webcam Lines", mouse_callback)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read camera")
        break

    for start, end in lines:
        cv2.line(
            frame,
            start,
            end,
            (0, 255, 0),
            3
        )

    cv2.imshow("Live Webcam Lines", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()