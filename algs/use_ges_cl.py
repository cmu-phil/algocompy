from causallearn.search.ScoreBased.GES import ges
from utils import my_statistics as stat


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

        X = self.get_variable_names(data)

        maxP = 5
        parameters = {}
        # parameters["lambda_value"] = -2
        parameters["kfold"] = 5
        parameters["lambda"] = 0.01
        testges = ges(data, 'local_score_CV_general', maxP=maxP, parameters=parameters)['G']

        self.gesperformance = stat.stats(G, testges)

    def get_variable_names(self, data):
        p = data.shape[1]
        X = []
        for q in range(1, p + 1):
            X.append('X' + str(q))
        # print(X)
        return X

    def get_performance(self):
        return self.gesperformance

    def get_alg_name():
        return "GES_CL"