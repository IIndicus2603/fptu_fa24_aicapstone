import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the image
img = cv2.imread('img.jpg', 0)

# Perform histogram equalization
eq_img = cv2.equalizeHist(img)

# Plot the original and equalized histograms
plt.subplot(121)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Original Histogram')

plt.subplot(122)
plt.hist(eq_img.ravel(), 256, [0, 256])
plt.title('Equalized Histogram')

plt.show()

