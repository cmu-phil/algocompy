import numpy as np
import random

from numpy import ndarray


def sample(p, d, N):

    g = random_dag(p, d)
    # I use dashed lines in my debugs for clarity and neatness

    # Debug print for random_dag g
    # print(g)
    # print("-----------------------")

    B = random_matrix(p, g)



    #
    # # Debug print for random_matrix B
    # print(B)
    # print("-----------------------")
    #
    # E = random_vector(p, B)
    #
    # Debug print for random_vector E
    # print(E)
    # print("-----------------------")
    #
    sample = linear_gaussian(B, p, N)

    # permutation = np.random.permutation(Sample.shape[1])
    # g = g[permutation, permutation]
    # Sample = Sample[:, permutation]

    # Final print
    return sample, g


# Generates my matrix but only contains 0 and 1
def random_dag(p, d):
    '''
    Randomly generates an Erdos-Renyi direct acyclic graph given an ordering.

    p = |variables|
    d = |edges| / |possible edges|
    '''
    # npe = |possible edges|
    pe = int(p * (p - 1) / 2)

    # e = |edges|
    ne = int(d * pe)

    # generate edges
    e = np.append(np.zeros(pe - ne, 'float'), np.ones(ne, 'float'))
    np.random.shuffle(e)

    # generate graph
    g = np.zeros([p, p], 'float')
    g.T[np.triu_indices(p, 1)] = e

    return g


# Changes all ones to a random float value between -1 and 1
def random_matrix(p, g):
    #B = g
    B = [x[:] for x in g]

    for a in range(p):
        for b in range(p):
            if B[a][b] == 1:
               B[a][b] = random.choice([-1, 1]) * random.uniform(0, 1)
    print("B = ", B)

    return B


# Generates a random vector of same size as matrix B
def random_vector(p):
    E = []

    for i in range(p):
        E.append(random.uniform(1, 3))

    return E


  # Generates the Linear Gaussian model
def linear_gaussian(B, p, N):
    I = np.identity(p)
    sample = np.zeros([N, p])
    BInv = np.linalg.inv(I - B)

    for i in range(N):
        E = random_vector(p)
        b: ndarray = np.dot(BInv, E)
        sample[i:] = b

    return sample
