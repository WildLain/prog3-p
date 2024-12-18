#!/usr/bin/env python3

import sys

argc = len(sys.argv)
progname = sys.argv[0]
textfile = sys.argv[1]
# textfile = "midsummernightsdream.txt"
# textfile = "test.txt"
f = open(textfile)

def count_words(f):
    wFromFile = f.read().lower().split()
    words = len(wFromFile)
    wk = sorted(wFromFile)
    d = {}
    for el in wk:
        d[el] = wFromFile.count(el)
    # print(d)
    dsorted = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    print(dsorted)
    print("Woerter insgesamt:",words)
    return d    

def count_chars(f):
    text = f.read().lower()
    d = {}
    letters = 0
    for c in "abcdefghijklmnopqrstuvwxyz":
        n = text.count(c)
        d[c] = n
        letters += n
    d = dict(sorted(d.items(), key=lambda x:x[1], reverse=True))
    print(d)
    print("Buchstaben:", letters)
    return d

def count_lines(f):
    lines = 0
    for line in f:
        lines += 1
    print("Zeilen:", lines)     

count_words(f)
count_chars(f)
count_lines(f)


