import os
from causallearn.utils.TXT2GeneralGraph import txt2generalgraph


def pc(path, alpha):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--algorithm pc "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--test fisher-z-test "
              + "--delimiter tab "
              + "--alpha " + str(alpha) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")


def fci(path, alpha):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--algorithm fci "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--alpha " + str(alpha) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")


def fges(path, penalty_discount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--algorithm fges "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--delimiter tab  "
              + "--precomputeCovariances "
              + "--penaltyDiscount " + str(penalty_discount) + " "
              + "--verbose "
              + "--prefix tmp "
              + "--parallelized")
    return txt2generalgraph("tmp.txt")


def grasp(path, penalty_discount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--algorithm grasp "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--precomputeCovariances "
              + "--penaltyDiscount " + str(penalty_discount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")


def graspfci(path, penalty_discount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--algorithm graspfci "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--precomputeCovariances "
              + "--penaltyDiscount " + str(penalty_discount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")


def boss_tuck(path, penalty_discount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--experimental "
              + "--algorithm boss-tuck "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab "
              + "--graspUseScore "
              + "--precomputeCovariances "
              + "--penaltyDiscount " + str(penalty_discount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")


def boss(path, penalty_discount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--experimental "
              + "--algorithm boss "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab "
              + "--graspUseScore "
              + "--precomputeCovariances "
              + "--penaltyDiscount " + str(penalty_discount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")


def rges(path, penalty_discount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--experimental "
              + "--algorithm rges "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--delimiter tab "
              + "--precomputeCovariances "
              + "--penaltyDiscount " + str(penalty_discount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")
