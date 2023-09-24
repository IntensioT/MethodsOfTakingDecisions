from math import sqrt
from random import randrange
from collections import defaultdict
from statistics import mean
from lab2.drawer import *


def sqr(a):
    return a*a


def distance(a, b):
    if len(a) != len(b):
        raise ValueError('Vectors have different dimensions')
    return sqrt(sum(map(sqr, (x-y for x, y in zip(a, b)))))


def allocate_clusters(vectors, centroids):
    clusters = defaultdict(list)
    for vector_index, vector in enumerate(vectors):
        centroid = min(centroids, key=lambda x: distance(vector, x))
        clusters[centroid].append(vector_index)
    return clusters


def average_centroids_distance(clusters: dict):
    return mean([distance(x, y) for x in clusters.keys() for y in clusters.keys()])


def get_new_centroid_index(vectors, clusters):
    result = None
    maxes = []
    for centroid in clusters.keys():
        maxes.append(max(((i, distance(centroid, vectors[i])) for i in clusters[centroid]), key=(lambda x: x[1])))
    true_max = max(maxes, key=(lambda x: x[1]))
    if true_max[1] > (average_centroids_distance(clusters) / 2):
        result = true_max[0]
    return result


def maximin(vectors):
    centroids = list()
    clusters = None
    new_centroid_index = randrange(len(vectors))
    while not (new_centroid_index is None):
        centroids.append(vectors[new_centroid_index])
        clusters = allocate_clusters(vectors, centroids)
        new_centroid_index = get_new_centroid_index(vectors, clusters)
        display_result(vectors, clusters)
    return clusters
