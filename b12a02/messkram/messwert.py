from typing import Any, Self
import re

class Messwert:
    def __init__(self, *args: Any) -> None:
        #"2013-07-15 18:45:01.420677",20.375
        timeRgx = re.compile(r'\b(\d{4})-([0][1-9]|[1][0-2])-([0-2][0-9]|[3][01]) ([01][0-9]|[2][0-3]):[0-5][0-9]:[0-5][0-9]\.\d{6}\b')
        tempRgx = re.compile(r'\b(\d{1,2}\.\d{1,4})\b')
        if(len(args) == 1):
            zeitpunkt_str = str(args[0].split(',')[0].strip('"'))
            temperatur_str = str(args[0].split(',')[1].strip("\n"))
        elif(len(args) == 2):
            zeitpunkt_str = args[0]
            temperatur_str = args[1]
        else:
            raise ValueError("Anzahl der uebergebenen Argumente falsch.")
        if timeRgx.match(zeitpunkt_str) is None:
            raise ZeitpunktFormatError("Zeitpunkt falsch formatiert")
        elif tempRgx.match(str(temperatur_str)) is None:
            raise TemperaturFormatError("Temperatur falsch formatiert.")  
        else:
            self.zeitpunkt = zeitpunkt_str
            self.temperatur = temperatur_str
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

class ZeitpunktFormatError(ValueError):
    pass

class TemperaturFormatError(ValueError):
    pass

if __name__ == '__main__':
    messwerte = []
    with open('b12a02/messwerteError.csv') as file:
        lines = file.readlines()
        for i in range (0,11):
                try:
                    print(Messwert(lines[i])) 
                except(ZeitpunktFormatError, TemperaturFormatError, ValueError) as e:
                    print(e)
                    continue