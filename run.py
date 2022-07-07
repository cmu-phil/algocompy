from matplotlib.style import use
from algs.use_pc_cc import use_pc_cc
import make_file as mf
from algs import use_fci_cl, use_fges_cc, use_pc_cc, use_ges_cl, use_grasp_cc, use_pc_cl, use_pcmax_cc, use_granger_cl
from utils import true_graph as tg, random_sample as sampler

def run():
    p = 10
    a = 4
    d = a / (p - 1)
    n = 500
    runnum = 5
    random_data = True

    est_g1 = []
    est_g2 = []
    est_g3 = []
    est_g4 = []
    est_g5 = []
    est_g6 = []
    est_g7 = []
    est_g8 = []

    if random_data:
        for i in range(runnum):
            print("run number:", i + 1)

            data, g = sampler.sample(p, d, n)

            g0 = tg.TrueGraph(g, p, 0)
            g1 = tg.TrueGraph(g, p, 1)

            pc_performance = use_pc_cl.PC(data, g1)
            est_g1.append(pc_performance)

            pc_cc_performance = use_pc_cc.use_pc_cc(data, g1).get_performance()
            est_g2.append(pc_cc_performance)

            pc_max_cc_performance = use_pcmax_cc.PCMAX(data, g1, True)
            est_g3.append(pc_max_cc_performance)

            # gesperformance = use_ges_cl.GES(data, g0)
            # est_g4.append(gesperformance)

            grangerperformance = use_granger_cl.granger(data, g1)
            est_g4.append(grangerperformance)

            fges_cc_performance = use_fges_cc.FGES(data, g1)
            est_g5.append(fges_cc_performance)

            fci_cl_performance = use_fci_cl.FCI(data, g1)
            est_g6.append(fci_cl_performance)

            grasp_cc_performance = use_grasp_cc.GRASP(data, g1)
            est_g7.append(grasp_cc_performance)

            i += 1

    # np.savetxt('PC-OUTPUT.txt', PC, delimiter = '\t')
    # np.savetxt('FCI-OUTPUT.txt', FCI, delimiter = '\t')
    # np.savetxt('GES-OUTPUT.txt', GES, delimiter = '\t')

    mf.make_file(est_g1, est_g2, est_g3, est_g4, est_g5, est_g6, est_g7)

    print("------------------")
    print("------finish------")
    print("------------------")


if __name__ == "__main__":
    run()
