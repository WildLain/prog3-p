import sys
import re
import socket

if len(sys.argv) != 2:
    print("Usage: python3 b12a03.py <logfile>")
    sys.exit(1)
else:
    filepath: str = sys.argv[1]
    
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
    
    total_accesses = sum(hourly_access.values())
    hourly_percentages = { hour : "{:.2f} %".format((count/total_accesses) * 100) for hour, count in hourly_access.items()} 
    [print(f'Stunde: {hour:2s} Prozent: {percentage}') for hour, percentage in hourly_percentages.items()]  
    # print(f'jpgs: {pics_dict['jpg']:2d} pngs: {pics_dict['png']:2d} gifs: {pics_dict['gif']:2d}')
    # ipMatch:    re.Match[str] | None = ipRgx.search(line)  