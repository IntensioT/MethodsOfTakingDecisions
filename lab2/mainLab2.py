import numpy as np
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt

from main import KMeansClustering


class MaxiMinClustering:
    def __init__(self, k):
        self.k = k  # maximum number of clusters
        self.centroids = []  # list of cluster centroids
        self.labels = []  # list of cluster labels

    def fit(self, X):
        # randomly select the first centroid
        i = np.random.randint(len(X))
        self.centroids.append(X[i])
        self.labels.append(0)

        # save the original data
        X_orig = X.copy()

        # find the most distant object from the first centroid and make it the second centroid
        dist = cdist(X, [self.centroids[0]], metric='euclidean')
        j = np.argmax(dist)
        self.centroids.append(X[j])
        self.labels.append(1)

        # plot the initial state of points with the first two centroids
        plt.figure()
        plt.scatter(X_orig[:, 0], X_orig[:, 1], s=1)
        plt.scatter(self.centroids[0][0], self.centroids[0][1], c='r', marker="*", s=200)
        plt.scatter(self.centroids[1][0], self.centroids[1][1], c='g', marker="*", s=200)
        plt.title("Initial state with first two centroids maximin")
        plt.show()

        # repeat until the desired number of clusters is reached or no more objects are left
        while len(self.centroids) < self.k and len(self.centroids) < len(X):
            # find the distance to the nearest centroid for each object
            dist = cdist(X, self.centroids, metric='euclidean')
            min_dist = np.min(dist, axis=1)

            # find the object with the maximum distance to the nearest centroid and make it a new centroid
            k = np.argmax(min_dist)
            self.centroids.append(X[k])
            self.labels.append(len(self.centroids) - 1)

            # remove the new centroid from the data
            X = np.delete(X, k, axis=0)

        # recalculate the centroids as the mean of the objects in each cluster
        self.centroids = np.array(self.centroids)
        for i in range(len(self.centroids)):
            cluster = X[self.labels == i]
            if len(cluster) > 0:
                self.centroids[i] = np.mean(cluster, axis=0)

        # assign each object to the nearest centroid
        dist = cdist(X, self.centroids, metric='euclidean')
        self.labels = np.argmin(dist, axis=1)

# generate some random data
random_points = np.random.randint(0, 1000, (5000, 2))

# create an instance of the MaxiMinClustering class with k=4
maximin = MaxiMinClustering(k=4)

# fit the data and get the labels
labels = maximin.fit(random_points)

# plot the final state of clusters with the centroids
plt.figure()
plt.scatter(random_points[:, 0], random_points[:, 1], c=labels, s=1)
plt.scatter(maximin.centroids[:, 0], maximin.centroids[:, 1], c=range(len(maximin.centroids)), marker="*", s=200)
plt.title("Final clusters maximin")
plt.show()

kmeans = KMeansClustering(k=maximin.k)
labels = kmeans.fit(random_points, centroids=maximin.centroids)

plt.figure()
plt.scatter(random_points[:, 0], random_points[:, 1], c = labels, s=1)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:,1], c=range(len(kmeans.centroids)), marker="*", s=200)
plt.title("Final clusters kmeans")

plt.show()

