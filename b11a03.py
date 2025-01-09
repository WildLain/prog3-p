from typing import Any, Self, Iterator, Union


class Messwert:
    def __init__(self, *args: Any) -> None:
        if len(args) == 1:
            self.zeitpunkt = str(args[0].split(',')[0]).strip('"')
            self.temperatur = float(args[0].split(',')[1])
        elif len(args) == 2:
            self.zeitpunkt = str(args[0])
            self.temperatur = float(args[1]) if isinstance(args[1], (float, int)) else float(args[1])
        else:
            raise ValueError("Falsche Anzahl an Argumenten")
    def __repr__(self) -> str:
        return f"Messwert(\'{self.zeitpunkt}\', {self.temperatur})"
    def __eq__(self, other: Self) -> bool:
        return self.zeitpunkt == other.zeitpunkt and self.temperatur == other.temperatur
    def __lt__(self, other: Self) -> bool:
        if self.zeitpunkt == other.zeitpunkt:
            return self.temperatur < other.temperatur
        return self.zeitpunkt < other.zeitpunkt
    def __hash__(self) -> int:
        return hash((self.zeitpunkt, self.temperatur))

class Messreihe:
    def __init__(self, iterable=None) -> None:
        self._werte: list[Messwert] = []
        if iterable is not None: 
            self._werte = [Messwert(line.strip()) if isinstance(line, str) else line for line in iterable]
            self._werte.sort()
    # property braucht man in dem Falle nicht weil die Messreihe an sich ja eigentlich eine Liste aus Messwerten sein soll?
    # @property
    # def werte(self) -> list[Messwert]:
    #     "Messwertliste als Liste von Messwerten: list[Messwerte]"
    #     return self._werte
    def __len__(self) -> int:
        return len(self._werte)
    def add(self, *messwerte: Messwert) -> None:
        if len(messwerte) == 0:
            raise ValueError("Es muss mindestens ein Messwert übergeben werden")
        else:
            assert(all(isinstance(mw, Messwert) for mw in messwerte))
            [self._werte.append(mw) for mw in messwerte if isinstance(mw, Messwert)]
            self._werte.sort()
    def addNew(self, messwert) -> None:
        if isinstance(messwert, Messwert):
            if messwert.zeitpunkt >= self._werte[-1].zeitpunkt:
                self.add(messwert)
            else:
                raise TypeError
        else:
            raise MonotonieVerstossError
    def __add__(self, other: 'Messreihe') -> 'Messreihe':
        assert(isinstance(other, Messreihe))
        nw = Messreihe()
        nw._werte = list(set(self._werte + other._werte))
        nw._werte.sort()
        return nw
    def __iter__(self) -> Iterator[Messwert]:
        return iter(self._werte)
    def __getitem__(self, n) -> 'Messreihe':
        if isinstance(n, int):
            return Messreihe([self._werte[n]])
        elif isinstance(n, str):
            return Messreihe([mw for mw in self._werte if mw.zeitpunkt.startswith(n)])
        elif isinstance(n, slice):
            return Messreihe(self._werte[n])
        else:
            raise TypeError("Ungültiges Argument")
    def __repr__(self) -> str:
        return f"Messreihe({self._werte})"

# Unterklasse von ValueError
class MonotonieVerstossError(ValueError):
    pass

mr = Messreihe(open("messwerte.csv"))[:10]

# a) die MonotonieVerstossError-Exception selbst zu fangen,
try:
    mr.addNew(mr[0])
except MonotonieVerstossError:
    print("MonotonieVerstossError gefangen.")

 # b) stattdessen die eingebaute ValueError-Exception aufzufangen oder
try:
    mr.addNew(mr[0])
except ValueError:
    print("ValueError gefangen")

# c) die ebenfalls eingebaute Exception RuntimeError.
try:
    mr.addNew(mr[0])
except RuntimeError:
    print("RuntimeError gefangen.")

# try:
#     mr.addNew(mr[0])
# except MonotonieVerstossError:
#     print("MonotonieVerstossError gefangen.")
# except ValueError:
#     print("ValueError gefangen")
# except RuntimeError:
#     print("RuntimeError gefangen.")

#Welche funktionieren, und warum?
