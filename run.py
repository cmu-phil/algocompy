import make_file as mf
from algs import use_pc_cl, use_pc_cc, use_grasp_cc, use_fges_cc, use_pcmax_cc
from utils import true_graph as tg, random_sample as sampler


def run():
    p = 20
    a = 4
    d = a / (p - 1)
    n = 1000
    runnum = 10
    random_data = True

    est_g1 = []
    est_g2 = []
    est_g3 = []
    est_g4 = []
    est_g5 = []

    if random_data:
        for i in range(runnum):
            print("run number:", i + 1)

            data, g = sampler.sample(p, d, n)

            # G0 = TG.TrueGraph(g, p, 0)
            g1 = tg.TrueGraph(g, p, 1)

            pc_performance = use_pc_cl.PC(data, g1)
            est_g1.append(pc_performance)

            pc_cc_performance = use_pc_cc.PC(data, g1)
            est_g2.append(pc_cc_performance)

            pc_max_cc_performance = use_pcmax_cc.PCMAX(data, g1, True)
            est_g3.append(pc_max_cc_performance)

            # gesperformance = use_ges_cl.GES(data, G0)
            # EstG3.append(gesperformance)

            fges_cc_performance = use_fges_cc.FGES(data, g1)
            est_g4.append(fges_cc_performance)

            grasp_cc_performance = use_grasp_cc.GRASP(data, g1)
            est_g5.append(grasp_cc_performance)

            i += 1
    # else:

    # np.savetxt('PC-OUTPUT.txt', PC, delimiter = '\t')
    # np.savetxt('FCI-OUTPUT.txt', FCI, delimiter = '\t')
    # np.savetxt('GES-OUTPUT.txt', GES, delimiter = '\t')

    mf.make_file(est_g1, est_g2, est_g3, est_g4, est_g5)

    print("------------------")
    print("------finish------")
    print("------------------")


if __name__ == "__main__":
    run()
