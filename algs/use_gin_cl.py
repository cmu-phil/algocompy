import numpy as np
from causallearn.search.HiddenCausal.GIN import GIN
from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf
from utils.SHD import SHD
from causallearn.utils.cit import kci

def gin (data, G):

    testgin = GIN.GIN(data, kci, 0.05)

    ginperformance =GINstats(G, testgin)

    return ginperformance

def GINstats(G, testgin):
    ginStat = []

    # Adjacency and Arrowhead
    ACgin = AdjConf.AdjacencyConfusion(G, testgin)
    ArrCgin = ArrConf.ArrowConfusion(G, testgin)

    ginStat.append(ACgin.get_adj_precision())
    ginStat.append(ACgin.get_adj_recall())
    ginStat.append(ArrCgin.get_arrows_precision())
    ginStat.append(ArrCgin.get_arrows_precision_ce())
    ginStat.append(ArrCgin.get_arrows_recall())
    ginStat.append(ArrCgin.get_arrows_recall_ce())
    ginStat.append(ACgin.get_adj_Mc())
    ginStat.append(ArrCgin.get_arrows_Mc())
    ginStat.append(ACgin.get_adj_F1())
    ginStat.append(ArrCgin.get_arrows_F1())

    # SHD
    SHDgin = SHD(G, testgin)

    ginStat.append(SHDgin.get_shd())

    return ginStat