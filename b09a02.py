#!/usr/bin/env python3
import sys

crypt = "wgsnqcdvmeyluzoabhrjfkxipt"
decrypt ="abcdefghijklmnopqrstuvwxyz"

filename = sys.argv[1]

#Zeilenweise auslesen, ganze Datei als String einzulesen, schlechter Stil ;)
[print("".join([decrypt[crypt.find(c)]  if c.isalpha() else c for c in line])) for line in open(filename)]

# Ursprüngliche version
#txt = open(filename).read()
#print("".join([decrypt[crypt.find(c)]  if c.isalpha() else c for c in txt]))


# ./b09a02.py verschluesselt.txt 
# ./b09a02.py encrypted.txt