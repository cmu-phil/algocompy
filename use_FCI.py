from causallearn.search.ConstraintBased.FCI import fci
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import SHD as shd
import myStatistics as stat
from causallearn.utils.DAG2PAG import dag2pag
import numpy as np
import sys

from causallearn.graph.GraphNode import GraphNode
from causallearn.graph.GeneralGraph import GeneralGraph
from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz


def FCI(data, G):
    """
    Runs FCI algorithm with given data.
    Computes adjacency and Arrowhead confusion between estimated and true graph.
    Saves results into matrix.
    -----------
    data: sample data
    G: true graph
    """

    # testfci = fci(data, fisherz, 0.01, verbose=False)
    testpc = pc(data, 0.01, fisherz, True, 0, -1).G

    fciPerformance = FCIstats(G, testpc)

    return fciPerformance


def FCIstats(G, testfci):
    fciStat = []

    # Adjacency and Arrowhead
    ACfci = AdjConf.AdjacencyConfusion(G, testfci)
    ArrCfci = ArrConf.ArrowConfusion(G, testfci)

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

    # SHD
    SHDfci = shd.SHD(G, testfci)

    fciStat.append(SHDfci.get_shd())

    return fciStat
