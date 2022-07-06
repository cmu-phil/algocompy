from causallearn.search.ConstraintBased.FCI import fci
from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf

from causallearn.utils.cit import fisherz
from utils.SHD import SHD


def FCI(data, G):
    """
    Runs FCI algorithm with given data.
    Computes adjacency and Arrowhead confusion between estimated and true graph.
    Saves results into matrix.
    -----------
    data: sample data
    G: true graph
    """

    testfci = fci(data, fisherz, 0.01, verbose=False)

    fciPerformance = FCIstats(G, testfci)

    return fciPerformance


def FCIstats(G, testfci):
    fciStat = []

    # Adjacency and Arrowhead
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

    # SHD
    SHDfci = SHD(G, testfci[0])

    fciStat.append(SHDfci.get_shd())

    return fciStat
