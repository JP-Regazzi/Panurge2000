import numpy as np
import random as rd


def set_graph(n, m=None):

    if m == None:
        m = n

    Graph = np.full((n*m, n*m), np.inf)
    Vit = np.zeros((n*m, n*m))
    v_max = 7

    for i in range(n*m):
        if i % n != 0:
            t = rd.randint(1, 4)
            Vit[i, i-1] = v_max/t
            Vit[i-1, i] = v_max/t
            Graph[i, i-1] = t
            Graph[i-1, i] = t

        if i >= n:
            t = rd.randint(1, 4)
            Vit[i, i-n] = v_max/t
            Vit[i-n, i] = v_max/t
            Graph[i, i-n] = t
            Graph[i-n, i] = t

    return Graph
