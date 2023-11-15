import numpy as np


def dijkstra(Graph, i, j):

    if i == j:
        return 0, []

    n = np.size(Graph, 1)
    frontier = [i]
    parent = {i: None}
    dist = {i: 0}

    while len(frontier) > 0:
        min_dist = np.inf
        x = frontier[0]
        for noeud in frontier:
            if dist[noeud] < min_dist:
                x = noeud
                min_dist = dist[noeud]
        frontier.remove(x)
        for y in range(n):
            if y not in parent:
                frontier.append(y)
            new_dist = dist[x] + Graph[x, y]
            if y not in dist or dist[y] > new_dist:
                dist[y] = new_dist
                parent[y] = x

    distance = dist[j]
    Chemin = []
    while j != i:
        Chemin.append(j)
        j = parent[j]

    return distance, Chemin
