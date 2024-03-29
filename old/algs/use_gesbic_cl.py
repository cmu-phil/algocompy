from causallearn.search.ScoreBased.GES import ges
from old.utils import my_statistics as stat
import time


class use_gesbic_cl:
    def __init__(self):
        """
        Runs GES algorithm with given data.
        Computes adjacency and Arrowhead confusion between estimated and true graph.
        Saves results into matrix.
        -----------
        data: sample data
        G: true graph
        """

    def run(self, data, G):
        maxP = 5
        parameters = {}
        parameters["lambda_value"] = 2
        parameters["kfold"] = 5
        parameters["lambda"] = 0.01

        start = time.time()
        testges = ges(data, 'local_score_BIC', maxP=maxP, parameters=parameters)['G']
        finish = time.time()
        e_time = finish - start

        return stat.stats(G, testges, e_time)

    def __str__(self):
        return "GESBIC_CL"