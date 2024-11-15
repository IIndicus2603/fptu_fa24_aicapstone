import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an example image with salt and pepper noise
image = cv2.imread("noiseimg.jpg", cv2.IMREAD_GRAYSCALE)

# Perform mean filtering
mean = cv2.blur(image, (3, 3))

# Plot the original and filtered images
plt.subplot(121), plt.imshow(image, cmap="gray", vmin=0, vmax=255)
plt.title("Noisy Image")
plt.subplot(122), plt.imshow(mean, cmap="gray", vmin=0, vmax=255)
plt.title("Filtered Image")

# Show the plot
plt.show()
