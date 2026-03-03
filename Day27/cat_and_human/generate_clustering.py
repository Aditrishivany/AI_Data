import os
import glob
import json
import numpy as np
from PIL import Image
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

def load_data(base_path):
    cats_path = os.path.join(base_path, 'cats', '*.jpg')
    humans_path = os.path.join(base_path, 'human', '*.jpg')
    
    cat_files = glob.glob(cats_path)
    human_files = glob.glob(humans_path)
    
    X = []
    y = [] # 0 for cat, 1 for human
    
    for f in cat_files:
        try:
            img = Image.open(f).convert('RGB').resize((64, 64))
            X.append(np.array(img).flatten())
            y.append(0)
        except Exception as e:
            print(f"Error loading {f}: {e}")
            
    for f in human_files:
        try:
            img = Image.open(f).convert('RGB').resize((64, 64))
            X.append(np.array(img).flatten())
            y.append(1)
        except Exception as e:
            print(f"Error loading {f}: {e}")
            
    return np.array(X), np.array(y)

def generate_notebook():
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Cat and Human Image Clustering\n",
                    "This notebook applies K-Means and DBSCAN clustering to the cat and human dataset.\n",
                    "We use **shapes** to represent the true classes (Circles for Cats, Squares for Humans) and **colors** to represent the assigned clusters."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import os\n",
                    "import glob\n",
                    "import numpy as np\n",
                    "from PIL import Image\n",
                    "from sklearn.decomposition import PCA\n",
                    "from sklearn.cluster import KMeans, DBSCAN\n",
                    "import matplotlib.pyplot as plt\n",
                    "import matplotlib.patches as mpatches\n",
                    "import matplotlib.lines as mlines\n",
                    "\n",
                    "import warnings\n",
                    "warnings.filterwarnings('ignore')"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 1. Load and Preprocess Data\n",
                    "We'll load the images, resize them to 64x64, and flatten them into 1D arrays."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "def load_data(base_path):\n",
                    "    cats_path = os.path.join(base_path, 'cats', '*.jpg')\n",
                    "    humans_path = os.path.join(base_path, 'human', '*.jpg')\n",
                    "    \n",
                    "    cat_files = glob.glob(cats_path)\n",
                    "    human_files = glob.glob(humans_path)\n",
                    "    \n",
                    "    X = []\n",
                    "    y = []\n",
                    "    \n",
                    "    for f in cat_files:\n",
                    "        img = Image.open(f).convert('RGB').resize((64, 64))\n",
                    "        X.append(np.array(img).flatten())\n",
                    "        y.append(0)\n",
                    "            \n",
                    "    for f in human_files:\n",
                    "        img = Image.open(f).convert('RGB').resize((64, 64))\n",
                    "        X.append(np.array(img).flatten())\n",
                    "        y.append(1)\n",
                    "            \n",
                    "    return np.array(X), np.array(y)\n",
                    "\n",
                    "X, y_true = load_data('dataset')\n",
                    "print(f\"Loaded {len(X)} images. Shape of X: {X.shape}\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 2. Dimensionality Reduction\n",
                    "Using PCA to reduce the features to 2 dimensions for visualization."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "pca = PCA(n_components=2, random_state=42)\n",
                    "X_pca = pca.fit_transform(X)\n",
                    "print(f\"Explained variance ratio: {pca.explained_variance_ratio_}\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 3. True Labels Visualization\n",
                    "Let's see where the true humans and true cats are located in the PCA space."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "plt.figure(figsize=(10, 7))\n",
                    "scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_true, cmap='coolwarm', alpha=0.9, s=150, edgecolors='k')\n",
                    "cat_patch = mpatches.Patch(color=scatter.cmap(scatter.norm(0)), label='Cat (True)')\n",
                    "human_patch = mpatches.Patch(color=scatter.cmap(scatter.norm(1)), label='Human (True)')\n",
                    "plt.legend(handles=[cat_patch, human_patch])\n",
                    "plt.title('True Labels (PCA)')\n",
                    "plt.xlabel('PCA Component 1')\n",
                    "plt.ylabel('PCA Component 2')\n",
                    "plt.show()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 4. K-Means Clustering\n",
                    "Applying K-Means to divide the points into 2 clusters."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)\n",
                    "kmeans_labels = kmeans.fit_predict(X)\n",
                    "\n",
                    "plt.figure(figsize=(10, 7))\n",
                    "for i, marker in zip([0, 1], ['o', 's']): # 0=Cat, 1=Human\n",
                    "    mask = (y_true == i)\n",
                    "    plt.scatter(X_pca[mask, 0], X_pca[mask, 1], c=kmeans_labels[mask], cmap='viridis', \n",
                    "                marker=marker, alpha=0.9, s=150, vmin=0, vmax=1, edgecolors='k')\n",
                    "\n",
                    "marker_cat = mlines.Line2D([0], [0], marker='o', color='w', label='True: Cat', markerfacecolor='gray', markersize=12, markeredgecolor='k')\n",
                    "marker_human = mlines.Line2D([0], [0], marker='s', color='w', label='True: Human', markerfacecolor='gray', markersize=12, markeredgecolor='k')\n",
                    "plt.legend(handles=[marker_cat, marker_human], loc='best')\n",
                    "\n",
                    "plt.title('K-Means Clustering (Colors=Clusters, Shapes=True Class)')\n",
                    "plt.xlabel('PCA Component 1')\n",
                    "plt.ylabel('PCA Component 2')\n",
                    "sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=0, vmax=1))\n",
                    "plt.colorbar(sm, ticks=[0, 1], label='K-Means Cluster ID', ax=plt.gca())\n",
                    "plt.show()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 5. DBSCAN Clustering\n",
                    "Applying DBSCAN to find complex clusters and outliers."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "dbscan = DBSCAN(eps=5000, min_samples=2)\n",
                    "dbscan_labels = dbscan.fit_predict(X_pca)\n",
                    "\n",
                    "plt.figure(figsize=(10, 7))\n",
                    "vmin, vmax = min(dbscan_labels), max(dbscan_labels)\n",
                    "for i, marker in zip([0, 1], ['o', 's']):\n",
                    "    mask = (y_true == i)\n",
                    "    plt.scatter(X_pca[mask, 0], X_pca[mask, 1], c=dbscan_labels[mask], cmap='plasma', \n",
                    "                marker=marker, alpha=0.9, s=150, vmin=vmin, vmax=vmax, edgecolors='k')\n",
                    "\n",
                    "plt.legend(handles=[marker_cat, marker_human], loc='best')\n",
                    "plt.title('DBSCAN Clustering (Colors=Clusters, Shapes=True Class)')\n",
                    "plt.xlabel('PCA Component 1')\n",
                    "plt.ylabel('PCA Component 2')\n",
                    "sm_db = plt.cm.ScalarMappable(cmap='plasma', norm=plt.Normalize(vmin=vmin, vmax=vmax))\n",
                    "plt.colorbar(sm_db, ticks=list(range(vmin, vmax+1)), label='DBSCAN Cluster ID (-1=Outlier)', ax=plt.gca())\n",
                    "plt.show()"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    
    with open('clustering_models.ipynb', 'w') as f:
        json.dump(notebook, f, indent=4)
    print("Notebook clustering_models.ipynb generated.")

def run_clustering():
    X, y_true = load_data('dataset')
    
    if len(X) == 0:
        print("No images found! Check path.")
        return
        
    print(f"Loaded {len(X)} images.")
    
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X)
    
    marker_cat = mlines.Line2D([0], [0], marker='o', color='w', label='True: Cat', markerfacecolor='gray', markersize=12, markeredgecolor='k')
    marker_human = mlines.Line2D([0], [0], marker='s', color='w', label='True: Human', markerfacecolor='gray', markersize=12, markeredgecolor='k')
    
    # 1. True Labels (Reference)
    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_true, cmap='coolwarm', alpha=0.9, s=150, edgecolors='k')
    cat_patch = mpatches.Patch(color=scatter.cmap(scatter.norm(0)), label='Cat (True)')
    human_patch = mpatches.Patch(color=scatter.cmap(scatter.norm(1)), label='Human (True)')
    plt.legend(handles=[cat_patch, human_patch])
    plt.title('True Labels View (PCA)')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.savefig('true_labels.png')
    plt.close()
    print("Saved true_labels.png")
    
    # 2. KMeans
    kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
    kmeans_labels = kmeans.fit_predict(X)
    
    plt.figure(figsize=(10, 7))
    for i, marker in zip([0, 1], ['o', 's']): # 0=Cat, 1=Human
        mask = (y_true == i)
        plt.scatter(X_pca[mask, 0], X_pca[mask, 1], c=kmeans_labels[mask], cmap='viridis', 
                    marker=marker, alpha=0.9, s=150, vmin=0, vmax=1, edgecolors='k')
        
    plt.legend(handles=[marker_cat, marker_human], loc='best')
    plt.title('K-Means Clustering (Colors = Clusters, Shapes = True Class)')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    sm = plt.cm.ScalarMappable(cmap='viridis', norm=plt.Normalize(vmin=0, vmax=1))
    plt.colorbar(sm, ticks=[0, 1], label='K-Means Cluster ID', ax=plt.gca())
    plt.savefig('kmeans_clusters.png')
    plt.close()
    print("Saved kmeans_clusters.png")
    
    # 3. DBSCAN
    dbscan = DBSCAN(eps=5000, min_samples=2)
    dbscan_labels = dbscan.fit_predict(X_pca)
    
    plt.figure(figsize=(10, 7))
    vmin, vmax = min(dbscan_labels), max(dbscan_labels)
    for i, marker in zip([0, 1], ['o', 's']):
        mask = (y_true == i)
        plt.scatter(X_pca[mask, 0], X_pca[mask, 1], c=dbscan_labels[mask], cmap='plasma', 
                    marker=marker, alpha=0.9, s=150, vmin=vmin, vmax=vmax, edgecolors='k')
                    
    plt.legend(handles=[marker_cat, marker_human], loc='best')
    plt.title('DBSCAN Clustering (Colors = Clusters, Shapes = True Class)')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    sm_db = plt.cm.ScalarMappable(cmap='plasma', norm=plt.Normalize(vmin=vmin, vmax=vmax))
    plt.colorbar(sm_db, ticks=list(range(vmin, vmax+1)), label='DBSCAN Cluster ID (-1=Outlier)', ax=plt.gca())
    plt.savefig('dbscan_clusters.png')
    plt.close()
    print("Saved dbscan_clusters.png")

if __name__ == '__main__':
    run_clustering()
    generate_notebook()
