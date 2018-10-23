import cv2


# 1. Install OpenCV with debug libs on your system.
# 2. Take two photos of a static (not changing) object,
# about 3m away from two view points, with about
# 10cm horizontal distance.
# 3. Measure the overall brightness of the two images and adjust
#  it to the mean value of the two images.
# 4. Create a mixed image and put the red channel from the
#  (adjusted) left image and the green and blue channel from
#  the right image into said mixed image.
#  Do this by (i) looping over all the pixels,
# (ii) by using opencv functions – compare the runtime!
# 5. View the mixed image with red-cyan glasses ;-)

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
