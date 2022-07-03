import os
from causallearn.utils.TXT2GeneralGraph import txt2generalgraph

def pc(path, alpha):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--default "
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
              + "--default "
              + "--algorithm fci "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--alpha " + str(alpha) + " "
              # + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")

def fges(path, penaltyDiscount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--default "
              + "--algorithm fges "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--delimiter tab  "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix tmp "
              + "--parallelized")
    return txt2generalgraph("tmp.txt")

def grasp(path, penaltyDiscount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--default "
              + "--algorithm grasp "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")

def graspfci(path, penaltyDiscount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--default "
              + "--algorithm graspfci "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")

def boss_tuck(path, penaltyDiscount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--default "
              + "--experimental "
              + "--algorithm boss-tuck "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab "
              + "--graspUseScore "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")

def boss(path, penaltyDiscount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--default "
              + "--experimental "
              + "--algorithm boss "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab "
              + "--graspUseScore "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")

def rges(path, penaltyDiscount):
    os.system("rm tmp.txt;java -Xmx10g -jar causal-cmd-1.4.0-SNAPSHOT-jar-with-dependencies.jar "
              + "--default "
              + "--experimental "
              + "--algorithm rges "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--delimiter tab "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix tmp")
    return txt2generalgraph("tmp.txt")
