filename = "bonz.txt"

# aufsteigend sortierte Liste der Wohnorte aller Männer
wohnorte = sorted(line.split(";")[4].strip() for line in open(filename))
print(wohnorte)

# Summe der Gehälter aller Frauen
gehalt = sum(int(line.split(";")[3]) for line in open(filename) if line.startswith("Frau"))
print(gehalt)

# den Wohnort der Person, die unter allen, deren Vorname mit ’J’ beginnt, am meisten verdient (bzw.
# bekommt)
johnort = max([line.split(";") for line in open(filename) if line.split(";")[2].startswith('J')],
              key = lambda x: int(x[3]))[4].strip()
print(johnort)

# Eine (inhaltlich natürlich nicht gerechtfertigte) Liste von gehaltsbezogenen Schmähungen für alle Personen
# mit Gehalt ab 100000 Euro in der Form “Anrede Nachname bekommt mehr, als er/sie verdient!”
# (Beispiel: “Herr Meier bekommt mehr, als er verdient!” oder “Frau Biffel bekommt mehr, als sie
# verdient!”)

# schmaeh = [print(line.split(';')[0], line.split(';')[1], "bekommt mehr, als er/sie verdient!") for line in open(filename) if int(line.split(';')[3]) > 100000]

sch = [f"{line[0]} {line[1]} bekommt mehr, als {'er' if line[0].startswith('Herr') else 'sie'} verdient!" for line in [line.strip().split(';') for line in open(filename)] if int(line[3]) >= 100000]
[print(line) for line in sch]

#Max
# [f"{x[0]} {x[1]} bekommt mehr, als {"er" if x[0] == "Herr" else "sie"} verdient!" for x in [x[:-1].split(";") for x in list(open("bonz.txt"))] if int(x[3]) >= 100000]

#Larissa
# print([ f"{part[0]} {part[1]} bekommt mehr, als {'er' if (part[0].startswith('Herr')) else 'sie'} verdient!" for part in [(word[0],word[1],int(word[3])) for word in [word.split(";") for word in [line.strip() for line in open("bonz.txt",'r').readlines()]] if int(word[3]) >= 100000]])
