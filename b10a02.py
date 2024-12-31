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
    def __iter__(self):
        return iter(self._list)
    def __getitem__(self, n):
        if isinstance(n, int):
            return self._list[n]
        elif isinstance(n, str):
            return [mw for mw in self._list if mw.zeitpunkt.startswith(n)]
        elif isinstance(n, slice):
            return self._list[n]
    def __repr__(self):
        return f"Messreihe({self._list})"

# Instanziierung, kann ohne Parameter erfolgen oder alternativ iterierbares Objekt übergeben
# mr = Messreihe(open('messwerte.csv'))
# print(mr)

# Standardfunktion len(mr) liefert Anzahl der Messwerte
# print(len(mr))

# Methode add() fügt Messwerte hinzu
# mr.add(Messwert("2014-11-16 18:30:02.145456",19.75))

# Zwei Messreiehen können mit dem + Operator vereinigt werden, es sollen keine gleichen doppelten Messwerte enthalten sein
# mr1 = Messreihe()
# mr1.add(Messwert("2013-07-15 23:45:01.439331",18.9375), 
#         Messwert("2013-07-15 19:45:02.073782",19.0625), 
#         Messwert("2015-08-21 06:45:01.484487",23.75), 
#         Messwert("2014-11-14 03:30:01.987710",20.9375))
# mr2 = Messreihe()
# mr2.add(Messwert("2014-11-16 18:30:02.145456",19.75),
#         Messwert("2014-11-16 18:45:01.713329",20.9375),
#         Messwert("2014-11-16 19:15:01.730072",21.3125),
#         Messwert("2013-07-15 23:45:01.439331",18.9375))
# m3 = mr1 + mr2
# print("len(mr1) + len(mr2) = len(m3)", len(mr1), "+", len(mr2), "=", len(m3))
# print(m3)

# Messreihe soll iteriert werden können
# for mw in mr:
#     print(mw)

# Mit einer Ganzzahl n indiziert soll der n-te Messwert einer Messreihe zurückgeliefert werden
# print("m3[16]:", mr[16])
# print("mr['2019-01-07 15']:", mr['2019-01-07 15'])
# Slicing wäre doch toll, oder?
# print("mr[5:10]:", mr[5:10])

