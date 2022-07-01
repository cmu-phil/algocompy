from causallearn.search.ScoreBased.GES import ges
from causallearn.utils.cit import chisq, fisherz, gsq, kci, mv_fisherz
import AdjacencyConfusion as AdjConf
import ArrowConfusion as ArrConf
import SHD as shd
import myStatistics as stat


def GES(data, G):
    """
    Runs GES algorithm with given data.
    Computes adjacency and Arrowhead confusion between estimated and true graph.
    Saves results into matrix.
    -----------
    data: sample data
    G: true graph
    """

    maxP = 5
    parameters = {}
    # parameters["lambda_value"] = -2
    parameters["kfold"] = 5
    parameters["lambda"] = 0.01
    testges = ges(data, 'local_score_CV_general', maxP=maxP, parameters=parameters)['G']

    gesPerformance = GESstats(G, testges)

    return gesPerformance


def GESstats(G, testges):
    gesStat = []

    # Adjacency and Arrowhead
    ACcges = AdjConf.AdjacencyConfusion(G, testges)
    ArrCges = ArrConf.ArrowConfusion(G, testges)

    gesStat.append(ACcges.get_adj_precision())
    gesStat.append(ACcges.get_adj_recall())
    gesStat.append(ArrCges.get_arrows_precision())
    gesStat.append(ArrCges.get_arrows_precision_ce())
    gesStat.append(ArrCges.get_arrows_recall())
    gesStat.append(ArrCges.get_arrows_recall_ce())
    gesStat.append(ACcges.get_adj_Mc())
    gesStat.append(ArrCges.get_arrows_Mc())
    gesStat.append(ACcges.get_adj_F1())
    gesStat.append(ArrCges.get_arrows_F1())

    # SHD
    SHDges = shd.SHD(G, testges)

    gesStat.append(SHDges.get_shd())

    return gesStat