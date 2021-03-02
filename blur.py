import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)
# AVERAGING
average = cv.blur(img, (7,7))
cv.imshow('Average blur', average)

# Gaussian Blur
# Average of the products natural method

varun = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian blur', varun)

# Median blur
median = cv.medianBlur(img, 7)
cv.imshow('Median blur', median)

# bilateral blur
# you can retain image edges

bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)