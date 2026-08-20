import cv2

image = cv2.imread("image.jpg")

if image is None:
    image = 255 * __import__("numpy").ones((500, 700, 3), dtype="uint8")

drawing = False
start_point = None


def mouse_callback(event, x, y, flags, param):
    global drawing, start_point, image

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        temp = image.copy()

        cv2.rectangle(
            temp,
            start_point,
            (x, y),
            (0, 255, 0),
            2
        )

        cv2.imshow("Draw Shapes", temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

        end_point = (x, y)

        cv2.rectangle(
            image,
            start_point,
            end_point,
            (0, 255, 0),
            2
        )

        cv2.imshow("Draw Shapes", image)


cv2.namedWindow("Draw Shapes")
cv2.setMouseCallback("Draw Shapes", mouse_callback)

cv2.imshow("Draw Shapes", image)

while True:
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()