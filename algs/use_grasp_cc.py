from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf

import causalcmd.tetrad_cmd_algs as tc
import pandas as pd

from utils.SHD import SHD


def GRASP(data, G):
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

    pd.DataFrame(data, columns=X).to_csv("../GRaSP-INPUT.txt", sep="\t", index=False)
    testgrasp = tc.grasp("../GRaSP-INPUT.txt", 2)

    graspPerformance = GRaSPstats(G, testgrasp)

    return graspPerformance


def GRaSPstats(G, testgrasp):
    graspStat = []

    # Adjacency and Arrowhead
    ACgrasp = AdjConf.AdjacencyConfusion(G, testgrasp)
    ArrCgrasp = ArrConf.ArrowConfusion(G, testgrasp)

    graspStat.append(ACgrasp.get_adj_precision())
    graspStat.append(ACgrasp.get_adj_recall())
    graspStat.append(ArrCgrasp.get_arrows_precision())
    graspStat.append(ArrCgrasp.get_arrows_precision_ce())
    graspStat.append(ArrCgrasp.get_arrows_recall())
    graspStat.append(ArrCgrasp.get_arrows_recall_ce())
    graspStat.append(ACgrasp.get_adj_Mc())
    graspStat.append(ArrCgrasp.get_arrows_Mc())
    graspStat.append(ACgrasp.get_adj_F1())
    graspStat.append(ArrCgrasp.get_arrows_F1())

    # SHD
    SHDgrasp = SHD(G, testgrasp)

    graspStat.append(SHDgrasp.get_shd())

    return graspStat
