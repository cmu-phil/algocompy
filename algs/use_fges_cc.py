from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf

import causalcmd.tetrad_cmd_algs as tc
import pandas as pd
from utils.SHD import SHD

def FGES(data, G):
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
    testfges = tc.fges("../PC-INPUT.txt", 2)

    pcPerformance = FGESstats(G, testfges)

    return pcPerformance


def FGESstats(G, testfges):
    fgesStat = []

    # Adjacency and Arrowhead
    ACfges = AdjConf.AdjacencyConfusion(G, testfges)
    ArrCfges = ArrConf.ArrowConfusion(G, testfges)

    fgesStat.append(ACfges.get_adj_precision())
    fgesStat.append(ACfges.get_adj_recall())
    fgesStat.append(ArrCfges.get_arrows_precision())
    fgesStat.append(ArrCfges.get_arrows_precision_ce())
    fgesStat.append(ArrCfges.get_arrows_recall())
    fgesStat.append(ArrCfges.get_arrows_recall_ce())
    fgesStat.append(ACfges.get_adj_Mc())
    fgesStat.append(ArrCfges.get_arrows_Mc())
    fgesStat.append(ACfges.get_adj_F1())
    fgesStat.append(ArrCfges.get_arrows_F1())

    # SHD
    SHDfges = SHD(G, testfges)

    fgesStat.append(SHDfges.get_shd())

    return fgesStat
