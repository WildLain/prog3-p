from typing import Any, Self
import re

class ZeitpunktFormatError(ValueError):
    pass

class TemperaturFormatError(ValueError):
    pass

class Messwert:
    def __init__(self, *args: Any) -> None:
        #"2013-07-15 18:45:01.420677",20.375
        timeRgx = re.compile(r'\b(\d{4})-([0][1-9]|[1][0-2])-([0-2][0-9]|[3][01]) ([01][0-9]|[2][0-3]):[0-5][0-9]:[0-5][0-9]\.\d{6}\b')
        tempRgx = re.compile(r'\b(\d{1,2}\.\d{1,4})\b')
        
        try:
            if len(args) == 1:
                zeitpunkt_str = str(args[0].split(',')[0]).strip('"')
                temperatur_str = str(args[0].split(',')[1])
                zeitpunkt_match = re.match(timeRgx, zeitpunkt_str)
                temperatur_match = re.match(tempRgx, temperatur_str)
                if not zeitpunkt_match:
                    raise ZeitpunktFormatError("Zeitpunkt falsch formatiert.")
                if not temperatur_match:
                    raise TemperaturFormatError("Temperatur falsch formatiert oder komischer Wert.")
                self.zeitpunkt = zeitpunkt_str
                self.temperatur = float(temperatur_str)
            elif len(args) == 2:
                zeitpunkt_match = re.match(timeRgx, str(args[0]))
                temperatur_match = re.match(tempRgx, str(args[1]))
                if not zeitpunkt_match:
                    raise ZeitpunktFormatError("Zeitpunkt falsch formatiert.")
                if not temperatur_match:
                    raise TemperaturFormatError("Temperatur falsch formatiert oder komischer Wert.")
                self.zeitpunkt = str(args[0])
                self.temperatur = float(args[1]) if isinstance(args[1], (float, int)) else float(args[1])
            else:
                raise ValueError("Falsche Anzahl an Argumenten")
        except (ZeitpunktFormatError, TemperaturFormatError, ValueError) as e:
            print(f"Error: {e}")
            raise
        
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



mw = Messwert('"2013-07-15 18:45:01.420677",20.375')
mw = Messwert('"2013-07-15 19:0013566:01.885987",19.5625hds347')
print(mw)   