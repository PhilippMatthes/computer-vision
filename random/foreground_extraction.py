import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

cap = cv.VideoCapture(0)
_, frame = cap.read()
cap.release()

mask = np.zeros(frame.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (161, 79, 150, 150)

cv.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
img = frame * mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
