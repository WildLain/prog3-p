from b10a01 import Messwert

class Messreihe:
    def __init__(self, iterable=None):
        self._list = []
        if iterable is not None: 
            self._list = [Messwert(line.strip()) if isinstance(line, str) else line for line in iterable]
            self._list.sort()
    def __len__(self):
        return len(self._list)
    def add(self, *messwerte):
        if len(messwerte) == 0:
            raise ValueError("Es muss mindestens ein Messwert übergeben werden")
        else:
            [self._list.append(mw) for mw in messwerte if isinstance(mw, Messwert)]
            self._list.sort()
    def __add__(self, other):
        nw = Messreihe()
        nw._list = list(set(self._list + other.list))
        nw._list.sort()
        return nw
    #Generator Methode
    def __iter__(self):
        for mw in self._list:
            yield mw
    def __getitem__(self, n):
        if isinstance(n, int):
            return self._list[n]
        elif isinstance(n, str):
            return [mw for mw in self._list if mw.zeitpunkt.startswith(n)]
        elif isinstance(n, slice):
            return self._list[n]
    def __repr__(self):
        return f"Messreihe({self._list})"

#Iterator Klasse
class MessIter:
    def __init__(self, mr):
        self._mr = mr
        self.pos = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.pos += 1
        if self.pos >= len(self._mr):
            raise StopIteration
        return self._mr[self.pos]
    
# Test geschachteltes Iterieren Test
mw = Messreihe(open('messwerte.csv'))
it1, it2 = iter(mw), iter(mw)
for i in range(10):
    m1, m2 = next(it1), next(it2)
    print(m1, m2, "Problem" if m1 != m2 else "OK")

'''
Messwert('2013-07-15 16:03:08.260597', 19.875) Messwert('2013-07-15 16:03:08.260597', 19.875) OK
Messwert('2013-07-15 16:15:01.997792', 19.5625) Messwert('2013-07-15 16:15:01.997792', 19.5625) OK
Messwert('2013-07-15 16:30:01.455079', 20.3125) Messwert('2013-07-15 16:30:01.455079', 20.3125) OK
Messwert('2013-07-15 17:00:01.201636', 20.0625) Messwert('2013-07-15 17:00:01.201636', 20.0625) OK
Messwert('2013-07-15 17:15:01.618921', 20.625) Messwert('2013-07-15 17:15:01.618921', 20.625) OK
Messwert('2013-07-15 17:30:02.060205', 19.75) Messwert('2013-07-15 17:30:02.060205', 19.75) OK
Messwert('2013-07-15 17:42:38.733501', 20.1875) Messwert('2013-07-15 17:42:38.733501', 20.1875) OK
Messwert('2013-07-15 18:30:01.251394', 20.4375) Messwert('2013-07-15 18:30:01.251394', 20.4375) OK
Messwert('2013-07-15 18:45:01.420677', 20.375) Messwert('2013-07-15 18:45:01.420677', 20.375) OK
Messwert('2013-07-15 19:00:01.885987', 19.5625) Messwert('2013-07-15 19:00:01.885987', 19.5625) OK
'''
