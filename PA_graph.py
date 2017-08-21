import networkx as nx
import matplotlib.pyplot as plt
import random
import copy
import numpy as np
import pylab
import math
import pickle


# The following function creates a graph that creates a graph that follows the preferential attachment model.
# networkx library comes with a different implementation of the Barabasi Albert model.
# Here we implement the one presented in Random Graphs (by Alan Frieze).
def pa_graph(m, n):
    G = nx.MultiGraph()
    G.add_node(1)
    for x in range(0, m):
        G.add_edge(1, 1)
    # so far we created G_m^(1)
    targets = [1] * 2 * m
    vertex = 2
    # we start adding the vertices starting from vertex two and working our way up.
    while vertex < n + 1:
        G.add_node(vertex)
        # create a shallow copy of the targets. We will be using this one to randomly choose the neighbors of x.
        targets2 = copy.copy(targets)
        for x in range(0, m):
            chosen = random.choice(targets2)
            G.add_edge(vertex, chosen)
            # we update our targets list so we can use it for the next vertex.
            targets.append(chosen)
            targets.append(vertex)
        vertex += 1
    return G
