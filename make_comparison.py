from datetime import datetime
from algs import use_fci_cl, use_fges_cc, use_pc_cc, use_ges_cl, use_grasp_cc, use_pc_cl, use_pcmax_cc
from utils import my_statistics as stat
import numpy as np


class make_comparison:
    def __init__(self, reps, algs, results):

        with open("Comparison.txt", mode="w") as c:
            self.dateandtime(c)

            self.stat_info(c)

            self.sim_info(c)

            self.alg_info(c, algs)

            self.weight_info(c)

            self.average(c, reps, results)


    def dateandtime(self, c):
        dt = datetime.now()
        dt_string = dt.strftime("%d/%m/%Y %H:%M:%S")

        c.write(dt_string)
        c.write('\n' + '\n')

    def stat_info(self, c):
        c.write('Statistics:')
        c.write('\n' + '\n')
        c.write('AP = Adjacency Precision\n')
        c.write('AR = Adjacency Recall\n')
        c.write('AHP = Arrowhead Precicion\n')
        c.write('AHR = Arrowhead Recall\n')
        c.write('McAdj = Matthews correlation coefficient for adjacencies\n')
        c.write('McArrow = Matthews correlation coefficient for arrowheads\n')
        c.write('F1Adj = F1 statistics for adjacencies\n')
        c.write('F1Arrow = F1 statistics for arrowheads\n')
        c.write('SHD = Structural Hamming Distance\n')
        c.write('E = Elapsed time in secinds\n')
        c.write('\n')


    def sim_info(self, c):
        c.write('Simulation:')
        c.write('\n' + '\n')
        c.write('**Write info here**')
        c.write('\n' + '\n')


    def alg_info(self, c, algs):
        c.write('Algorithms:')
        c.write('\n' + '\n')
        
        for alg in algs:
            c.write( str(alg.get_id()) + '. ' + str(alg) + '\n')

        c.write('\n' + '\n')


    def weight_info(self, c):
        c.write('Weighting of Statistics:')
        c.write('\n' + '\n')
        c.write('**Write weighting here**')
        c.write('\n' + '\n')
    
    def average(self, c, reps, results):

        with open('averageTEST.txt', mode='w') as a:
            
            for alg in results:
                for sim in results[alg]:
                    for result in results[alg][sim]:
                        a.write(str(result) +'\n')
                        
        # g_stat = stat.average(est_g)
        # for i in g_stat:
        #     m = stat.truncate(i, 2)
        #     c.write('%s\t' % m)


    def st_dev(self, est_g, c):
        g_stat = stat.STdev(est_g)
        for i in g_stat:
            m = stat.truncate(i, 2)
            c.write('%s\t' % m)


    def worst_case(self, est_g, c):
        g_stat = stat.worstCase(est_g)
        for i in g_stat:
            m = stat.truncate(i, 2)
            c.write('%s\t' % m)


    def median_case(self, est_g, c):
        g_stat = stat.median(est_g)
        for i in g_stat:
            m = stat.truncate(i, 2)
            c.write('%s\t' % m)
