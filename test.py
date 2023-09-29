import sys
import re

with open(sys.argv[1]) as f:
    src = f.read()

    ifs = len(re.findall(r"if .*:", src))
    elifs = len(re.findall(r"elif .*:", src))
    elses = len(re.findall(r"else .*:", src))
    nests = len(re.findall(r"    if .*:", src))

    print(f"{ifs=}")
    print(f"{elifs=}")
    print(f"{elses=}")
    print(f"{nests=}")

    assert(ifs >= 4)
    assert(elifs >= 1)
    assert(elses >= 1)
    assert(nests >= 1)
