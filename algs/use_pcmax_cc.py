from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf

import pandas as pd
import causalcmd.tetrad_cmd_algs as tc

from utils.SHD import SHD

def PCMAX(data, G, max):
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
    testpcmax = tc.pcmax("../PC-INPUT.txt", 0.01)

    pcmaxPerformance = PCMAXstats(G, testpcmax)

    return pcmaxPerformance


def PCMAXstats(G, testpcmax):
    pcmaxStat = []

    # Adjacency and Arrowhead
    ACpc = AdjConf.AdjacencyConfusion(G, testpcmax)
    ArrCpc = ArrConf.ArrowConfusion(G, testpcmax)

    pcmaxStat.append(ACpc.get_adj_precision())
    pcmaxStat.append(ACpc.get_adj_recall())
    pcmaxStat.append(ArrCpc.get_arrows_precision())
    pcmaxStat.append(ArrCpc.get_arrows_precision_ce())
    pcmaxStat.append(ArrCpc.get_arrows_recall())
    pcmaxStat.append(ArrCpc.get_arrows_recall_ce())
    pcmaxStat.append(ACpc.get_adj_Mc())
    pcmaxStat.append(ArrCpc.get_arrows_Mc())
    pcmaxStat.append(ACpc.get_adj_F1())
    pcmaxStat.append(ArrCpc.get_arrows_F1())

    # SHD
    SHDpc = SHD(G, testpcmax)

    pcmaxStat.append(SHDpc.get_shd())

    return pcmaxStat
