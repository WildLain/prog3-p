import sys
import re
import socket

if len(sys.argv) != 2:
    print("Usage: python3 b12a03.py <logfile>")
    sys.exit(1)
else:
    filepath: str = sys.argv[1]

dataRgx:    re.Pattern[str] = re.compile(r"(?P<ip>\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)|"
                                         r"(?P<timestamp>\b(?P<tag>[0][1-9]|[1-2][\d]|[3][0-1])/(?P<monat>\w{3})/(?P<jahr>\d{4}):(?P<stunden>\d{2}):(?P<minuten>\d{2}):(?P<sekunden>\d{2}) \+\d{4}\b)|"
                                         r"(?P<pics>\bGET [\w~\-/]+\.(?P<filetype>png|jpg|gif)\b)", re.IGNORECASE)

pics_dict:      dict[str, int] = { 'jpg' : 0, 'png' : 0, 'gif' : 0}
hourly_access:  dict[str, int] = {f'{hour:02d}' :  0 for hour in range(24)}
cache = {}
requests = {}
weird = []

with open(filepath) as file:
    lines = file.readlines()
for line in lines:
    print(f'Processing line: {line}')
    match = dataRgx.search(line)
    if match:
        ipMatch = match.group('ip')
        if ipMatch:
            if ipMatch not in cache:
                try:
                    host = socket.gethostbyaddr(ipMatch)[0]
                    hostname = '.'.join(host.split('.')[-2:])
                    if hostname == '.':
                        weird.append(line)
                except Exception:
                    hostname = 'unknown host'
                cache[ipMatch] = hostname
            hostname = cache[ipMatch]
            if hostname not in requests:
                requests[hostname] = 0
            requests[hostname] += 1
        
        picsMatch = match.group('pics')
        if picsMatch:
            filetype = match.group('filetype').lower()
            pics_dict[filetype] += 1
        
        timeMatch = match.group('timestamp')
        if timeMatch:
            hour = match.group('stunden')
            hourly_access[hour] += 1

# [print(f'{k} {v}') for k,v in requests.items()]
print(weird)
    
# Verteilung der Grafiken
print(f'jpgs: {pics_dict['jpg']:2d} pngs: {pics_dict['png']:2d} gifs: {pics_dict['gif']:2d}')

# Wie verteilt sich insgesamt die Anzahl der Zugriffe anteilig stundenweise über den Tag? (Prozent Zugriffe in der Stunde)
total_accesses = sum(hourly_access.values())
hourly_percentages = { hour : ((count/total_accesses) * 100) for hour, count in hourly_access.items()} 
[print(f'Stunde: {hour:2s} Prozent: {percentage:.2f} %') for hour, percentage in hourly_percentages.items()]


# ipRgx:      re.Pattern[str] = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
# timeRgx:    re.Pattern[str] = re.compile(r"\b(?P<tag>[0][1-9]|[1-2][\d]|[3][0-1])/(?P<monat>\w{3})/(?P<jahr>\d{4}):(?P<stunden>\d{2}):(?P<minuten>\d{2}):(?P<sekunden>\d{2}) \+\d{4}\b")
# picsRgx:    re.Pattern[str] = re.compile(r"\bGET [\w~\-/]+\.(?P<filetype>png|jpg|gif)\b", re.IGNORECASE)
# addRgx:     re.Pattern[str] = re.compile(r"\b([\d\w\-]*[\.])*([\w]+\.[\w]{2,})\b\b")
# with open(filepath) as file:
#     for line in file:
#         print(f'Processing line: {line}')
#         # Anzahl der Bilder je Dateityp
#         picsMatch:  re.Match[str] | None = picsRgx.search(line)
#         if picsMatch is not None:
#             filetype: str = picsMatch.group('filetype')
#             pics_dict[filetype.lower()] += 1
        
#         # Nach Stunden verteilte Zugriffe
#         timeMatch:  re.Match[str] | None = timeRgx.search(line)  
#         if timeMatch is not None:
#             hour: str =  timeMatch.group('stunden')
#             hourly_access[hour] += 1
                         
#         ipMatch: re.Match[str] | None = ipRgx.search(line)
#         if ipMatch is not None:
#             ip = ipMatch.group()
#             if ip not in cache:
#                 try:
#                     host = socket.gethostbyaddr(ip)[0]
#                     hostname = host.split('.')[-2:]
#                     hostname = '.'.join(hostname)
#                 except:
#                     hostname = 'unknown host'            
#             cache[ip] = hostname
#             hostname = cache[ip]
#             if hostname not in requests:
#                 requests[hostname] = 0
#             requests[hostname] += 1