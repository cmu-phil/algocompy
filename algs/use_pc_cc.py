from utils import AdjacencyConfusion as AdjConf, ArrowConfusion as ArrConf

import pandas as pd
import causalcmd.tetrad_cmd_algs as tc

from utils.SHD import SHD

class use_pc_cc:
    def __init__(self, data, true_graph):
        """
        Runs PC algorithm with given data .
        Computes adjacency and Arrowhead confusion between estimated and true graph.
        Saves results into matrix.
        -----------
        data: sample data
        G: true graph
        """
        X = self.get_variable_names(data)

        pd.DataFrame(data, columns=X).to_csv("../PC-INPUT.txt", sep="\t", index=False)
        est_grap = tc.pc("../PC-INPUT.txt", 0.01)

        self.pc_performance = self.stats(true_graph, est_grap)

    def get_variable_names(self, data):
        p = data.shape[1]
        X = []
        for q in range(1, p + 1):
            X.append('X' + str(q))
        print(X)
        return X

    def get_performance(self):
        return self.pc_performance

    def get_alg_name(self):
        return "PC_CL"

    def stats(self, g_true, g_est):
        stats = []

        # Adjacency and Arrowhead
        ACpc = AdjConf.AdjacencyConfusion(g_true, g_est)
        ArrCpc = ArrConf.ArrowConfusion(g_true, g_est)

        stats.append(ACpc.get_adj_precision())
        stats.append(ACpc.get_adj_recall())
        stats.append(ArrCpc.get_arrows_precision())
        stats.append(ArrCpc.get_arrows_precision_ce())
        stats.append(ArrCpc.get_arrows_recall())
        stats.append(ArrCpc.get_arrows_recall_ce())
        stats.append(ACpc.get_adj_Mc())
        stats.append(ArrCpc.get_arrows_Mc())
        stats.append(ACpc.get_adj_F1())
        stats.append(ArrCpc.get_arrows_F1())

        # SHD
        _shd = SHD(g_true, g_est)

        stats.append(_shd.get_shd())

        return stats
