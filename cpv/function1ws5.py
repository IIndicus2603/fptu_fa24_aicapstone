import cv2
import numpy as np

def ransac(image1, image2, n_iter, dist_threshold):
    # Detect features and extract descriptors using SIFT
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(image1, None)
    kp2, des2 = sift.detectAndCompute(image2, None)

    # Match descriptors using Brute Force Matcher
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test to select good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    if len(good_matches) < 4:
        return None

    # Convert keypoint coordinates to numpy arrays
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

    best_transform = None
    max_inliers = 0

    for i in range(n_iter):
        # Randomly select 4 correspondences
        idx = np.random.choice(len(good_matches), 4, replace=False)
        src_pts_rand = src_pts[idx]
        dst_pts_rand = dst_pts[idx]

        # Estimate transform using 4 correspondences
        transform, _ = cv2.estimateAffinePartial2D(src_pts_rand, dst_pts_rand)

        # Calculate inliers
        src_pts_transformed = cv2.transform(src_pts, transform)
        distances = np.linalg.norm(src_pts_transformed - dst_pts, axis=2)
        inliers = np.sum(distances < dist_threshold)

        # Update best transform if better inlier count
        if inliers > max_inliers:
            best_transform = transform
            max_inliers = inliers

    return best_transform

# Load two images
image1 = cv2.imread('img.jpg')
image2 = cv2.imread('noiseimg.jpg')

# Align images using RANSAC
n_iter = 100
dist_threshold = 5.0
transform = ransac(image1, image2, n_iter, dist_threshold)

if transform is not None:
    # Apply transform to image1
    aligned_image = cv2.warpAffine(image1, transform, (image1.shape[1], image1.shape[0]))

    # Display aligned image
    cv2.imshow('Aligned Image', aligned_image)
    cv2
