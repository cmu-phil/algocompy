from datetime import datetime
from utils import my_statistics as stat
import numpy as np
import math

class make_comparison:
    def __init__(self, algs, results, reps, num_var, avg_deg, num_samp):

        with open("Comparison.txt", mode="w") as c:
            self.dateandtime(c)

            self.stat_info(c)

            self.sim_info(c, reps, num_var, avg_deg, num_samp)

            self.alg_info(c, algs)

            self.average(c, results)

            self.st_dev(c, results)

            self.worst_case(c, results)

            self.median_case(c, results)


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


    def sim_info(self, c, reps, num_var, avg_deg, num_samp):
        c.write('Simulation:')
        c.write('\n' + '\n')
        c.write('reps: ' + str(reps) + '\n')
        c.write('number of variables: ' + str(num_var) + '\n')
        c.write('average degree: ' + str(avg_deg) + '\n')
        c.write('rnumber of samples: ' + str(num_samp) + '\n')
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


    def average(self, c, results):

        c.write("Average:\n\n")

        c.write('\tAlg   AP     AR     AHP    AHPC   AHR    AHRC   McAdj  McArr  F1Adj  F1Arr  SHD    E\n')
        
        for alg in results:
            for sim in results[alg]:
                c.write('\t' + str(alg) + '     ')
                temp = np.array(results[alg][sim])
                avg = np.mean(temp, 0)
                for i in avg:
                    check = math.isnan(i)
                    if check:
                        c.write("nan    ")
                    else:
                        c.write(str(stat.truncate(i, 2)) + "   ")  
                c.write('\n')
        c.write('\n')


    def st_dev(self, c, results):
        c.write("Standard Deviation:\n\n")

        c.write('\tAlg   AP     AR     AHP    AHPC   AHR    AHRC   McAdj  McArr  F1Adj  F1Arr  SHD    E\n')
        
        for alg in results:
            for sim in results[alg]:
                c.write('\t' + str(alg) + '     ')
                temp = np.array(results[alg][sim])
                avg = np.std(temp, 0)
                for i in avg:
                    check = math.isnan(i)
                    if check:
                        c.write("nan    ")
                    else:
                        c.write(str(stat.truncate(i, 2)) + "   ")  
                c.write('\n')
        c.write('\n')


    def worst_case(self, c, results):
        c.write("Worst Case:\n\n")

        c.write('\tAlg   AP     AR     AHP    AHPC   AHR    AHRC   McAdj  McArr  F1Adj  F1Arr  SHD    E\n')
        
        for alg in results:
            for sim in results[alg]:
                c.write('\t' + str(alg) + '     ')
                temp = np.array(results[alg][sim])
                avg = np.amin(temp, 0)
                for i in avg:
                    check = math.isnan(i)
                    if check:
                        c.write("nan    ")
                    else:
                        c.write(str(stat.truncate(i, 2)) + "   ")  
                c.write('\n')
        c.write('\n')


    def median_case(self, c, results):
        c.write("Median Case:\n\n")

        c.write('\tAlg   AP     AR     AHP    AHPC   AHR    AHRC   McAdj  McArr  F1Adj  F1Arr  SHD    E\n')
        
        for alg in results:
            for sim in results[alg]:
                c.write('\t' + str(alg) + '     ')
                temp = np.array(results[alg][sim])
                avg = np.median(temp, 0)
                for i in avg:
                    check = math.isnan(i)
                    if check:
                        c.write("nan    ")
                    else:
                        c.write(str(stat.truncate(i, 2)) + "   ")  
                c.write('\n')
        c.write('\n')
