# unter Linux befinden sich im Ordner /etc eine Reihe von Konfigurationsdateien, 
# von denen einige mit .conf enden. Schreiben Sie unter Verwendung von List-Comprehension einen Python-Ausdruck, 
# der eine Liste Namen der drei grö0ten conf-Dateien liefert

# Hinweis: Sie können Ihr Ergebnis mit folgendem Linux-Kommando überprüfen:
# ls -rSl /etc/*.conf | tail -3

import glob
import os.path

# os.path.gestsize(dateipfad)

res = sorted([f for f in glob.glob("/etc/*.conf")], key=lambda file:os.path.getsize(file))[-3:]
print(res)

