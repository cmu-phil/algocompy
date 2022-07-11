import causalcmd.tetrad_cmd_algs as tc
import pandas as pd
from utils import my_statistics as stat


class use_fges_cc:
    def __init__(self, data, G):
        """
        Runs FGES algorithm with given data.
        Computes adjacency and Arrowhead confusion between estimated and true graph.
        Saves results into matrix.
        -----------
        data: sample data
        G: true graph
        """

        X = self.get_variable_names(data)

        pd.DataFrame(data, columns=X).to_csv("../PC-INPUT.txt", sep="\t", index=False)
        testfges = tc.fges("../PC-INPUT.txt", 2)

        self.fgesperformance = stat.stats(G, testfges)

    def get_variable_names(self, data):
        p = data.shape[1]
        X = []
        for q in range(1, p + 1):
            X.append('X' + str(q))
        # print(X)
        return X

    def get_performance(self):
        return self.fgesperformance

    def get_alg_name():
        return "FGES_CC"

class use_fges_cc:
    def __init__(self):
        """
        Runs PC algorithm with given data .
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
        return stat.stats(G, tc.fges("../PC-INPUT.txt", 2))

    def __str__(self):
        return "PC_CC"

    def get_variable_names(self, data):
        p = data.shape[1]
        X = []
        for q in range(1, p + 1):
            X.append('X' + str(q))
        # print(X)
        return X
