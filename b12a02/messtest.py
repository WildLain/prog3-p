from random import gauss
from typing import Generator, Any
from messkram import Messreihe, Messwert
from datetime import datetime, timedelta

def makeMessreihe(jahr: int, monat: int, tag: int, anzahl: int) -> Messreihe:
    startzeit: datetime = datetime(jahr, monat, tag, 0, 0, 0)
    messwerte: list[Messwert] = []
    for i in range(anzahl):
        zeitpunkt: datetime = startzeit + timedelta(minutes=15 * i)
        messwerte.append(Messwert(zeitpunkt.strftime('%Y-%m-%d %H:%M:%S.%f'), gauss(17.0, 3.0)))
    return Messreihe(messwerte)

def messreihe2text(mr: Messreihe) -> Generator[str, Any, None]:
    for mw in mr:
        yield f'\"{mw.zeitpunkt}\", {mw.temperatur:.4f}\n'

if __name__ == "__main__":
    mr: Messreihe = makeMessreihe(2023, 1, 1, 10)
    with open('./messreihe.csv', 'w', newline='') as csvfile:
        for line in messreihe2text(mr):
            csvfile.write(line)