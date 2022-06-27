from datetime import datetime
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import myStatistics as stat

def makefile(pc, fci, cdnod):
    with open("Comparison.txt", mode = "w") as c:

    #date and time
        dt = datetime.now()
        dt_string = dt.strftime("%d/%m/%Y %H:%M:%S")

        c.write(dt_string)
        c.write('\n' + '\n')

    #Statistics info
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


    #Simulation info
        c.write('Simulation:')
        c.write('\n' + '\n')
        c.write('**Write info here**')
        c.write('\n' + '\n')

    #Algorithms info
        c.write('Algorithms:')
        c.write('\n' + '\n')
        c.write('1. PC' + '\n' + '2. FCI' + '\n' + '3. CDNOD')
        c.write('\n' + '\n')
    
    #Weight info
        c.write('Weighting of Statistics:')
        c.write('\n' + '\n')
        c.write('**Write weighting here**')
        c.write('\n' + '\n')

    #Results

        c.write('AVERAGE STATISTICS')
        c.write('\n' + '\n')

        c.write('All edges')
        c.write('\n' + '\n')
        c.write('\tSim' + '\tAP' + '\tAR' + '\tAHP' + '\tAHP_CE' + '\tAHR' + '\tAHR_CE' + '\tMcAdj' + '\tMcArrow' + '\tF1Adj' + '\tF1Arrow' + '\tSHD' + '\tE' + '\tU')
        
        c.write('\n' + '\t')
        c.write('1' + '\t')
        pcStat = stat.average(pc)
        for i in pcStat:
            m = stat.truncate(i, 4)
            c.write('%s\t' % m)
        
        c.write('\n' + '\t')
        c.write('2' + '\t')
        fciStat = stat.average(fci)
        for j in fciStat:
            n = stat.truncate(j, 4)
            c.write('%s\t' % n)
        
        c.write('\n' + '\t')
        c.write('3' + '\t')
        cdnodStat = stat.average(cdnod)
        for k in cdnodStat:
            o = stat.truncate(k, 4)
            c.write('%s\t' % o)
        c.write('\n' + '\n')

        c.write('STANDARD DEVIATION')
        c.write('\n' + '\n')

        c.write('All edges')
        c.write('\n' + '\n')
        c.write('\tSim' + '\tAP' + '\tAR' + '\tAHP' + '\tAHP_CE' + '\tAHR' + '\tAHR_CE' + '\tMcAdj' + '\tMcArrow' + '\tF1Adj' + '\tF1Arrow' + '\tSHD' + '\tE' + '\tU')
        c.write('\n' + '\t')
        c.write('1' + '\t')
        pcStat = stat.STdev(pc)
        for i in pcStat:
            m = stat.truncate(i, 4)
            c.write('%s\t' % m)
        
        c.write('\n' + '\t')
        c.write('2' + '\t')
        fciStat = stat.STdev(fci)
        for j in fciStat:
            n = stat.truncate(j, 4)
            c.write('%s\t' % n)
        
        c.write('\n' + '\t')
        c.write('3' + '\t')
        cdnodStat = stat.STdev(cdnod)
        for k in cdnodStat:
            o = stat.truncate(k, 4)
            c.write('%s\t' % o)
        c.write('\n' + '\n')

        c.write('WORST CASE')
        c.write('\n' + '\n')

        c.write('All edges')
        c.write('\n' + '\n')
        c.write('\tSim' + '\tAP' + '\tAR' + '\tAHP' + '\tAHP_CE' + '\tAHR' + '\tAHR_CE' + '\tMcAdj' + '\tMcArrow' + '\tF1Adj' + '\tF1Arrow' + '\tSHD' + '\tE' + '\tU')
        #Place array with all results here
        c.write('\n' + '\n')

        c.write('MEDIAN CASE')
        c.write('\n' + '\n')

        c.write('All edges')
        c.write('\n' + '\n')
        c.write('\tSim' + '\tAP' + '\tAR' + '\tAHP' + '\tAHP_CE' + '\tAHR' + '\tAHR_CE' + '\tMcAdj' + '\tMcArrow' + '\tF1Adj' + '\tF1Arrow' + '\tSHD' + '\tE' + '\tU')
        
        c.write('\n' + '\t')
        c.write('1' + '\t')
        pcStat = stat.median(pc)
        for i in pcStat:
            m = stat.truncate(i, 4)
            c.write('%s\t' % m)
        
        c.write('\n' + '\t')
        c.write('2' + '\t')
        fciStat = stat.median(fci)
        for j in fciStat:
            n = stat.truncate(j, 4)
            c.write('%s\t' % n)
        
        c.write('\n' + '\t')
        c.write('3' + '\t')
        cdnodStat = stat.median(cdnod)
        for k in cdnodStat:
            o = stat.truncate(k, 4)
            c.write('%s\t' % o)
        c.write('\n' + '\n')

