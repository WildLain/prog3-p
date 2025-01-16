# Schreiben Sie bitte reguläre Ausdrücke zum Matchen folgender Arten von Zeichenketten.

# • Datum in der Form TT.MM.JJJJ, (Tag.Monat.Jahr)
# ([3][01]|[0-2][\d]\.)([0][\d]|[1][1-2]\.)([\d]{4})

# • Euro-Beträge: Optional mit durch Leerzeichen getrenntem EUR dahinter. Beträge haben mindestens
# eine Vorkommastelle und optionale, durch Komma getrennte Nachkommastellen (genau zwei). Der
# Punkt ist als Tausender-Separator erlaubt, also “17.342.915”, “23,56 EUR”, “1425,40 EUR”
# oder “1.234,56”, nicht aber “1.2.3,56” oder “123.45,97765”.
# ^([1-9]{1,3}\.?)([1-9]{2,3}\.?)*(,\d{2})(\sEUR)?$

# • Telefonnummern: Optional mit Länderkennung (z.B. +49) durch Leerzeichen abgesetzt und ohne 0 bei
# der Vorwahl. Als Trennzeichen sind Leerezeichen, / und - erlaubt. Zwischen zwei Trennzeichen sind
# mindestens 2 Ziffern notwendig.

# ^(\+\d{2}[\s/-])[^0](\d{2,}([\s/-]?))*$