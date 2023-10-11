import random
import math
import matplotlib.pyplot as plt

#first step of k-means algortihm, assign vectors to nearest representatives
def assign_clusters(data, centers):
    clusters = []
    for point in data:
        distances = [math.dist(point, center) for center in centers]
        cluster = distances.index(min(distances))
        clusters.append(cluster)
    return clusters

#second step of k-means algorithm, update representatives
def update_centers(data, clusters, k):
    centers = []
    for i in range(k):
        cluster_points = [data[j] for j in range(len(data)) if clusters[j] == i]
        center = [sum(coords) / len(cluster_points) for coords in zip(*cluster_points)]
        centers.append(center)
    return centers

#k-means algorithm
def k_means(data, k, initial_centers):
    centers = initial_centers
    while True:
        clusters = assign_clusters(data, centers)
        new_centers = update_centers(data, clusters, k)
        if centers == new_centers: #if not equal -> convergence
            break
        centers = new_centers
    return clusters, centers

def main():
    data = [[2, 3], [1, 5], [4, 6], [6, 2], [7, 4], [8, 5], [3, 1], [5, 3], [6, 6], [7, 7], [9, 2], [3, 5]] #some random data set consisting of 2dim vectors
    k = 3
    initial_centers = random.sample(data, k) #take 3 random vectors from data for the initial representatives
    clusters, centers = k_means(data, k, initial_centers)
    plt.scatter([point[0] for point in data], [point[1] for point in data], c=clusters)
    plt.scatter([center[0] for center in centers], [center[1] for center in centers], c='red', marker='x')
    plt.show()