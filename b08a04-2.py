def auskunft(linie, start, ziel):
    LINIE, START, ZIEL, MINUTEN = 0,1,2,3
    lines, minutes       = {}, 0
    
    data    = [line[:-1].split(";") for line in list(open("fahrzeiten.txt", "r"))]
    for el in data:
        stop    = { el[START] : {"Ziel": el[ZIEL], "Minuten" : el[MINUTEN]}}
        line    = { el[LINIE] : stop }
        if el[LINIE] not in lines:
            lines.update(line)
        else:
            lines[el[LINIE]].update(stop)

    stops   = lines[linie]
    dest    = start
    lst     = []
    lst.append(str(start))
    while(True):
        stop = stops.get(dest)
        print(stop)
        minutes += int(stop["Minuten"])
        lst.append(stop["Ziel"])
        dest = stop["Ziel"]
        if stop["Ziel"] == ziel:
            break

    print("Minuten:", minutes, "Stationen:", lst)
auskunft("S9", "Kelsterbach", "Niederrad")

#S9;Stadion;Niederrad;3
#S9;Flughafen;Stadion;4
#S9;Kelsterbach;Flughafen;6
      
# stationen = list(open(data, "r"))
# station = [line[:-1].split(";") for line in stationen]

# data = list(open("fahrzeiten.txt", "r"))
# data = [tuple(line[:-1].split(";")) for line in data]
