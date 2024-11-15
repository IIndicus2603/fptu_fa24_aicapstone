import cv2
import numpy as np

def gaussian_smoothing(image, kernel_size, sigma):
    # Create a 2D Gaussian filter
    kernel = cv2.getGaussianKernel(kernel_size, sigma)
    kernel = kernel * kernel.T
    
    # Apply the filter to the image
    smoothed_image = cv2.filter2D(image, -1, kernel)
    
    return smoothed_image

# Load an image
image = cv2.imread("noiseimg.jpg", 0)

# Apply Gaussian smoothing to the image
kernel_size = 3
sigma = 0.5
smoothed_image = gaussian_smoothing(image, kernel_size, sigma)

# Display the original and smoothed images
cv2.imshow("Original", image)
cv2.imshow("Smoothed", smoothed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
