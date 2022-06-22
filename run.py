# files withing the project
import constants as const
import RandomSample as sampler
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import MakeResults as MR
from causallearn.graph.GeneralGraph import GeneralGraph
from causallearn.utils.DAG2CPDAG import dag2cpdag

# useful python libraries
import numpy as np
import pandas as pd

# causal-learn package
import causallearn as cl

from causallearn.search.ConstraintBased.PC import pc
from causallearn.search.ConstraintBased.FCI import fci
from causallearn.search.ConstraintBased.CDNOD import cdnod
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz
from causallearn.graph.Graph import Graph
from causallearn.graph.GraphNode import GraphNode

import os
import sys
import io
from causallearn.score.LocalScoreFunction import local_score_BDeu
from causallearn.utils.GraphUtils import GraphUtils
sys.path.append("")
import unittest
import warnings
from pickle import load
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


def run():

    data, g = sampler.sample(const.p, const.d, const.N)
    #print(data)

    #np.savetxt('randomDataset.txt', data, delimiter ='\t')

    M = const.N

    nodes = [GraphNode('X'+str(x)) for x in range(1, M+1)]


    G = GeneralGraph(nodes)

    for i in range(len(nodes)):
        for j in np.where(g[i] != 0)[0]:
            G.add_directed_edge(nodes[j], nodes[i])
    
    G = dag2cpdag(G)


    testpc = pc(data, const.d, gsq, True, 0, -1 )
    print("---------------------------------------")

    testfci = fci(data, fisherz, const.d, verbose=False)
    print("---------------------------------------")
    
    c_indx = np.reshape(np.asarray(list(range(data.shape[0]))), (data.shape[0],1))
    #print(c_indx)
    testcdnod = cdnod(data, c_indx, const.d, kci, True, 0, -1)
    print("---------------------------------------")

    #testpc.draw_pydot_graph()

    true_edges = set([(e.get_node1().get_name(), e.get_node2().get_name()) for e in G.get_graph_edges()])
    pred_edges = set([(e.get_node1().get_name(), e.get_node2().get_name()) for e in testpc.G.get_graph_edges()])

    sym_diff = true_edges ^ pred_edges
    flipped = set([(edge[1], edge[0]) for edge in sym_diff])
    intersect = sym_diff & flipped

    print(len(sym_diff) - len(intersect) / 2)


    pcStat = []

    ACpc = AdjConf.AdjacencyConfusion(G, testpc.G)
    ArrCpc = ArrConf.ArrowConfusion(G, testpc.G)

    pcStat.append(ACpc.get_adj_precision())
    pcStat.append(ACpc.get_adj_recall())
    pcStat.append(ArrCpc.get_arrows_precision())
    pcStat.append(ArrCpc.get_arrows_precision_ce())
    pcStat.append(ArrCpc.get_arrows_recall())
    pcStat.append(ArrCpc.get_arrows_recall_ce())
    pcStat.append(ACpc.get_adj_Mc())
    pcStat.append(ArrCpc.get_arrows_Mc())
    pcStat.append(ACpc.get_adj_F1())
    pcStat.append(ArrCpc.get_arrows_F1())


    fciStat = []

    ACfci = AdjConf.AdjacencyConfusion(G, testfci[0])
    ArrCfci = ArrConf.ArrowConfusion(G, testfci[0])

    fciStat.append(ACfci.get_adj_precision())
    fciStat.append(ACfci.get_adj_recall())
    fciStat.append(ArrCfci.get_arrows_precision())
    fciStat.append(ArrCfci.get_arrows_precision_ce())
    fciStat.append(ArrCfci.get_arrows_recall())
    fciStat.append(ArrCfci.get_arrows_recall_ce())
    fciStat.append(ACfci.get_adj_Mc())
    fciStat.append(ArrCfci.get_arrows_Mc())
    fciStat.append(ACfci.get_adj_F1())
    fciStat.append(ArrCfci.get_arrows_F1())

    cdnodStat = []

    ACcdnod = AdjConf.AdjacencyConfusion(G, testcdnod.G)
    ArrCcdnod = ArrConf.ArrowConfusion(G, testcdnod.G)

    cdnodStat.append(ACcdnod.get_adj_precision())
    cdnodStat.append(ACcdnod.get_adj_recall())
    cdnodStat.append(ArrCcdnod.get_arrows_precision())
    cdnodStat.append(ArrCcdnod.get_arrows_precision_ce())
    cdnodStat.append(ArrCcdnod.get_arrows_recall())
    cdnodStat.append(ArrCcdnod.get_arrows_recall_ce())
    cdnodStat.append(ACcdnod.get_adj_Mc())
    cdnodStat.append(ArrCcdnod.get_arrows_Mc())
    cdnodStat.append(ACcdnod.get_adj_F1())
    cdnodStat.append(ArrCcdnod.get_arrows_F1())

    #MR.makefile(pcStat, fciStat, cdnodStat)

    print("finish")




if __name__ == "__main__":
    run()