from datetime import datetime
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import myStatistics as stat


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
    c.write('All edges')
    c.write('\n' + '\n')
    c.write('\tAlg' + '\tAP' + '\tAR' + '\tAHP' + '\tAHP_CE' + '\tAHR' + '\tAHR_CE' + '\tMcAdj' + '\tMcArrow' + '\tF1Adj' + '\tF1Arrow' + '\tSHD' + '\tE' + '\tU')



