def dreh(lst):
    #Rekusriv Liste leeren
    #base case leere Liste
    if lst == []:
        return []
    else:
    #erstes Listenelement merken
        first = lst[0]
    #rest der liste herum drehen
        lst = dreh(lst[1:])
    #gemerktes listenElement an gedrehte Restliste dranhängen
        lst.append(first)
        return lst

print(dreh([1,2,3,4,5,6,7,8,9,10]))