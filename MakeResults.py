import fileHelper as file
import myStatistics as stat

def makefile(pc, fci, ges):
    with open("Comparison.txt", mode = "w") as c:

    #date and time
        file.dateandtime(c)

    #Statistics info
        file.statInfo(c)
        
    #Simulation info
        file.simInfo(c)

    #Algorithms info
        file.algInfo(c)
    
    #Weight info
        file.weightInfo(c)

    #Results
        c.write('AVERAGE STATISTICS')
        c.write('\n' + '\n')

        file.tableHeader(c)
        #--------------------------
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
        gesStat = stat.average(ges)
        for k in gesStat:
            o = stat.truncate(k, 4)
            c.write('%s\t' % o)
        #--------------------------

        c.write('\n' + '\n')

        c.write('STANDARD DEVIATION')
        c.write('\n' + '\n')

        file.tableHeader(c)
        #--------------------------
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
        gesStat = stat.STdev(ges)
        for k in gesStat:
            o = stat.truncate(k, 4)
            c.write('%s\t' % o)
        #--------------------------
        c.write('\n' + '\n')

        c.write('WORST CASE')
        c.write('\n' + '\n')

        file.tableHeader(c)
        #--------------------------
        c.write('\n' + '\t')
        c.write('1' + '\t')
        pcStat = stat.worstCase(pc)
        for i in pcStat:
            m = stat.truncate(i, 4)
            c.write('%s\t' % m)
    
        c.write('\n' + '\t')
        c.write('2' + '\t')
        fciStat = stat.worstCase(fci)
        for j in fciStat:
            n = stat.truncate(j, 4)
            c.write('%s\t' % n)
        
        c.write('\n' + '\t')
        c.write('3' + '\t')
        gesStat = stat.worstCase(ges)
        for k in gesStat:
            o = stat.truncate(k, 4)
            c.write('%s\t' % o)
        #--------------------------        
        c.write('\n' + '\n')

        c.write('MEDIAN CASE')
        c.write('\n' + '\n')

        file.tableHeader(c)
        #--------------------------
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
        gesStat = stat.median(ges)
        for k in gesStat:
            o = stat.truncate(k, 4)
            c.write('%s\t' % o)
        #--------------------------
        c.write('\n' + '\n')

