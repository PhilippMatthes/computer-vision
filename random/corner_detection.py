import cv2 as cv
import numpy as np

cv.destroyAllWindows()
cap = cv.VideoCapture(0)

while True:
    try:
        _, frame = cap.read()

        gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
        gray = np.float32(gray)

        amount = 1000
        quality = 0.01
        min_dist = 10
        corners = cv.goodFeaturesToTrack(gray, amount, quality, min_dist)

        corners = np.int0(corners)

        for corner in corners:
            x, y = corner.ravel()
            radius = 3
            color = 255
            cv.circle(frame, (x, y), radius, color, -1)

        cv.imshow("corners", frame)

        cv.waitKey(5)

    except KeyboardInterrupt:
        print("Shutting down pipes...")
        cv.destroyAllWindows()
        cap.release()
        break