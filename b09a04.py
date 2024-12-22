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

schmaeh = [print(line.split(';')[0], line.split(';')[1], "bekommt mehr, als er/sie verdient!") for line in open(filename) if int(line.split(';')[3]) > 100000]