import cv2
import numpy as np
import tkinter as tk
from tkinter import Scale

def update_image(value):
    # Get the current values of the sliders
    r = red_scale.get()
    g = green_scale.get()
    b = blue_scale.get()

    # Perform color balance
    image_balanced = cv2.merge((
        np.clip(r * image[:, :, 0], 0, 255).astype(np.uint8),
        np.clip(g * image[:, :, 1], 0, 255).astype(np.uint8),
        np.clip(b * image[:, :, 2], 0, 255).astype(np.uint8),
    ))

    # Update the displayed image
    cv2.imshow("Image", image_balanced)

# Load an example image
image = cv2.imread("Img.jpg")

# Create the GUI window
root = tk.Tk()
root.title("Color Balance")

# Add the sliders to adjust red, green, and blue channels
red_scale = Scale(root, from_=0.0, to=2.0, resolution=0.01, orient=tk.HORIZONTAL, label="Blue", command=update_image)
red_scale.set(1.0)
red_scale.pack()

green_scale = Scale(root, from_=0.0, to=2.0, resolution=0.01, orient=tk.HORIZONTAL, label="Green", command=update_image)
green_scale.set(1.0)
green_scale.pack()

blue_scale = Scale(root, from_=0.0, to=2.0, resolution=0.01, orient=tk.HORIZONTAL, label="Red", command=update_image)
blue_scale.set(1.0)
blue_scale.pack()

# Show the initial image
cv2.imshow("Image", image)

# Start the GUI event loop
root.mainloop()