from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import SHD as shd
import myStatistics as stat

import tetrad_cmd_algs as tc
import pandas as pd

def PC(data, G):
    """
    Runs PC algorithm with given data.
    Computes adjacency and Arrowhead confusion between estimated and true graph.
    Saves results into matrix.
    -----------
    data: sample data
    G: true graph
    """

    # testpc = pc(data, 0.01, fisherz, True, 0, -1).G

    pd.DataFrame(data, columns=G.get_node_names()).to_csv("PC-INPUT.txt", sep="\t", index=False)
    testpc = tc.pc("./PC-INPUT.txt", 0.01)

    pcPerformance = PCstats(G, testpc)

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
