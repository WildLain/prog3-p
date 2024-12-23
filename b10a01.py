class Messwert:
    def __init__(self, *args):
        if len(args) == 1:
            self.zeitpunkt  = str(args[0].split(',')[0]).strip('"')
            self.temperatur = float(args[0].split(',')[1])
        elif len(args) == 2:
            self.zeitpunkt = str(args[0])
            self.temperatur = float(args[1])
        else:
            raise ValueError("Falsche Anzahl an Argumenten")
    def __repr__(self):
        return f"Messwert(\'{self.zeitpunkt}\', {self.temperatur})"
    def __eq__(self, other):
        return self.zeitpunkt == other.zeitpunkt and self.temperatur == other.temperatur
    def __lt__(self, other):
        if self.zeitpunkt == other.zeitpunkt:
            return self.temperatur < other.temperatur
        return self.zeitpunkt < other.zeitpunkt
    def __hash__(self):
        return hash((self.zeitpunkt, self.temperatur))


# line = '"2013-07-15 16:03:08.260597",19.875'
# mw = Messwert(line)
# print(mw.zeitpunkt, mw.temperatur)
# mw = Messwert('2013-07-15 16:03:08.260597', 19.875)
# print(mw.zeitpunkt, mw.temperatur)
# print(mw)
# print(eval(repr(mw))== mw)


# mws = [Messwert("2013-07-15 23:45:01.439331",18.9375), 
#        Messwert("2013-07-15 19:45:02.073782",19.0625), 
#        Messwert("2015-08-21 06:45:01.484487",23.75), 
#        Messwert("2014-11-14 03:30:01.987710",20.9375)]
# new = sorted(mws)
# [print(n) for n in new]

mw1 = Messwert("2013-07-15 19:45:02.073782",19.0625)
mw2 = Messwert("2015-08-21 06:45:01.484487",23.75) 

mset = {mw1, mw2}
print(len(mset))
