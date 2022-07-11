import pandas as pd
import causalcmd.tetrad_cmd_algs as tc

from utils import my_statistics as stat


class use_pcmax_cc:
    def __init__(self):
        """
        Runs PCMAX algorithm with given data .
        Computes adjacency and Arrowhead confusion between estimated and true graph.
        Saves results into matrix.
        -----------
        data: sample data
        G: true graph
        """

        self.alpha = 0.01


    def run(self, data, G): 
        # data : dataset
        # G    : true graph
        X = self.get_variable_names(data)
        pd.DataFrame(data, columns=X).to_csv("../PC-INPUT.txt", sep="\t", index=False)
        return stat.stats(G, tc.pcmax("../PC-INPUT.txt", self.alpha))

    def __str__(self):
        return "PCMAX_CC"

    def get_variable_names(self, data):
        p = data.shape[1]
        X = []
        for q in range(1, p + 1):
            X.append('X' + str(q))
        # print(X)
        return X