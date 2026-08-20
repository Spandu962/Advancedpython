import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not found")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    flipped = cv2.flip(frame, 1)

    cv2.imshow("Original Video", frame)
    cv2.imshow("Flipped Video", flipped)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()