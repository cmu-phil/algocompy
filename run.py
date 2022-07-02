from algs import use_pc, use_pc_cc, use_grasp_cc
from utils import true_graph as TG, random_sample as sampler
import makefile as mf

def run():
    p = 20
    a = 4
    d = a / (p - 1)
    N = 1000
    runnum = 10
    randomdata = True

    EstG1 = []
    EstG2 = []
    EstG3 = []

    if randomdata == True:
        for i in range(runnum):
            print("run number:", i+1)

            data, g = sampler.sample(p, d, N)

            # G0 = TG.TrueGraph(g, p, 0)
            G1 = TG.TrueGraph(g, p, 1)

            pcPerformance = use_pc.PC(data, G1)
            EstG1.append(pcPerformance)

            fciperformance = use_pc_cc.PC(data, G1)
            EstG2.append(fciperformance)

            # gesperformance = use_GES.GES(data, G0)
            # EstG3.append(gesperformance)

            gesperformance = use_grasp_cc.GRASP(data, G1)
            EstG3.append(gesperformance)

            i += 1
    #else:

    
    # np.savetxt('PC-OUTPUT.txt', PC, delimiter = '\t')
    # np.savetxt('FCI-OUTPUT.txt', FCI, delimiter = '\t')
    # np.savetxt('GES-OUTPUT.txt', GES, delimiter = '\t')

    mf.makefile(EstG1, EstG2, EstG3)

    print("------------------")
    print("------finish------")
    print("------------------")


if __name__ == "__main__":
    run()