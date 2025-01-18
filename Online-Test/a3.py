import re
def isHawaiian(w):
    pattern = r'^([hklmnpw][aeiou]+)+([\'][aeiou])?$' # mehrere Vokale hintereinander erlaubt! T_T
    match = re.match(pattern, w, re.IGNORECASE)
    result = bool(match)        
    print(f'Uebergeben: {w:25s} Match: {match.group() if match else "":25s} Result: {result}')
    return result

if __name__=="__main__":
    isHawaiian("Hawai'i")                   #wahr
    isHawaiian("Wahine")                    #wahr
    isHawaiian("wikiwiki")                  #wahr    
    isHawaiian("Humuhumunukunukuapua'a")    #wahr

    isHawaiian("Qui'juno")      #falsch
    isHawaiian("Alaaf")         #falsch
    isHawaiian("lekker")        #falsch
    isHawaiian("Pu'kuuli")      #falsch
    isHawaiian("ohamak'uluu")   #falsch
