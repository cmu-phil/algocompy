from algs import use_pc, use_pc_cc, use_grasp_cc, use_fges_cc
from utils import true_graph as TG, random_sample as sampler
import makefile as mf

def run():
    p = 20
    a = 4
    d = a / (p - 1)
    N = 1000
    runnum = 10
    random_data = True

    est_g1 = []
    est_g2 = []
    est_g3 = []
    est_g4 = []

    if random_data == True:
        for i in range(runnum):
            print("run number:", i+1)

            data, g = sampler.sample(p, d, N)

            # G0 = TG.TrueGraph(g, p, 0)
            G1 = TG.TrueGraph(g, p, 1)

            pc_performance = use_pc.PC(data, G1)
            est_g1.append(pc_performance)

            pc_cc_performance = use_pc_cc.PC(data, G1)
            est_g2.append(pc_cc_performance)

            # gesperformance = use_GES.GES(data, G0)
            # EstG3.append(gesperformance)

            fges_cc_performance = use_fges_cc.FGES(data, G1)
            est_g3.append(fges_cc_performance)

            grasp_cc_performance = use_grasp_cc.GRASP(data, G1)
            est_g4.append(grasp_cc_performance)

            i += 1
    #else:

    
    # np.savetxt('PC-OUTPUT.txt', PC, delimiter = '\t')
    # np.savetxt('FCI-OUTPUT.txt', FCI, delimiter = '\t')
    # np.savetxt('GES-OUTPUT.txt', GES, delimiter = '\t')

    mf.make_file(est_g1, est_g2, est_g3, est_g4)

    print("------------------")
    print("------finish------")
    print("------------------")


if __name__ == "__main__":
    run()