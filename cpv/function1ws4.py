import cv2
import numpy as np

# Load the image
img = cv2.imread('img.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Initialize the snake contour
snake = np.array([[100, 100], [200, 100], [200, 200], [100, 200]], np.int32)

# Define the parameters for the Snake algorithm
alpha = 0.1
beta = 1.0
gamma = 0.01
iterations = 500

# Run the Snake algorithm
snake = cv2.cvtColor(snake, cv2.COLOR_BGR2GRAY)
snake = snake.reshape((-1, 1, 2))
cv2.fillPoly(img, [snake], (0, 255, 0))
cv2.imshow('Initial Contour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
snake = snake.reshape((-1, 2))
snake = cv2.cvtColor(snake, cv2.COLOR_GRAY2BGR)

for i in range(iterations):
    # Calculate the external energy of the snake
    external_energy = cv2.Sobel(blurred, cv2.CV_32F, 1, 0) ** 2 + cv2.Sobel(blurred, cv2.CV_32F, 0, 1) ** 2
    external_energy = cv2.GaussianBlur(external_energy, (5, 5), 0)

    # Calculate the internal energy of the snake
    dxdy = cv2.Sobel(snake, cv2.CV_32F, 1, 1)
    internal_energy = beta * dxdy[:, :, 0] ** 2 + alpha * dxdy[:, :, 1] ** 2

    # Calculate the image energy
    image_energy = -gamma * external_energy
    for j in range(snake.shape[0]):
        image_energy[j] += external_energy[snake[j, 1], snake[j, 0]] + internal_energy[j]

    # Update the snake contour
    snake += cv2.grabCut(img, snake.astype(np.int32), None, None, 1, cv2.GC_INIT_WITH_RECT)[0] == 1

# Draw the final snake contour on the original image
cv2.drawContours(img, [snake.astype(np.int32)], -1, (0, 0, 255), 2)

# Display the final result
cv2.imshow('Segmented Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
