import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
import cv2

image = cv2.imread('face.jpeg', 0)
edges = cv2.Canny(image, 100, 200)
points = np.column_stack(np.where(edges > 0)) 

db = DBSCAN(eps=10, min_samples=10).fit(points)
labels = db.labels_

plt.scatter(points[:, 1], points[:, 0], c=labels, cmap='viridis', s=1)
plt.title("Face Features Segmented by DBSCAN")
plt.gca().invert_yaxis()
plt.show()