# Schreiben Sie bitte reguläre Ausdrücke zum Matchen folgender Arten von Zeichenketten.

# • Datum in der Form TT.MM.JJJJ, (Tag.Monat.Jahr)

# • Euro-Beträge: Optional mit durch Leerzeichen getrenntem EUR dahinter. Beträge haben mindestens
# eine Vorkommastelle und optionale, durch Komma getrennte Nachkommastellen (genau zwei). Der
# Punkt ist als Tausender-Separator erlaubt, also “17.342.915”, “23,56 EUR”, “1425,40 EUR”
# oder “1.234,56”, nicht aber “1.2.3,56” oder “123.45,97765”.

# • Telefonnummern: Optional mit Länderkennung (z.B. +49) durch Leerzeichen abgesetzt und ohne 0 bei
# der Vorwahl. Als Trennzeichen sind Leerezeichen, / und - erlaubt. Zwischen zwei Trennzeichen sind
# mindestens 2 Ziffern notwendig.


import re

dateRgx = re.compile(r'^([3][01]|[0-2][\d])\.([0][\d]|[1][1-2])\.([\d]{4})$')
euroRgx = re.compile(r'^[1-9]{,3}\.?(\d*|.\d{3})*(,\d\d)?( EUR)?$')
teleRgx = re.compile(r'^(\+\d\d |[^0])?([\d]|[\d]{2,}[ /\-])*$')
emailRgx = re.compile(r'^[\w\.-]*@[\w-]+\.\w{2,}$')

patterns = [dateRgx, euroRgx, teleRgx]

data = [line.split() for line in open('daten-regulaere-ausdruecke.txt')]
# [print(d) for d in data]
for entry in data:  
    val = ' '.join(entry[1:-1]).strip()
    if entry[0] == 'PLZ':
        pattern = r'\d{5}'
    elif entry[0] == 'Datum':
        pattern = dateRgx
    elif entry[0] == 'EUR':
        pattern = euroRgx
    elif entry[0] == 'Tel':
        pattern = teleRgx
    elif entry[0] == 'Email':
        pattern = emailRgx
    match = re.search(pattern, val)
    if match is not None:
        print(match.group(), entry[-1])