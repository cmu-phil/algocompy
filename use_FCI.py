from causallearn.search.ConstraintBased.FCI import fci
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import SHD as shd
import myStatistics as stat


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
    SHDfci = shd.SHD(G, testfci[0])

    fciStat.append(SHDfci.get_shd())

    return fciStat

def FCI_average(FCI, c):
    pcStat = stat.average(FCI)
    for i in pcStat:
        m = stat.truncate(i, 2)
        c.write('%s\t' % m)

def FCI_stDev(FCI, c):
    pcStat = stat.STdev(FCI)
    for i in pcStat:
        m = stat.truncate(i, 2)
        c.write('%s\t' % m)

def FCI_worstCase(FCI, c):
    pcStat = stat.worstCase(FCI)
    for i in pcStat:
        m = stat.truncate(i, 2)
        c.write('%s\t' % m)

def FCI_medianCase(FCI, c):
    pcStat = stat.median(FCI)
    for i in pcStat:
        m = stat.truncate(i, 2)
        c.write('%s\t' % m)