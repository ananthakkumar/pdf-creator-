import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image of the document
img = cv2.imread('images\img1.jpg')

# Find the four corners of the document
pts = cv2.cornerHarris(img, 2, 3, 0.04)
pts = pts.reshape(-1, 2)

# Rearrange the order of the corners
rect = order_points(pts)

# Warp the image so that it is aligned properly
warped = cv2.warpAffine(img, rect, (img.shape[1], img.shape[0]))

# Save the warped image
cv2.imwrite('warped.png')