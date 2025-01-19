import re

def isHawaiian(w):
    # mehrere Vokale hintereinander erlaubt! Pattern GENAU anschauen T_T
    pattern = r'^([aeiou]*[hklmnpw][aeiou]+)*(\'[aeiou]*[hklmnpw]*[aeiou])*$'
    match = re.match(pattern, w, re.IGNORECASE)
    result = bool(match)
    # print(f'Uebergeben: {w:25s} Match: {match.group() if match else "":25s} Result: {result}')        
    return result

def extractHi(iterable):
    for sentence in iterable:
        words = re.findall(r'[\w\']+', sentence, re.IGNORECASE)  # Extrahiere Wörter ohne Satzzeichen
        for word in words:
            if isHawaiian(word):
                yield word

if __name__=="__main__":
    isHawaiian("Aloha")
    isHawaiian("Hawai'i")
    isHawaiian("Wahine")
    isHawaiian("wikiwiki")
    isHawaiian("Humuhumunukunukuapua'a")

    isHawaiian("Qui'juno")
    isHawaiian("Alaaf")
    isHawaiian("lekker")
    isHawaiian("Pu'kuuli")
    isHawaiian("ohamak'uluu")
    it = extractHi(["Eine Wahine sagt", "Maika'i no au!"])
    for i in it: 
        print(i)

    it = extractHi(("Hau'oli", "la hanau!", "Happy", "Birthday!"))
    for i in it:
        print(i)
