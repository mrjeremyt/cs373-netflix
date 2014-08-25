#!/usr/bin/env python3

"""
To run the program
    % coverage3 run --branch RunCollatz.py < RunCollatz.in

To obtain coverage of the run:
    % coverage3 report -m

To document the program
    % pydoc -w Collatz
"""

# -------
# imports
# -------

import sys

from Netflix import netflix_solve

# ----
# main
# ----

netflix_solve(sys.stdin, sys.stdout)