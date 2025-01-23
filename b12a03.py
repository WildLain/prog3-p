import sys
import re

# die Internet-Adresse (IP-Adresse) des abrufenden Rechners,
# den Zeitpunkt des Abrufs (Datum/Uhrzeit/Zeitzone),
# die eigentliche HTTP-Anfrage (aus HTTP-Methode wie GET, HEAD oder POST, den Pfad zu der ab-
# gerufenen Ressource/Datei und Protokollversion) und die Bezeichnung des verwendeten Clients (z.B.
# Web-Browsers)

if len(sys.argv) != 2:
    print("Usage: python3 b12a03.py <logfile>")
    sys.exit(1)
else:
    filepath: str = sys.argv[1]

# ipRgx:      re.Pattern[str] = re.compile(r"\b\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\b")
# timeRgx:    re.Pattern[str] = re.compile(r"\b([0][1-9]|[1-2][\d]|[3][0-1])/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}\b")
# getRgx:      re.Pattern[str] = re.compile(r"\bGET [\w~\-/]+\.(png|jpg|gif)\b")


ipRgx:      re.Pattern[str]  = re.compile(r"\b\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\b")
timeRgx:    re.Pattern[str]  = re.compile(r"\b(?P<tag>[0][1-9]|[1-2][\d]|[3][0-1])/(?P<monat>\w{3})/(?P<jahr>\d{4}):(?P<stunden>\d{2}):(?P<minuten>\d{2}):(?P<sekunden>\d{2}) \+\d{4}\b")
picsRgx:    re.Pattern[str] = re.compile(r"\bGET [\w~\-/]+\.(?P<filetype>png|jpg|gif)\b", re.IGNORECASE)

count = 0
pics_dict = { 'jpg' : 0, 'png' : 0, 'gif' : 0}
hourly_access = {f'{hour:02d}' :  0 for hour in range(24)}
with open(filepath) as file:
    for line in file:
        # Anzahl der Bilder je Dateityp
        picsMatch:  re.Match[str] | None = picsRgx.search(line)
        if picsMatch is not None:
            filetype = picsMatch.group('filetype')
            pics_dict[filetype.lower()] += 1
        
        # Nach Stunden verteilte Zugriffe
        timeMatch:  re.Match[str] | None = timeRgx.search(line)  
        if timeMatch is not None:
            hour =  timeMatch.group('stunden')
            hourly_access[hour] += 1            
    
    # print(pics_dict)
    # print(hourly_access)
    total_accesses = sum(hourly_access.values())
    hourly_percentages = { hour : "{:.2f} %".format((count/total_accesses) * 100) for hour, count in hourly_access.items()} 
    [print(f'Stunde: {hour:2s} Prozent: {percentage}') for hour, percentage in hourly_percentages.items()]  
    # print(f'jpgs: {pics_dict['jpg']:2d} pngs: {pics_dict['png']:2d} gifs: {pics_dict['gif']:2d}')
    # ipMatch:    re.Match[str] | None = ipRgx.search(line)  