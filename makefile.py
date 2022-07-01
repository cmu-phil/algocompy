from datetime import datetime
import use_PC
import use_FCI
import use_GES



def makefile (PC, FCI, GES):
    with open("Comparison.txt", mode = "w") as c:

        dateandtime(c)

        statInfo(c)

        simInfo(c)

        algInfo(c)

        weightInfo(c)

        c.write("AVERAGE STATISTICS:")

        tableHeader(c)
        c.write('\n' + '\t')
        c.write('1' + '\t')
        use_PC.PC_average(PC, c)
        c.write('\n' + '\t')
        c.write('2' + '\t')
        use_FCI.FCI_average(FCI, c)
        c.write('\n' + '\t')
        c.write('3' + '\t')
        use_FCI.FCI_average(GES, c)

        c.write('\n' + '\n')
        c.write("STANDARD DEVIATION:")

        tableHeader(c)
        c.write('\n' + '\t')
        c.write('1' + '\t')
        use_PC.PC_stDev(PC, c)
        c.write('\n' + '\t')
        c.write('2' + '\t')
        use_FCI.FCI_stDev(FCI, c)
        c.write('\n' + '\t')
        c.write('3' + '\t')
        use_FCI.FCI_stDev(GES, c)

        c.write('\n' + '\n')
        c.write("WORST CASE:")

        tableHeader(c)
        c.write('\n' + '\t')
        c.write('1' + '\t')
        use_PC.PC_worstCase(PC, c)
        c.write('\n' + '\t')
        c.write('2' + '\t')
        use_FCI.FCI_worstCase(FCI, c)
        c.write('\n' + '\t')
        c.write('3' + '\t')
        use_FCI.FCI_worstCase(GES, c)

        c.write('\n' + '\n')
        c.write("MEDIAN CASE:")

        tableHeader(c)
        c.write('\n' + '\t')
        c.write('1' + '\t')
        use_PC.PC_medianCase(PC, c)
        c.write('\n' + '\t')
        c.write('2' + '\t')
        use_FCI.FCI_medianCase(FCI, c)
        c.write('\n' + '\t')
        c.write('3' + '\t')
        use_FCI.FCI_medianCase(GES, c)


def dateandtime (c):
    dt = datetime.now()
    dt_string = dt.strftime("%d/%m/%Y %H:%M:%S")

    c.write(dt_string)
    c.write('\n' + '\n')

def statInfo (c):
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

def simInfo (c):
    c.write('Simulation:')
    c.write('\n' + '\n')
    c.write('**Write info here**')
    c.write('\n' + '\n')

def algInfo (c):
    c.write('Algorithms:')
    c.write('\n' + '\n')
    c.write('1. PC' + '\n' + '2. FCI' + '\n' + '3. GES')
    c.write('\n' + '\n')

def weightInfo (c):
    c.write('Weighting of Statistics:')
    c.write('\n' + '\n')
    c.write('**Write weighting here**')
    c.write('\n' + '\n')

def tableHeader (c):
    c.write('\n' + '\n')
    c.write('All edges')
    c.write('\n' + '\n')
    c.write('\tAlg   AP      AR     AHP   AHPCE     AHR   AHRCE   McAdj   McArr   F1Adj   F1Arr     SHD    E')
