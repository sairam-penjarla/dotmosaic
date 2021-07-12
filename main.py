import cv2
import numpy as np
import matplotlib.pyplot as plt

file_name = ['a', 'b']


def converter(img_name):
    img = cv2.imread('/Users/sai/Desktop/everything/Programming/mosaic/images/' + str(img_name) + '.jpg')
    cv2.imwrite('/Users/sai/Desktop/everything/Programming/mosaic/static/images/' + str(img_name) + '.jpg', img)
    def adjust_gamma(image, gamma=1.0):
        invGamma = 1.0 / gamma
        table = np.array([
            ((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)])
        return cv2.LUT(image.astype(np.uint8), table.astype(np.uint8))

    circle_gap = 5
    image_resizer = 8
    border = 100
    print(img.shape[0], img.shape[1])
    if 200 < img.shape[0] < 500:
        # 251, 201
        circle_gap = 5  # circle gap
        image_resizer = 8  # image resizer
        border = 100  # border size
    if 500 < img.shape[0] < 1000:
        # 866 882
        circle_gap = 5  # circle gap
        image_resizer = 8  # image resizer
        border = 100  # border size
    if 1000 < img.shape[0] < 2000:
        # 1334 750
        circle_gap = 5  # circle gap
        image_resizer = 8  # image resizer
        border = 100  # border size
    if 2000 < img.shape[0] < 5000:
        # 4032 3024
        circle_gap = 5  # circle gap
        image_resizer = 60  # image resizer
        border = 350  # border size
    img = cv2.copyMakeBorder(img, border, border, border, border, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smaller = cv2.resize(img_gray, (int(img.shape[0] / image_resizer), int(img.shape[1] / image_resizer)))
    plt.figure(figsize=(int(smaller.shape[0] / circle_gap), int(smaller.shape[1] / circle_gap)))
    X, Y = np.meshgrid(np.arange(smaller.shape[1]), np.arange(smaller.shape[0]))
    plt.scatter(X.flatten(), Y.flatten(), c=smaller.flatten())
    plt.axis('off')
    plt.savefig('/Users/sai/Desktop/everything/Programming/mosaic/faces.png')
    img_new = cv2.imread('/Users/sai/Desktop/everything/Programming/mosaic/faces.png')
    img_new = cv2.rotate(img_new, cv2.ROTATE_180)
    img_new = cv2.flip(img_new, 1)
    img_new = adjust_gamma(img_new, gamma=0.4)
    cv2.imwrite('/Users/sai/Desktop/everything/Programming/mosaic/results/' + str(img_name) + '.jpg', img_new)
    cv2.imwrite('/Users/sai/Desktop/everything/Programming/mosaic/static/results/' + str(img_name) + '.jpg', img_new)

for i in file_name:
    converter(i)
