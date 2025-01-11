from typing import Any, Self

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