from causallearn.search.ConstraintBased.FCI import fci
from causallearn.utils.cit import fisherz
from utils import my_statistics as stat


class use_fci_cl:
    def __init__(self):
        """
        Runs FCI algorithm with given data.
        Computes adjacency and Arrowhead confusion between estimated and true graph.
        Saves results into matrix.
        """

        self.alpha = 0.01


    def run(self, data, G): 
        # data : dataset
        # G    : true graph
        return stat.stats(G, fci(data, fisherz, 0.01, verbose=False)[0])

    def __str__(self):
        return "FCI_CL"