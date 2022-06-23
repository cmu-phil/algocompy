import constants as const
import numpy as np

from causallearn.graph.Graph import Graph
from causallearn.graph.GraphNode import GraphNode
from causallearn.graph.GeneralGraph import GeneralGraph
from causallearn.utils.DAG2CPDAG import dag2cpdag

def makeTrueGraph(g):
    M = const.N

    nodes = [GraphNode('X'+str(x)) for x in range(1, M+1)]


    G = GeneralGraph(nodes)

    for i in range(len(nodes)):
        for j in np.where(g[i] != 0)[0]:
            G.add_directed_edge(nodes[j], nodes[i])
    
    G = dag2cpdag(G)

    return G