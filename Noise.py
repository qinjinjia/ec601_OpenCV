# Copyright 2017 Qinjin Jia qjia@bu.edu

""" EC601_OpenCV_Exercise 2 smoothing
    type python Noise.py IMAGE_NAME in terminal to run
    python Noise.py cameraman.png, for instance"""

import sys
import cv2
import copy
from random import randint


def add_gaussian_noise(img, mean, sigma):
    "add gaussian noise to the image"
    img_gaussian = copy.deepcopy(img)
    cv2.randn(img_gaussian, mean, sigma)
    img_gaussian = cv2.add(img_gaussian, img)
    return img_gaussian


def add_salt_pepper_noise(img, pa, pb):
    "add salt and pepper noise to the image"
    img_sp = copy.deepcopy(img)
    rows, cols = img_sp.shape
    amount1, amount2 = int(rows * cols * pa), int(rows * cols * pb)
    for i in range(amount1):  # pepper noise
        img_sp[randint(0, rows - 1), randint(0, cols - 1)] = 0    # [low, high]
    for i in range(amount2):  # salt noise
        img_sp[randint(0, rows - 1), randint(0, cols - 1)] = 255
    return img_sp


def main():
    "main"
    img_name = sys.argv[1]

    # original
    src = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('Original image', src)

    # add Gaussian noise
    mean = 0
    sigma = 50
    noise_img = add_gaussian_noise(src, mean, sigma)
    cv2.imshow('Gaussian Noise', noise_img)

    # Box filter
    noise_dst = cv2.blur(noise_img, (3, 3))
    cv2.imshow('Gaussian Noise - Box filter', noise_dst)

    # Gaussian filter
    noise_dst1 = cv2.GaussianBlur(noise_img, (3, 3), 1.5)
    cv2.imshow('Gaussian Noise - Gaussian filter', noise_dst1)

    # Median filter
    noise_dst2 = cv2.medianBlur(noise_img, 3)
    cv2.imshow('Gaussian Noise - Median filter', noise_dst2)

    # add salt and peper noise
    pa = 0.01
    pb = 0.01
    noise_img2 = add_salt_pepper_noise(src, pa, pb)
    cv2.imshow('Salt and Pepper Noise', noise_img2)

    # Box filter, Salt and Pepper Noise
    noise_dst3 = cv2.blur(noise_img2, (3, 3))
    cv2.imshow('Salt and Pepper Noise - Box filter', noise_dst3)

    # Gaussian filter, Salt and Pepper Noise
    noise_dst4 = cv2.GaussianBlur(noise_img2, (3, 3), 1.5)
    cv2.imshow('Salt and Pepper Noise - Gaussian filter', noise_dst4)

    # Median filter, Salt and Pepper Noise
    noise_dst5 = cv2.medianBlur(noise_img2, 3)
    cv2.imshow('Salt and Pepper Noise - Median filter', noise_dst5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
