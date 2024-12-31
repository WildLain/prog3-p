from b10a04 import Messreihe, Messwert, MessIter

def enum(iterable):
    nr = -1
    for mw in iterable:
        nr += 1
        yield (nr, mw)

mr = Messreihe(open("messwerte.csv"))
for nr, messwert in enum(mr):
    print(nr,"->",messwert)