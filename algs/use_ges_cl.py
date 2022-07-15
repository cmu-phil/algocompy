from causallearn.search.ScoreBased.GES import ges
from utils import my_statistics as stat
import time


class use_ges_cl:
    def __init__(self, data, G):
        """
        Runs GES algorithm with given data.
        Computes adjacency and Arrowhead confusion between estimated and true graph.
        Saves results into matrix.
        -----------
        data: sample data
        G: true graph
        """

        maxP = 5
        parameters = {}
        # parameters["lambda_value"] = -2
        parameters["kfold"] = 5
        parameters["lambda"] = 0.01

        start = time.time()
        testges = ges(data, 'local_score_CV_general', maxP=maxP, parameters=parameters)['G']
        finish = time.time()
        e_time = finish - start

        return stat.stats(G, testges, e_time)

    def get_alg_name():
        return "GES_CL"