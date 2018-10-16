import cv2


def read_image_grayscale(filename):
    return cv2.imread(filename, 0)


def read_image(filename):
    return cv2.imread(filename)


def show_image(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_image(filename, image):
    cv2.imwrite(filename, image)


def edge_detection(image, thr_low=0, thr_high=255):
    return cv2.Canny(image,thr_low, thr_high)


def bilateral_filter(image):
    return cv2.bilateralFilter(image, 9, 75, 75)


if __name__ == "__main__":
    img = read_image("images/apb.jpg")
    for i in range(0, 255):
        blur = bilateral_filter(img)
        edges = edge_detection(blur, thr_low=i, thr_high=i)
        save_image("images/created/canny_bilateral_filter/apb_{}_{}.jpg".format(i, i), edges)
