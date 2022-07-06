from datetime import datetime

from utils import my_statistics as stat


def make_file(est_g1, est_g2, est_g3, est_g4, est_g5, est_g6, est_g7):
    with open("Comparison.txt", mode="w") as c:
        dateandtime(c)

        stat_info(c)

        sim_info(c)

        alg_info(c)

        weight_info(c)

        c.write("AVERAGE STATISTICS:")

        table_header(c)
        c.write('\n' + '\t')
        c.write('1' + '\t')
        average(est_g1, c)
        c.write('\n' + '\t')
        c.write('2' + '\t')
        average(est_g2, c)
        c.write('\n' + '\t')
        c.write('3' + '\t')
        average(est_g3, c)
        c.write('\n' + '\t')
        c.write('4' + '\t')
        average(est_g4, c)
        c.write('\n' + '\t')
        c.write('5' + '\t')
        average(est_g5, c)
        c.write('\n' + '\t')
        c.write('6' + '\t')
        average(est_g6, c)
        c.write('\n' + '\t')
        c.write('7' + '\t')
        average(est_g7, c)

        c.write('\n' + '\n')
        c.write("STANDARD DEVIATION:")

        table_header(c)
        c.write('\n' + '\t')
        c.write('1' + '\t')
        st_dev(est_g1, c)
        c.write('\n' + '\t')
        c.write('2' + '\t')
        st_dev(est_g2, c)
        c.write('\n' + '\t')
        c.write('3' + '\t')
        st_dev(est_g3, c)
        c.write('\n' + '\t')
        c.write('4' + '\t')
        st_dev(est_g4, c)
        c.write('\n' + '\t')
        c.write('5' + '\t')
        st_dev(est_g5, c)
        c.write('\n' + '\t')
        c.write('6' + '\t')
        st_dev(est_g6, c)
        c.write('\n' + '\t')
        c.write('7' + '\t')
        st_dev(est_g7, c)

        c.write('\n' + '\n')
        c.write("WORST CASE:")

        table_header(c)
        c.write('\n' + '\t')
        c.write('1' + '\t')
        worst_case(est_g1, c)
        c.write('\n' + '\t')
        c.write('2' + '\t')
        worst_case(est_g2, c)
        c.write('\n' + '\t')
        c.write('3' + '\t')
        worst_case(est_g3, c)
        c.write('\n' + '\t')
        c.write('4' + '\t')
        worst_case(est_g4, c)
        c.write('\n' + '\t')
        c.write('4' + '\t')
        worst_case(est_g5, c)
        c.write('\n' + '\t')
        c.write('6' + '\t')
        worst_case(est_g6, c)
        c.write('\n' + '\t')
        c.write('7' + '\t')
        worst_case(est_g7, c)

        c.write('\n' + '\n')
        c.write("MEDIAN CASE:")

        table_header(c)
        c.write('\n' + '\t')
        c.write('1' + '\t')
        median_case(est_g1, c)
        c.write('\n' + '\t')
        c.write('2' + '\t')
        median_case(est_g2, c)
        c.write('\n' + '\t')
        c.write('3' + '\t')
        median_case(est_g3, c)
        c.write('\n' + '\t')
        c.write('4' + '\t')
        median_case(est_g4, c)
        c.write('\n' + '\t')
        c.write('4' + '\t')
        median_case(est_g5, c)
        c.write('\n' + '\t')
        c.write('6' + '\t')
        median_case(est_g6, c)
        c.write('\n' + '\t')
        c.write('7' + '\t')
        median_case(est_g7, c)


def dateandtime(c):
    dt = datetime.now()
    dt_string = dt.strftime("%d/%m/%Y %H:%M:%S")

    c.write(dt_string)
    c.write('\n' + '\n')


def stat_info(c):
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


def sim_info(c):
    c.write('Simulation:')
    c.write('\n' + '\n')
    c.write('**Write info here**')
    c.write('\n' + '\n')


def alg_info(c):
    c.write('Algorithms:')
    c.write('\n' + '\n')
    c.write('1. PC_CL' + '\n' + '2. PC_CC' + '\n' + '3. PCMAX_CC' + '\n' + '4. GES_CL' + '\n' + '5. FGES_CC' + '\n' + '6. FCI_CL' + '\n' + '7. GRASP_CC' + '\n' + '8. GIN_CL')
    c.write('\n' + '\n')


def weight_info(c):
    c.write('Weighting of Statistics:')
    c.write('\n' + '\n')
    c.write('**Write weighting here**')
    c.write('\n' + '\n')


def table_header(c):
    c.write('\n' + '\n')
    c.write('All edges')
    c.write('\n' + '\n')
    c.write('\tAlg   AP      AR     AHP   AHPCE     AHR   AHRCE   McAdj   McArr   F1Adj   F1Arr     SHD    E')


def average(est_g, c):
    g_stat = stat.average(est_g)
    for i in g_stat:
        m = stat.truncate(i, 2)
        c.write('%s\t' % m)


def st_dev(est_g, c):
    g_stat = stat.STdev(est_g)
    for i in g_stat:
        m = stat.truncate(i, 2)
        c.write('%s\t' % m)


def worst_case(est_g, c):
    g_stat = stat.worstCase(est_g)
    for i in g_stat:
        m = stat.truncate(i, 2)
        c.write('%s\t' % m)


def median_case(est_g, c):
    g_stat = stat.median(est_g)
    for i in g_stat:
        m = stat.truncate(i, 2)
        c.write('%s\t' % m)
