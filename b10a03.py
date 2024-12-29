from b10a02 import Messreihe, Messwert
from functools import reduce

# Bitte initalisieren Sie eine Messreihe aus der Datei messwerte.csv
mr = Messreihe(open('messwerte.csv'))

# Wie viele Messwerte enthält die Messreihe?
print("Anzahl Messwerte:", len(mr))

# Was sind die Messwerte mit a) der kleinsten und b) der größten Temperatur?
print("Kleinster Messwert:\t", min(mr, key=lambda x: x.temperatur))
print("Größter Messwert:\t", max(mr, key=lambda x: x.temperatur))

# ie eingebauten Funktionen min( ) und max( ) unterstützen beide Generatorausdrücke
# als Parameter, das Minimum/Maximum einer Messreihe lässt sich so mit einem min( ) bzw. max(
# )-Aufruf platzsparend hinschreiben. Worin besteht der Vorteil im Vergleich zu einer Lösung mit List
# Comprehension?

# Der Hauptvorteil eines Generatorausdrucks gegenüber einer List Comprehension in diesem Kontext ist die Speichereffizienz. 
# Ein Generatorausdruck erzeugt die Elemente 'on-the-fly', d.h. die Elemente werden nacheinander berechnet und nicht alle auf einmal im Speicher abgelegt.
# Eine List  Comprehension hingegegn erstellt zuerst eine Liste im SPeicher, bevor sie weiterverarbeitet wird.
# Bei großen Datenmengen kann dies zu einem Speicherüberlauf führen.
# Da min() und max() direkt mit Generatorausdrücken arbeiten können, entfällt der zusätzliche Schritt des Erstelles der Liste, was die Performance verbessern kann.
# Außerdem sind Generatorausdrücke in der Regel schneller als List Comprehensions, da sie nur die Elemente berechnen, die tatsächlich benötigt werden und
# besser lesbar sind.

# Zu welchem Zeitpunkten (Liste) lag die Temperatur über 33 Grad?
print("Zeitpunkte mit Temperatur > 33 Grad:", [mw.zeitpunkt for mw in mr if mw.temperatur > 33])

# Wie oft war es 2017 wärmer als 26 Grad?
print("Anzahl Tage mit Temperatur > 26 Grad:", len([mw for mw in mr if  mw.temperatur > 26 and mw.zeitpunkt.startswith('2017')]))

# Wann lag die Temperatur zum letzten Mal bei 17 Grad, wenn man Nachkommastellen weglässt
print("Letztes mal 17 Grad:", max([mw for mw in mr if int(mw.temperatur) == 17], key=lambda z:z.zeitpunkt))

# Was ist der Mittelwert der Temperaturen aus den letzten drei Monaten des Jahres 2017? (arithmetisches Mittel)
ls = list(filter(lambda t:t.zeitpunkt > '2017-10' and t.zeitpunkt < "2018", mr))
print("Erster Messwert:", ls[0])
print("Letzter Messwert:", ls[-1])
print(reduce(lambda x, y: x + y.temperatur, ls, 0)/len(ls))