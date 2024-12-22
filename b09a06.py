def permutationen(seq):
    if len(seq) == 0:
        yield []
    for i in range(len(seq)):
        # Die Verwendung von Listenslicing (seq[:i] + seq[i+1:]) erstellt implizit eine
        rest = seq[:i] + seq[i+1:]
        for p in permutationen(rest):
            yield [seq[i]] + p

for p in permutationen([1,2,3]):
    print(p)