import cv2 as cv
import numpy as np

cv.destroyAllWindows()
cap = cv.VideoCapture(0)

while True:
    try:
        _, frame = cap.read()

        laplacian = cv.Laplacian(frame, cv.CV_64F)
        sobelx = cv.Sobel(frame, cv.CV_64F, 1, 0, ksize=5)
        sobely = cv.Sobel(frame, cv.CV_64F, 0, 1, ksize=5)

        cv.imshow("laplacian", laplacian)
        cv.imshow("sobelx", sobelx)
        cv.imshow("sobely", sobely)

        cv.waitKey(5)

    except KeyboardInterrupt:
        print("Shutting down pipes...")
        cv.destroyAllWindows()
        cap.release()
        break
