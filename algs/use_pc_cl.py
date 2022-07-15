from causallearn.search.ConstraintBased.PC import pc
from causallearn.utils.cit import fisherz
from utils import my_statistics as stat
import time

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
        start = time.time()
        testpc_cl = pc(data, self.alpha, fisherz, True, 0, -1).G
        finish = time.time()
        e_time = finish - start
        return stat.stats(G, testpc_cl, e_time)

    def __str__(self):
        return "PC_CL"
