#!/usr/bin/env python3
import sys
filename = sys.argv[1]
# filename = "raeuberbriefenc.sec"

f = open(filename).read()
hauefigkeiten = {c:f.count(c) for c in "abcdefghijklmnopqrstuvwxyz"}
hSortiert = dict(sorted(hauefigkeiten.items(), key = lambda v: v[1], reverse=True))
ersetzung = {k:"eniastruhdlcmogkwbzfvpjxyq"[i] for i,k in enumerate(hSortiert.keys())}
txt = "".join([ersetzung.get(c, c) if c.isalpha() else c for c in f])

print(hSortiert)
print(ersetzung)
print(txt)

# Version line by line attempt T_T
# hauefigkeiten = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"}
# [print("".join([ersetzung.get(c, c) if c.isalpha() else c for c in line])[:-1]) for line in open(filename)]

