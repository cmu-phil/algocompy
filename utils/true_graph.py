import numpy as np
import sys

from causallearn.graph.GraphNode import GraphNode
from causallearn.graph.GeneralGraph import GeneralGraph
from causallearn.utils.DAG2CPDAG import dag2cpdag


def TrueGraph(g, p, myrange):

    if myrange == 0:
        M = p

        nodes = [GraphNode('x'+str(x)) for x in range(M)]

        G = GeneralGraph(nodes)

        for i in range(len(nodes)):
            for j in np.where(g[i] != 0)[0]:
                G.add_directed_edge(nodes[j], nodes[i])
        
        G = dag2cpdag(G)

        return G
    
    elif myrange == 1:
        M = p

        nodes = [GraphNode('X'+str(x)) for x in range(1, M+1)]


        G = GeneralGraph(nodes)

        for i in range(len(nodes)):
            for j in np.where(g[i] != 0)[0]:
                G.add_directed_edge(nodes[j], nodes[i])
        
        G = dag2cpdag(G)

        return G
    else:
        sys.exit("error: True Graph out of range")