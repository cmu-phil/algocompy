import tetrad_cmd_algs as tc

path = "/Users/pablopuiz/Desktop/Algocomparison-main/14.txt"

print("pc", tc.pc(path, 0.05))
print("fci", tc.fci(path, 0.05))
print("fges", tc.fges(path, 2))
print("boss-tuck", tc.boss_tuck(path, 2))
print("boss", tc.boss(path, 2))
print("rges", tc.rges(path, 2))
print("graspfci", tc.graspfci(path, 2))