import numpy as np
import cv2 as cv

from image_processing import show_image, read_image_grayscale


def solarize_image(x1, y1, x2, y2, img):

    # Calculate polynomial
    a = np.array([[x1*x1*x1, x1*x1, x1, 1],
                  [x2*x2*x2, x2*x2, x2, 1],
                  [3*x1*x1, 2*x1, 1, 0],
                  [3*x2*x2, 2*x2, 1, 0]])
    b = np.array([y1, y2, 0, 0])
    e = np.linalg.solve(a, b)

    print("Computed polynomial: y = f(x) = {}x^3 + {}x^2 + {}x^1 + {}".format(e[0], e[1], e[2], e[3]))

    # grab the image dimensions
    h = img.shape[0]
    w = img.shape[1]

    for y in range(0, h):
        for x in range(0, w):
            c = img[y, x]
            value = e[0] * (c*c*c) + e[1] * (c*c) + e[2] * c + e[3]
            img[y, x] = value

    return img


if __name__ == "__main__":
    img = read_image_grayscale("images/apb.jpg")
    solarized_img = solarize_image(60, 60, 180, 180, img)
    show_image(solarized_img)
