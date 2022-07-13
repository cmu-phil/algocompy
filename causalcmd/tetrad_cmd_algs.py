import os
from datetime import datetime

from causallearn.utils.TXT2GeneralGraph import txt2generalgraph

jar = "causal-cmd-1.4.1-jar-with-dependencies.jar"

stamp = str(datetime.now()).replace(" ", "_")
prefix = "causal_cmd_results/out_" + stamp

# Check whether the specified path exists or not
isExist = os.path.exists("causal_cmd_results")

if not isExist:
    # Create a new directory because it does not exist
    os.makedirs("causal_cmd_results")
    print("A new directory, causal-cmd-results, is created.")

print("Result will be sent to this file: " + prefix + ".txt")

def pc(path, alpha):
    os.system("java -Xmx10g -jar " + jar + " "
              + "--default "
              + "--algorithm pc "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--test fisher-z-test "
              + "--delimiter tab "
              + "--alpha " + str(alpha) + " "
              + "--verbose "
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")

def pcmax(path, alpha):
    os.system("java -Xmx10g -jar " + jar + " "
              + "--default "
              + "--algorithm pcmax "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--test fisher-z-test "
              + "--delimiter tab "
              + "--alpha " + str(alpha) + " "
              + "--verbose "
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")

def fci(path, alpha):
    os.system("java -Xmx10g -jar " + jar + " "
              + "--default "
              + "--algorithm fci "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--alpha " + str(alpha) + " "
              + "--verbose "
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")

def fges(path, penaltyDiscount):
    os.system("java -Xmx10g -jar " + jar + " "
              + "--default "
              + "--algorithm fges "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--delimiter tab  "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--parallel "
              + "--verbose "
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")

def grasp(path, penaltyDiscount):
    os.system("java -Xmx10g -jar " + jar + " "
              + "--default "
              + "--algorithm grasp "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")

def graspfci(path, penaltyDiscount):
    os.system("java -Xmx10g -jar " + jar + " "
              + "--default "
              + "--algorithm graspfci "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--test fisher-z-test "
              + "--delimiter tab  "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")

def boss_tuck(path, penaltyDiscount):
    os.system("java -Xmx10g -jar " + jar + " "
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
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")

def boss(path, penaltyDiscount):
    os.system("java -Xmx10g -jar " + jar + " "
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
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")

def rges(path, penaltyDiscount):
    os.system("java -Xmx10g -jar " + jar + " "
              + "--default "
              + "--experimental "
              + "--algorithm rges "
              + "--data-type continuous "
              + "--dataset " + path + " "
              + "--score sem-bic-score "
              + "--delimiter tab "
              + "--penaltyDiscount " + str(penaltyDiscount) + " "
              + "--verbose "
              + "--prefix " + prefix)
    return txt2generalgraph(prefix + ".txt")
