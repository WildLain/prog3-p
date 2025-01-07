from typing import Any, Self, Iterator


class Messwert:
    def __init__(self, *args: str) -> None:
        if len(args) == 1:
            self.zeitpunkt  = str(args[0].split(',')[0]).strip('"')
            self.temperatur = float(args[0].split(',')[1])
        elif len(args) == 2:
            self.zeitpunkt = str(args[0])
            self.temperatur = float(args[1])
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
        self._list = []
        if iterable is not None: 
            self._list = [Messwert(line.strip()) if isinstance(line, str) else line for line in iterable]
            self._list.sort()
    def __len__(self) -> int:
        return len(self._list)
    def add(self, *messwerte: Messwert) -> None:
        if len(messwerte) == 0:
            raise ValueError("Es muss mindestens ein Messwert übergeben werden")
        else:
            [self._list.append(mw) for mw in messwerte if isinstance(mw, Messwert)]
            self._list.sort()
    def __add__(self, other: 'Messreihe') -> 'Messreihe':
        nw = Messreihe()
        nw._list = list(set(self._list + other._list))
        nw._list.sort()
        return nw
    def __iter__(self) -> Iterator[Messwert]:
        return iter(self._list)
    def __getitem__(self, n) -> Messwert | list[Messwert] | list[str]:
        if isinstance(n, int):
            return self._list[n]
        elif isinstance(n, str):
            return [mw for mw in self._list if mw.zeitpunkt.startswith(n)]
        elif isinstance(n, slice):
            return self._list[n]
        else:
            raise TypeError("Ungültiges Argument")
    def __repr__(self) -> str:
        return f"Messreihe({self._list})"