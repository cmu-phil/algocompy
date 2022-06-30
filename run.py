# files withing the project
import constants as const
import RandomSample as sampler
import TrueGraph as TG
import myStatistics as Stat
import MakeResults as MR

# useful python libraries
import numpy as np

# causal-learn package
import causallearn as cl

from causallearn.search.ConstraintBased.PC import pc
from causallearn.search.ConstraintBased.FCI import fci
from causallearn.search.ScoreBased.GES import ges
#from causallearn.search.ConstraintBased.CDNOD import cdnod
#from causallearn.search.PermutationBased.GRaSP import grasp
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz

from causallearn.utils.DAG2CPDAG import dag2cpdag

def run():

    PC = []
    FCI = []
    GES = []

    runnum = const.runnum
    for i in range(runnum):
        print('run number:', i+1)
        # Generating random samples
        data, g = sampler.sample(const.p, const.d, const.N)
        #print(data)

        # True Graph
        G0 = TG.makeTrueGraph_0(g)
        G1 = TG.makeTrueGraph_1(g)

        print("---------------------------------------")
        
        # Algorythims
        testpc = pc(data, 0.01, fisherz, True, 0, -1 )
        print("---------------------------------------")

        testfci = fci(data, fisherz, 0.01, verbose=False)
        print("---------------------------------------")
        
        #c_indx = np.reshape(np.asarray(list(range(data.shape[0]))), (data.shape[0],1))
        #print(c_indx)
        #testcdnod = cdnod(data, c_indx, const.d, kci, True, 0, -1)
        maxP = 5
        parameters = {}
        # parameters["lambda_value"] = -2
        parameters["kfold"] = 5
        parameters["lambda"] = 0.01
        testges = ges(data, 'local_score_CV_general', maxP=maxP, parameters=parameters)['G']
        
        print(testges)

        print("---------------------------------------")

        # testgrasp = grasp.grasp()

        pcPerformance = Stat.PCstats (G1, testpc.G)
        PC.append(pcPerformance)
        
        fciPerformance = Stat.FCIstats (G1, testfci)
        FCI.append(fciPerformance)

        gesPerformance = Stat.GESstats (G0, testges)
        GES.append(gesPerformance)

        i += 1

    np.savetxt('PC-OUTPUT.txt', PC, delimiter = '\t')
    np.savetxt('FCI-OUTPUT.txt', FCI, delimiter = '\t')
    np.savetxt('GES-OUTPUT.txt', GES, delimiter = '\t')

    MR.makefile(PC, FCI, GES)

    print("finish")

if __name__ == "__main__":
    run()