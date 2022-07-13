from os import stat
from xml.etree.ElementTree import tostring
from matplotlib.style import use
from algs.use_pc_cc import use_pc_cc
import make_comparison as mc
from algs import task, use_fci_cl, use_fges_cc, use_pc_cc, use_ges_cl, use_grasp_cc, use_pc_cl, use_pcmax_cc
from utils import true_graph as tg, random_sample as sampler
import numpy as np
from utils import my_statistics as stat

def run():
    reps = 2

    num_var = [10, 20]
    avg_deg = [2, 4]
    num_samp = [1000, 10000]

    save_data = False

    algs = []
    algs.append(task.task(use_pc_cl.use_pc_cl(), 1))
    algs.append(task.task(use_pc_cc.use_pc_cc(), 2))
    algs.append(task.task(use_pcmax_cc.use_pcmax_cc(), 3))
    algs.append(task.task(use_fges_cc.use_fges_cc(), 4))
    algs.append(task.task(use_fci_cl.use_fci_cl(), 5))
    algs.append(task.task(use_grasp_cc.use_grasp_cc(), 6))


    results = {}
    for alg in algs:
        results[alg.get_id()] = {}

    for p in num_var:
        for a in avg_deg:
            d = a / (p - 1)
            for n in num_samp:
                for rep in range(reps):
                    data, g = sampler.sample(p, d, n)
                    if save_data == True:
                        np.savetxt(str() + '_sample.txt', data, delimiter = '\t')
                    g1 = tg.TrueGraph(g, p, 1)
                    for alg in algs:
                        key = (p,a,n)
                        if rep == 0: results[alg.get_id()][key] = []
                        results[alg.get_id()][key].append(alg.run(data, g1))



    mc.make_comparison(results, algs)


    with open('results.txt', mode='w') as f:

        for alg in results:
            for sim in results[alg]:
                for result in results[alg][sim]:
                    f.write(str(alg) + '\t' + str(sim) + '\t' + str(result) + '\n')




    print("------------------")
    print("------finish------")
    print("------------------")


if __name__ == "__main__":
    run()
