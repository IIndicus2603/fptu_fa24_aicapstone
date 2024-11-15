import cv2
import numpy as np

# Load the image and convert it to grayscale
img = cv2.imread('j.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Detect lines using Hough transform
lines = cv2.HoughLines(edges, 1, np.pi/180, 150)

# Convert lines from polar to Cartesian coordinates
cartesian_lines = []
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cartesian_lines.append((x1, y1, x2, y2))

# Find intersections of lines
intersections = []
for i, line1 in enumerate(cartesian_lines[:-1]):
    for line2 in cartesian_lines[i+1:]:
        x1, y1, x2, y2 = line1
        x3, y3, x4, y4 = line2
        denominator = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if denominator != 0:
            x = ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4))/denominator
            y = ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4))/denominator
            intersections.append((x, y))

# Find corners of rectangles
corners = []
for i, point1 in enumerate(intersections[:-1]):
    for point2 in intersections[i+1:]:
        dist = np.linalg.norm(np.array(point1) - np.array(point2))
        if 100 < dist < 300:
            corners.append((point1, point2))

# Draw rectangles on the image
for corner_pair in corners:
    corner1, corner2 = corner_pair
    cv2.rectangle(img, (int(corner1[0]), int(corner1[1])), (int(corner2[0]), int(corner2[1])), (0, 0, 255), 2)

# Show the result
cv2.imshow('Rectangle detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
