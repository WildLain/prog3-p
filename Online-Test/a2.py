def statistik(dateiname):
    bestellungen = {}
    data = [line.strip().split(';') for line in open(dateiname)]
    for plz, name, betrag in data:
        if plz not in bestellungen:
            bestellungen[plz] = {}
        if name not in bestellungen[plz]:
            bestellungen[plz][name] = 0
        bestellungen[plz][name] += int(betrag)
    # print(bestellungen)

    ausgabe = []
    for plz, personen in sorted(bestellungen.items()):
        person_str = " ".join(f'{name} ({betrag})' for name, betrag in sorted(personen.items()))
        ausgabe.append(f'{plz}: {person_str}')
    
    [print(b) for b in ausgabe]

if __name__ =="__main__":
    statistik("Online-Test/testdaten.txt")


# lst = []
# [(line.strip().split(';')) for line in open(dateiname)]
# [d.update({e[0] : { e[1] : e[2] }}) if e[0] not in d else d[e[0]].key().reduce(e[2], 0) for e in lst]