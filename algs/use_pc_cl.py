from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import fisherz
from utils import my_statistics as stat

class use_pc_cl:
    def __init__(self):
        """
        Runs PC algorithm with given data.
        Computes adjacency and Arrowhead confusion between estimated and true graph.
        Saves results into matrix.
        """

        self.alpha = 0.01


    def run(self, data, G): 
        # data : dataset
        # G    : true graph
        return stat.stats(G, pc(data, self.alpha, fisherz, True, 0, -1).G)

    def __str__(self):
        return "PC_CL"
