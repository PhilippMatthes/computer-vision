import numpy as np
import matplotlib.pyplot as plt

from image_processing import show_image, read_image_grayscale


def calculate_polynomial(x1, y1, x2, y2):
    # Calculate polynomial
    a = np.array([[x1 * x1 * x1, x1 * x1, x1, 1],
                  [x2 * x2 * x2, x2 * x2, x2, 1],
                  [3 * x1 * x1, 2 * x1, 1, 0],
                  [3 * x2 * x2, 2 * x2, 1, 0]])
    b = np.array([y1, y2, 0, 0])
    e = np.linalg.solve(a, b)
    return e


def adjust_image(polynomial, img):
    assert len(polynomial) == 4

    # grab the image dimensions
    h = img.shape[0]
    w = img.shape[1]

    for y in range(0, h):
        for x in range(0, w):
            c = img[y, x]
            value = polynomial[0] * pow(c, 3) + polynomial[1] * pow(c, 2) + polynomial[2] * c + polynomial[3]
            img[y, x] = value

    return img


def visualize_polynomial(polynomial, low=0, high=255):
    values = [polynomial[0] * pow(c, 3) + polynomial[1] * pow(c, 2) + polynomial[2] * c + polynomial[3]
              for c in range(low, high)]
    plt.plot(values)
    plt.show()


if __name__ == "__main__":
    img = read_image_grayscale("images/apb.jpg")
    polynomial = calculate_polynomial(60, 60, 180, 180)
    solarized_img = adjust_image(polynomial, img)
    visualize_polynomial(polynomial)
    show_image(solarized_img)


