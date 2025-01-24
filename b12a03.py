import sys
import re
import socket

if len(sys.argv) != 2:
    print("Usage: python3 b12a03.py <logfile>")
    sys.exit(1)
else:
    filepath: str = sys.argv[1]
    
ipRgx:      re.Pattern[str] = re.compile(r"\b\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}\b")
timeRgx:    re.Pattern[str] = re.compile(r"\b(?P<tag>[0][1-9]|[1-2][\d]|[3][0-1])/(?P<monat>\w{3})/(?P<jahr>\d{4}):(?P<stunden>\d{2}):(?P<minuten>\d{2}):(?P<sekunden>\d{2}) \+\d{4}\b")
picsRgx:    re.Pattern[str] = re.compile(r"\bGET [\w~\-/]+\.(?P<filetype>png|jpg|gif)\b", re.IGNORECASE)
addRgx:     re.Pattern[str] = re.compile(r"\b[^w{3}.][\w\-.]+.\w{2}\b")

count = 0
pics_dict:      dict[str, int] = { 'jpg' : 0, 'png' : 0, 'gif' : 0}
hourly_access:  dict[str, int] = {f'{hour:02d}' :  0 for hour in range(24)}
with open(filepath) as file:
    for line in file:
        # Anzahl der Bilder je Dateityp
        picsMatch:  re.Match[str] | None = picsRgx.search(line)
        if picsMatch is not None:
            filetype: str = picsMatch.group('filetype')
            pics_dict[filetype.lower()] += 1
        
        # Nach Stunden verteilte Zugriffe
        timeMatch:  re.Match[str] | None = timeRgx.search(line)  
        if timeMatch is not None:
            hour: str =  timeMatch.group('stunden')
            hourly_access[hour] += 1
        
        

hostname =   socket.gethostbyaddr('195.72.105.32')[0]
match = addRgx.search(hostname)
if match is not None:
    print(match.group())
print(hostname)
    # print(f'jpgs: {pics_dict['jpg']:2d} pngs: {pics_dict['png']:2d} gifs: {pics_dict['gif']:2d}')
    
    # total_accesses = sum(hourly_access.values())
    # hourly_percentages = { hour : ((count/total_accesses) * 100) for hour, count in hourly_access.items()} 
    # [print(f'Stunde: {hour:2s} Prozent: {percentage:.2f} %') for hour, percentage in hourly_percentages.items()]