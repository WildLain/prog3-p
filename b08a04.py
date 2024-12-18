def auskunft(linie, start, ziel):
    START, ZIEL, MIN = 0, 1, 2
    data = "fahrzeiten.txt"
    f = open(data)
    station = {}
    min = 0
    for line in f:
        l,s,z,m = line.split(";")
        if l == linie:
            station[s] = (s, z, m[:-1])
        
    haltestelle = station.get(start)
    haltestellen = []
    while(True):
        haltestellen.append(haltestelle[START])
        min += int(haltestelle[MIN])
        haltestelle = station.get(haltestelle[ZIEL])
        if ziel in haltestelle[START]:
            haltestellen.append(haltestelle[START])
            break
    print("Minuten:",min, "Haltestellen:", haltestellen)

auskunft("S9", "Kelsterbach", "Niederrad")