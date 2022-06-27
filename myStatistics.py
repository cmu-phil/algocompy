import numpy as np
import constants as const
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import SHD as shd

import math


def PCstats (G, testpc):
    pcStat = []

    ACpc = AdjConf.AdjacencyConfusion(G, testpc)
    ArrCpc = ArrConf.ArrowConfusion(G, testpc)

    #Adjacency and Arrowhead Stats
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

    #SHD calculation
    # true_edges = set([(e.get_node1().get_name(), e.get_node2().get_name()) for e in G.get_graph_edges()])
    # pred_edges = set([(e.get_node1().get_name(), e.get_node2().get_name()) for e in testpc.get_graph_edges()])

    # sym_diff = true_edges ^ pred_edges
    # flipped = set([(edge[1], edge[0]) for edge in sym_diff])
    # intersect = sym_diff & flipped

    # pcStat.append(len(sym_diff) - len(intersect) / 2)

    SHDpc = shd.SHD(G, testpc)

    pcStat.append(SHDpc.get_shd())

    return pcStat

def FCIstats (G, testfci):
    fciStat = []

    ACfci = AdjConf.AdjacencyConfusion(G, testfci[0])
    ArrCfci = ArrConf.ArrowConfusion(G, testfci[0])

    #Adjacency and Arrowhead Stats
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

    #SHD calculation
    SHDfci = shd.SHD(G, testfci[0])

    fciStat.append(SHDfci.get_shd())

    return fciStat

def GESstats(G, testges):
    gesStat = []

    ACcges = AdjConf.AdjacencyConfusion(G, testges)
    ArrCges = ArrConf.ArrowConfusion(G, testges)

    #Adjacency and Arrowhead Stats
    gesStat.append(ACcges.get_adj_precision())
    gesStat.append(ACcges.get_adj_recall())
    gesStat.append(ArrCges.get_arrows_precision())
    gesStat.append(ArrCges.get_arrows_precision_ce())
    gesStat.append(ArrCges.get_arrows_recall())
    gesStat.append(ArrCges.get_arrows_recall_ce())
    gesStat.append(ACcges.get_adj_Mc())
    gesStat.append(ArrCges.get_arrows_Mc())
    gesStat.append(ACcges.get_adj_F1())
    gesStat.append(ArrCges.get_arrows_F1())

    #SHD calculation
    SHDges = shd.SHD(G, testges)

    gesStat.append(SHDges.get_shd())

    return gesStat

def average (stats):

    s = np.mean(stats, axis=0)

    return s

def STdev (stats):

    s = np.std(stats, axis=0)

    return s

def median (stats):

    s = np.median(stats, axis = 0)

    return s

def truncate (n, decimals=0):
    a = math.isnan(n)
    if a:
        return np.NaN
    else:
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier