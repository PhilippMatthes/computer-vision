import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
fgbg = cv.createBackgroundSubtractorMOG2()

while True:
    try:
        _, frame = cap.read()

        fgmask = fgbg.apply(frame)

        cv.imshow("foreground", fgmask)

        cv.waitKey(5)

    except KeyboardInterrupt:
        print("Shutting down pipes...")
        cv.destroyAllWindows()
        cap.release()
        break