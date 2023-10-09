import numpy as np
import matplotlib.pyplot as plt

class KMeansClustering:

    def __init__(self, k=3):
        self.k = k
        self.centroids = None

    @staticmethod
    def euclidean_distance(data_point, centroids):
        return np.sqrt(np.sum((centroids - data_point)**2, axis = 1))

    #def fit(self, X, max_iterations=200): #выбирать центры между min и max данными
    #    self.centroids = np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0), size=(self.k, X.shape[1]))

    def fit(self, X, max_iterations=200, centroids=None):  # выбирать центры между min и max данными
        if centroids is not None:  # если центроиды переданы, то использовать их
                self.centroids = centroids
        else:  # если нет, то случайно выбрать центры между min и max данными
                self.centroids = np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0), size=(self.k, X.shape[1]))

        initial_centroids = self.centroids.copy()

        # Присваиваем метки кластеров каждой точке данных до выполнения алгоритма
        initial_labels = []
        for data_point in random_points:
            distances = KMeansClustering.euclidean_distance(data_point, initial_centroids)
            cluster_num = np.argmin(distances)
            initial_labels.append(cluster_num)

        # Строим график начального состояния кластеров
        plt.figure()
        plt.scatter(random_points[:, 0], random_points[:, 1], c=initial_labels, s=1)
        plt.scatter(initial_centroids[:, 0], initial_centroids[:, 1], c=range(len(initial_centroids)), marker="*",
                    s=200)
        plt.title("Initial clusters")

        for _ in range (max_iterations):
            y = []

            for data_point in X:
                distances = KMeansClustering.euclidean_distance(data_point, self.centroids)
                cluster_num = np.argmin(distances)
                y.append(cluster_num)

            y = np.array(y)

            cluster_indices = []

            for i in range(self.k):
                cluster_indices.append(np.argwhere(y == i))

            cluster_centers = []

            for i, indices in enumerate(cluster_indices):
                if len(indices) == 0:
                    cluster_centers.append(self.centroids[i])
                else:
                    cluster_centers.append(np.mean(X[indices], axis=0)[0])

            if np.max(self.centroids - np.array(cluster_centers)) < 0.0001:
                break
            else:
                self.centroids = np.array(cluster_centers)

        return y

random_points = np.random.randint(0, 1000, (5000, 2))
kmeans = KMeansClustering(k = 4)

labels = kmeans.fit(random_points)

# Строим график конечного состояния кластеров
plt.figure()
plt.scatter(random_points[:, 0], random_points[:, 1], c = labels, s=1)
plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:,1], c=range(len(kmeans.centroids)), marker="*", s=200)
plt.title("Final clusters")

plt.show()




