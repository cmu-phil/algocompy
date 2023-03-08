Our current plan is to update this repository to do algorithms comparisons using the [algcomparison](https://dl.acm.org/doi/abs/10.5555/3455716.3455954) command line XML tool.

Algcomparison is an API in Tetrad for algorithms comparison that is already well-developed and has been heavily used. The command line tool allows on to construct XML files to instruct algcomparison as to how to run these comparisons. The command line tool also adds a facility to include search graphs from other platforms such as R, Python, or Matlab, so the idea is to write some Python code (this project) to do these runs, construct the relevant XML files to give to the command-line tool, and to run the command line tool using os.system(..) to generate comparison tables.

The previous algcompy code has been moved into the directory, 'old' and updated to causal-cmd 1.6.1.

jdramsey 2023-03-08
