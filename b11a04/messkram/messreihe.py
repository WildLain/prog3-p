from .messwert import Messwert
from typing import Any, Self, Iterator, Union

class Messreihe:
    def __init__(self, iterable=None) -> None:
        self._werte: list[Messwert] = []
        if iterable is not None: 
            self._werte = [Messwert(line.strip()) if isinstance(line, str) else line for line in iterable]
            self._werte.sort()
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

class MonotonieVerstossError(ValueError):
    pass