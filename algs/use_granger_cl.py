import numpy as np
from causallearn.search.Granger.Granger import Granger
from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf
from utils.SHD import SHD
from causallearn.utils.cit import kci

def granger (data, G):

    Grang = Granger()

    testgranger = Grang.granger_lasso(data)

    grangerperformance =GINstats(G, testgranger)

    return grangerperformance

def GINstats(G, testgranger):
    grangerStat = []

    # Adjacency and Arrowhead
    ACgranger = AdjConf.AdjacencyConfusion(G, testgranger)
    ArrCgranger = ArrConf.ArrowConfusion(G, testgranger)

    grangerStat.append(ACgranger.get_adj_precision())
    grangerStat.append(ACgranger.get_adj_recall())
    grangerStat.append(ArrCgranger.get_arrows_precision())
    grangerStat.append(ArrCgranger.get_arrows_precision_ce())
    grangerStat.append(ArrCgranger.get_arrows_recall())
    grangerStat.append(ArrCgranger.get_arrows_recall_ce())
    grangerStat.append(ACgranger.get_adj_Mc())
    grangerStat.append(ArrCgranger.get_arrows_Mc())
    grangerStat.append(ACgranger.get_adj_F1())
    grangerStat.append(ArrCgranger.get_arrows_F1())

    # SHD
    SHDgranger = SHD(G, testgranger)

    grangerStat.append(SHDgranger.get_shd())

    return grangerStat