from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf

import pandas as pd
import causalcmd.tetrad_cmd_algs as tc

from utils.SHD import SHD

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

    p = data.shape[1]

    X = []

    for q in range(1,p + 1):
        X.append('X' + str(q))

    print(X)

    pd.DataFrame(data, columns=X).to_csv("../PC-INPUT.txt", sep="\t", index=False)
    testpc = tc.pc("../PC-INPUT.txt", 0.01)

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
    SHDpc = SHD(G, testpc)

    pcStat.append(SHDpc.get_shd())

    return pcStat
