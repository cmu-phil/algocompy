import numpy as np
import math
from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf
from utils.SHD import SHD


def average (stats):

    s = np.mean(stats, axis=0)

    return s

def STdev (stats):

    s = np.std(stats, axis=0)

    return s

def median (stats):

    s = np.median(stats, axis = 0)

    return s

def worstCase (stats):

    s = np.amin(stats, axis=0)

    return s

def truncate (n, decimals):
    a = math.isnan(n)
    if a:
        return np.NaN
    else:
        string = ('.' + str(2) + 'f')
        n = format(n, string)
        return n
    
def chunk(arr, rep):
    for i in range(0, len(arr), rep):
        return arr[i: i + rep]

def stats(truegraph, estgraph):
    """
    Compares true graph and estimated graph with adjacency and arrowhead confusion.
    -----------
    truegraph: truth graph
    estgraph: estimated graph from algorithm
    -----------
    returns list of statistics
    """
    stat = []
    
    # Adjacency and Arrowhead
    adjc = AdjConf.AdjacencyConfusion(truegraph, estgraph)
    arrpc = ArrConf.ArrowConfusion(truegraph, estgraph)

    stat.append(adjc.get_adj_precision())
    stat.append(adjc.get_adj_recall())
    stat.append(arrpc.get_arrows_precision())
    stat.append(arrpc.get_arrows_precision_ce())
    stat.append(arrpc.get_arrows_recall())
    stat.append(arrpc.get_arrows_recall_ce())
    stat.append(adjc.get_adj_Mc())
    stat.append(arrpc.get_arrows_Mc())
    stat.append(adjc.get_adj_F1())
    stat.append(arrpc.get_arrows_F1())

    # SHD
    SHDpc = SHD(truegraph, estgraph)

    stat.append(SHDpc.get_shd())

    return stat