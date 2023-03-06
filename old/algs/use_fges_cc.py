import old.causalcmd.tetrad_cmd_algs as tc
import pandas as pd
from old.utils import my_statistics as stat
import time

class use_fges_cc:
    def __init__(self):
        """
        Runs FGES algorithm with given data .
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
        start = time.time()
        testfges = tc.fges("../PC-INPUT.txt", 2)        
        finish = time.time()
        e_time = finish - start

        return stat.stats(G, testfges, e_time)

    def __str__(self):
        return "FGES_CC"

    def get_variable_names(self, data):
        p = data.shape[1]
        X = []
        for q in range(1, p + 1):
            X.append('X' + str(q))
        # print(X)
        return X
