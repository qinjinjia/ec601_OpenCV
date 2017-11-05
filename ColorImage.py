# Copyright 2017 Qinjin Jia qjia@bu.edu

""" EC601_OpenCV_Exercise 2 colorspace conversion
    type python ColorImage.py IMAGE_NAME in terminal to run
    python ColorImage.py Lenna.png, for instance"""

import sys
import cv2


def colorspace(file_name):
    "colorspace conversion"
    # original
    src = cv2.imread(file_name, cv2.IMREAD_COLOR)  # ignore transparency
    cv2.imshow('Original image', src)

    # BGR
    (B, G, R) = cv2.split(src)
    cv2.imshow('Red', R)
    cv2.imshow('Green', G)
    cv2.imshow('Blue', B)

    # YCRCB
    (Y, Cb, Cr) = cv2.split(cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb))
    cv2.imshow('Y', Y)
    cv2.imshow('Cb', Cb)
    cv2.imshow('Cr', Cr)

    # HSV
    (Hue, Saturation, Value) = cv2.split(cv2.cvtColor(src, cv2.COLOR_BGR2HSV))
    cv2.imshow('Hue', Hue)
    cv2.imshow('Saturation', Saturation)
    cv2.imshow('Value', Value)

    # Save each image
    cv2.imwrite('exercise2_py_results/Original image.png', src)
    cv2.imwrite('exercise2_py_results/Red.png', R)
    cv2.imwrite('exercise2_py_results/Green.png', G)
    cv2.imwrite('exercise2_py_results/Blue.png', B)
    cv2.imwrite('exercise2_py_results/Y.png', Y)
    cv2.imwrite('exercise2_py_results/Cb.png', Cb)
    cv2.imwrite('exercise2_py_results/Cr.png', Cr)
    cv2.imwrite('exercise2_py_results/Hue.png', Hue)
    cv2.imwrite('exercise2_py_results/Saturation.png', Saturation)
    cv2.imwrite('exercise2_py_results/Value.png', Value)

    # Print Value at (20, 25)
    print('R(20,25):',R[20][25])
    print('G(20,25):',G[20][25])
    print('B(20,25):',B[20][25])

    print('Y(20,25):',Y[20][25])
    print('Cb(20,25):',Cb[20][25])
    print('Cr(20,25):',Cr[20][25])

    print('Hue(20,25):',Hue[20][25])
    print('Saturation(20,25):',Saturation[20][25])
    print('Value(20,25):',Value[20][25])

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    "main"
    colorspace(sys.argv[1])


if __name__ == '__main__':
    main()
