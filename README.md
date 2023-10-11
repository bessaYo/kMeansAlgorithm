# K-Means Clustering Algorithm

For a university seminar "Introduction to Machine Learning", I've developed a simple Python program to implement and demonstrate the K-Means clustering algorithm.

## Overview

The program leverages basic Python libraries such as `random`, `math`, and `matplotlib` for executing and visualizing the K-Means algorithm.

### Functionality

- **assign_clusters(data, centers)**:
   * Takes data points and cluster centers as input.
   * Assigns each data point to the nearest cluster center.
   * Returns a list of clusters, indicating the assignment of each data point to a cluster.

- **update_centers(data, clusters, k)**:
   * Based on the assignment of data points to clusters, this function recalculates the centers for each cluster.
   * Returns the updated cluster centers.

- **k_means(data, k, initial_centers)**:
   * Implements the core K-Means algorithm.
   * Continuously assigns data points to clusters and recalculates cluster centers until convergence.

- **main()**:
   * Demonstrates the K-Means algorithm on a sample dataset of 2-dimensional vectors.
   * Plots the dataset and the resulting clusters using `matplotlib`.

To execute the demonstration, simply run the script. The visualization will display the data points colored by their assigned cluster and the cluster centers marked with a red 'x'.
