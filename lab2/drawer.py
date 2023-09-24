import matplotlib.pyplot as plt
from random import random


def display_result(vectors, clusters):
    colors = [[random() for _ in range(3)] for _ in range(len(clusters))]
    centroids_colors = [[1-x for x in color] for color in colors]
    for cluster_index, (centroid, cluster) in enumerate(clusters.items()):
        current_cluster = [vectors[i] for i in cluster]
        xs = list(map(lambda x: x[0], current_cluster))
        ys = list(map(lambda x: x[1], current_cluster))
        for vector in current_cluster:
            plt.plot([vector[0], centroid[0]], [vector[1], centroid[1]], c=colors[cluster_index], linewidth=1)
        plt.scatter(xs, ys, c=colors[cluster_index], marker='.')
        plt.plot(centroid[0], centroid[1], c=centroids_colors[cluster_index], marker='*', markersize=20)
    plt.show()
