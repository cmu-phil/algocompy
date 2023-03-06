from algs.use_pc_cc import use_pc_cc
import make_comparison as mc
from algs import task, use_fci_cl, use_fges_cc, use_gesbic_cl, use_pc_cc, use_grasp_cc, use_pc_cl, use_pcmax_cc
from utils import true_graph as tg, random_sample as sampler
import numpy as np
import pickle
import time
from utils import my_statistics as st

def run():
    reps = 10

    num_var = [10, 20]
    avg_deg = [2, 4]
    num_samp = [1000, 10000]

    save_data = False

    start = time.time()

    algs = []
    algs.append(task.task(use_pc_cl.use_pc_cl(), 1))
    algs.append(task.task(use_pc_cc.use_pc_cc(), 2))
    algs.append(task.task(use_pcmax_cc.use_pcmax_cc(), 3))
    algs.append(task.task(use_fges_cc.use_fges_cc(), 4))
    algs.append(task.task(use_fci_cl.use_fci_cl(), 5))
    algs.append(task.task(use_grasp_cc.use_grasp_cc(), 6))
    algs.append(task.task(use_gesbic_cl.use_gesbic_cl(), 7))
    # algs.append(task.task(use_gescv_cl.use_gescv_cl(), 8))


    results = {}
    for alg in algs:
        results[alg.get_id()] = {}

    for p in num_var:
        for a in avg_deg:
            d = a / (p - 1)
            for n in num_samp:
                for rep in range(reps):
                    print("------------------")
                    print("run number: ", rep+1)
                    print("------------------")
                    count = rep + 1
                    data, g = sampler.sample(p, d, n)
                    if save_data == True:
                        np.savetxt(str(count) + '_sample.txt', data, delimiter = '\t')
                    g1 = tg.TrueGraph(g, p, 1)
                    g0 = tg.TrueGraph(g, p, 0)
                    for alg in algs:
                        key = (p,a,n)
                        if rep == 0: results[alg.get_id()][key] = []
                        if alg.get_id() >= 7:
                            results[alg.get_id()][key].append(alg.run(data, g0))
                        else:
                            results[alg.get_id()][key].append(alg.run(data, g1))


    with open('results.p', mode='wb') as f:
        pickle.dump(results, f)

    # with open('results.p', mode='rb') as f:
    #     results = pickle.load(f)

    with open('results.txt', mode='w') as r:

        for alg in results:
            for sim in results[alg]:
                for result in results[alg][sim]:
                    r.write(str(alg) + '\t' + str(sim) + '\t' + str(result) + '\n')


    mc.make_comparison(algs, results, reps, num_var, avg_deg, num_samp)

    finish = time.time()
    total_time = finish - start
    total_time = st.truncate(total_time, 2)

    print("------------------")
    print("------finish------")
    print("------------------")
    print("Total time: ", total_time)
    print("------------------")


if __name__ == "__main__":
    run()
