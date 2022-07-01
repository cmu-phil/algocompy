import randomSample as sampler
import truegraph as TG
import use_PC
import use_FCI
import use_GES
import makefile as mf
import tetrad_cmd_algs as tca

def run():
    p = 10
    d = 0.25
    N = 500
    runnum = 10
    randomdata = True

    EstG1 = []
    EstG2 = []
    EstG3 = []

    if randomdata == True:
        for i in range(runnum):
            print("run number:", i+1)

            data, g = sampler.sample(p, d, N)

            G0 = TG.TrueGraph(g, p, 0)
            G1 = TG.TrueGraph(g, p, 1)

            pcPerformance = use_PC.PC(data, G1)
            EstG1.append(pcPerformance)

            fciperformance = use_FCI.FCI(data, G1)
            EstG2.append(fciperformance)

            # gesperformance = use_GES.GES(data, G0)
            # EstG3.append(gesperformance)

            i += 1
    #else:

    
    # np.savetxt('PC-OUTPUT.txt', PC, delimiter = '\t')
    # np.savetxt('FCI-OUTPUT.txt', FCI, delimiter = '\t')
    # np.savetxt('GES-OUTPUT.txt', GES, delimiter = '\t')

    mf.makefile(EstG1, EstG2)

    print("------------------")
    print("------finish------")
    print("------------------")


if __name__ == "__main__":
    run()