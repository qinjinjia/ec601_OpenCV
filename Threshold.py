# Copyright 2017 Qinjin Jia qjia@bu.edu

""" EC601_OpenCV_Exercise 4 Threshold
    type python Threshold.py IMAGE_NAME in terminal to run
    python Threshold.py cameraman.png, for instance"""

import sys
import cv2


def main():
    "opencv threshold"
    img_name = sys.argv[1]

    # Load an image
    src = cv2.imread(img_name, cv2.IMREAD_COLOR)  # ignore transparency
    cv2.imshow('Input Image', src);

    # Convert the image to Gray
    grey = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)

    # 0: Binary,      1: Binary Inverted, 2: Threshold Truncated,      
    # 3: Threshold to Zero,      4: Threshold to Zero Inverted
    threshold_type = 2     # slider 1 [0, 4]
    threshold_value = 128  # slider 2 [0 255]

    (retval, dst) = cv2.threshold(grey, threshold_value, 255, 2)
    cv2.imshow('Thresholded Image', dst)

    current_threshold = 128
    max_threshold = 255

    # Binary Threshold
    (retval, thresholded) = cv2.threshold(grey, current_threshold, max_threshold, cv2.THRESH_BINARY)
    cv2.imshow('Binary threshold', thresholded)

    # Band thresholding
    threshold1, threshold2 = 27, 125
    (retval, binary_image1) = cv2.threshold(grey, threshold1, max_threshold, cv2.THRESH_BINARY)
    (retval, binary_image2) = cv2.threshold(grey, threshold2, max_threshold, cv2.THRESH_BINARY_INV)
    band_thresholded_image = cv2.bitwise_and(binary_image1, binary_image2)
    cv2.imshow('Band Thresholding', band_thresholded_image)

    # Semi thresholding
    (retval, semi_thresholded_image) = cv2.threshold(grey, current_threshold, max_threshold, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    semi_thresholded_image = cv2.bitwise_and(grey, semi_thresholded_image);
    cv2.imshow('Semi Thresholding', semi_thresholded_image);

    # Adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(grey, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 101, 10);
    cv2.imshow('Adaptive Thresholding', adaptive_thresh);

    # Save each image
    cv2.imwrite('exercise4_py_results/Input Image.png', src)
    cv2.imwrite('exercise4_py_results/Thresholded Image.png', dst)
    cv2.imwrite('exercise4_py_results/Binary threshold.png', thresholded)
    cv2.imwrite('exercise4_py_results/Band Thresholding.png', band_thresholded_image)
    cv2.imwrite('exercise4_py_results/Semi Thresholding.png', semi_thresholded_image)
    cv2.imwrite('exercise4_py_results/Adaptive Thresholding.png', adaptive_thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
