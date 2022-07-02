import numpy as np
import math

def average (stats):

    s = np.mean(stats, axis=0)

    return s

def STdev (stats):

    s = np.std(stats, axis=0)

    return s

def median (stats):

    s = np.median(stats, axis = 0)

    return s

def worstCase (stats):

    s = np.amin(stats, axis=0)

    return s

def truncate (n, decimals):
    a = math.isnan(n)
    if a:
        return np.NaN
    else:
        string = ('.' + str(2) + 'f')
        n = format(n, string)
        return n