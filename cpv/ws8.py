import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier

# Load the dataset
faces = []
labels = []
for i in range(1, 41):
    for j in range(1, 11):
        img = cv2.imread(f"subject01.centerlight.jpg", cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (100, 100))
        faces.append(img.flatten())
        labels.append(i)

# Convert the dataset to numpy arrays
faces = np.array(faces)
labels = np.array(labels)

# Compute the mean face
mean_face = np.mean(faces, axis=0)

# Compute the eigenfaces using PCA
pca = PCA(n_components=40)
eigenfaces = pca.fit_transform(faces - mean_face)

# Train the KNN classifier on the face space representations
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(eigenfaces, labels)

# Load the input image and preprocess it
input_img = cv2.imread("subject01.centerlight.jpg", cv2.IMREAD_GRAYSCALE)
input_img = cv2.resize(input_img, (700, 700))

# Compute the face space representation of the input image
if mean_face.shape != input_img.flatten().shape:
    raise print("Shape of mean_face doesn't match input_img")

# subtract mean_face from input_img
input_face = input_img.flatten() - mean_face
input_face_space = pca.transform([input_face])

# Predict the label of the input image using KNN classifier
pred_label = knn.predict(input_face_space)

# Print the predicted label
print("Predicted label:", pred_label[0])
