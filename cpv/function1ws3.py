import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt

class Snake:
    def __init__(self, image, alpha=0.1, beta=1.0, gamma=1.0, sigma=1.0):
        self.image = image
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.sigma = sigma
        self.kernel = self._get_gaussian_kernel(sigma)
        self.gradient = self._get_image_gradient(image)
        self.external_energy = self._get_external_energy(image)
        self.internal_energy = np.zeros_like(image)
        self.points = None

    def _get_gaussian_kernel(self, sigma):
        kernel_size = int(4 * sigma) | 1
        return np.exp(-np.square(np.arange(kernel_size) - kernel_size // 2) / (2 * sigma**2))

    def _get_image_gradient(self, image):
        gx = scipy.ndimage.filters.convolve1d(image, np.array([1, 0, -1]), axis=0, mode='wrap')
        gy = scipy.ndimage.filters.convolve1d(image, np.array([1, 0, -1]), axis=1, mode='wrap')
        return np.dstack((gx, gy))

    def _get_external_energy(self, image):
        smoothed_image = scipy.ndimage.filters.convolve(image, self.kernel, mode='wrap')
        gx = scipy.ndimage.filters.convolve1d(smoothed_image, np.array([1, 0, -1]), axis=0, mode='wrap')
        gy = scipy.ndimage.filters.convolve1d(smoothed_image, np.array([1, 0, -1]), axis=1, mode='wrap')
        return np.square(gx) + np.square(gy)

    def _get_internal_energy(self, points):
        dx = scipy.ndimage.filters.convolve1d(points, np.array([1, -1]), axis=0, mode='wrap')
        dy = scipy.ndimage.filters.convolve1d(points, np.array([1, -1]), axis=1, mode='wrap')
        dxx = scipy.ndimage.filters.convolve1d(dx, np.array([1, -1]), axis=0, mode='wrap')
        dyy = scipy.ndimage.filters.convolve1d(dy, np.array([1, -1]), axis=1, mode='wrap')
        dxy = scipy.ndimage.filters.convolve1d(dx, np.array([1, -1]), axis=1, mode='wrap')
        dyx = scipy.ndimage.filters.convolve1d(dy, np.array([1, -1]), axis=0, mode='wrap')
        return self.alpha * np.square(dxx + dyy) + self.beta * np.square(dxy + dyx)

    def evolve(self, points, iterations=100):
        self.points = points
        for i in range(iterations):
            internal_energy = self._get_internal_energy(self.points)
            total_energy = self.gamma * self.external_energy - (1 - self.gamma) * internal_energy
            gradient = self._get_image_gradient(total_energy)
            self.points += gradient
        return self.points

# Example usage:
image = plt.imread('img.jpg')
points = np.array([[50, 50], [60, 50], [70, 50], [80, 50], [90, 50]])
snake = Snake(image)
final_points = snake.evolve(points, iterations=100)
plt.imshow
