import cv2

for i in range(5):
    print(f"Testing camera {i}")
    cap = cv2.VideoCapture(i)

    if cap.isOpened():
        ret, frame = cap.read()
        print(f"Camera {i}: Opened={cap.isOpened()} Read={ret}")
    else:
        print(f"Camera {i}: Not opened")

    cap.release()