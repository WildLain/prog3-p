#!/usr/bin/env python3
import sys

crypt = "wgsnqcdvmeyluzoabhrjfkxipt"
decrypt ="abcdefghijklmnopqrstuvwxyz"

filename = sys.argv[1]
txt = open(filename).read()

decrypt = print("".join([decrypt[crypt.find(c)]  if c.isalpha() else c for c in txt]))

# ./b09a02.py verschluesselt.txt 