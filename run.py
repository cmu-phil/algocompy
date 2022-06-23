# files withing the project
import constants as const
import RandomSample as sampler
import TrueGraph as TG
import Statistics as Stat
import MakeResults as MR

# useful python libraries
import numpy as np

# causal-learn package
import causallearn as cl

from causallearn.search.ConstraintBased.PC import pc
from causallearn.search.ConstraintBased.FCI import fci
from causallearn.search.ConstraintBased.CDNOD import cdnod
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz

def run():

    PC = []
    FCI = []
    CDNOD = []

    runnum = const.runnum
    for i in range(runnum):
        print('run number:', i)
        # Generating random samples
        data, g = sampler.sample(const.p, const.d, const.N)
        #print(data)

        # True Graph
        G = TG.makeTrueGraph(g)

        # Algorythims
        testpc = pc(data, const.d, gsq, True, 0, -1 )
        print("---------------------------------------")

        testfci = fci(data, fisherz, const.d, verbose=False)
        print("---------------------------------------")
        
        c_indx = np.reshape(np.asarray(list(range(data.shape[0]))), (data.shape[0],1))
        #print(c_indx)
        testcdnod = cdnod(data, c_indx, const.d, kci, True, 0, -1)
        print("---------------------------------------")


        pcPerformance = Stat.PCstats (G, testpc.G)
        PC.append(pcPerformance)
        
        fciPerformance = Stat.FCIstats (G, testfci)
        FCI.append(fciPerformance)

        cdnodPerformance = Stat.CDNODstats (G, testcdnod.G)
        CDNOD.append(cdnodPerformance)

        i += 1

    np.savetxt('PC-OUTPUT.txt', PC, delimiter = '\t')
    np.savetxt('FCI-OUTPUT.txt', FCI, delimiter = '\t')
    np.savetxt('CDNOD-OUTPUT.txt', CDNOD, delimiter = '\t')
    #MR.makefile(pcStat, fciStat, cdnodStat)


    print("finish")


if __name__ == "__main__":
    run()