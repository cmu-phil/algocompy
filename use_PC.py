from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import SHD as shd
import myStatistics as stat

def PC(data, G):
    """
    Runs PC algorithm with given data.
    Computes adjacency and Arrowhead confusion between estimated and true graph.
    Saves results into matrix.
    -----------
    data: sample data
    G: true graph
    """

    testpc = pc(data, 0.01, fisherz, True, 0, -1)

    pcPerformance = PCstats(G, testpc.G)

    return pcPerformance


def PCstats(G, testpc):
    pcStat = []

    # Adjacency and Arrowhead
    ACpc = AdjConf.AdjacencyConfusion(G, testpc)
    ArrCpc = ArrConf.ArrowConfusion(G, testpc)

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

    # SHD
    SHDpc = shd.SHD(G, testpc)

    pcStat.append(SHDpc.get_shd())

    return pcStat

# def PC_average(PC, c):
#     pcStat = stat.average(PC)
#     for i in pcStat:
#         m = stat.truncate(i, 2)
#         c.write('%s\t' % m)

# def PC_stDev(PC, c):
#     pcStat = stat.STdev(PC)
#     for i in pcStat:
#         m = stat.truncate(i, 2)
#         c.write('%s\t' % m)

# def PC_worstCase(PC, c):
#     pcStat = stat.worstCase(PC)
#     for i in pcStat:
#         m = stat.truncate(i, 2)
#         c.write('%s\t' % m)

# def PC_medianCase(PC, c):
#     pcStat = stat.median(PC)
#     for i in pcStat:
#         m = stat.truncate(i, 2)
#         c.write('%s\t' % m)