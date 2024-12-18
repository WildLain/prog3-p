# def ggTr(x,y):
#     if y == 0:
#         return x
#     else:
#         r = x % y
#         x = y
#         y = r
#         return ggTr(x, y)

def ggTr(x,y):
    if x == y:
        return x
    else:
        if y > x:
            return ggTr(y-x, x)
        else:
            return ggTr(x-y, y)

def ggT(x,y):
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

# print(ggTr(30,10))
# print(ggTr(20,30))
# print(ggTr(2,5))
# print(ggTr(8,6))
# print(ggTr(7,3))

# print(ggT(30,10))
# print(ggT(20,30))
# print(ggT(2,5))
# print(ggT(8,6))
# print(ggT(7,3))

def readFile():
    for i,line in enumerate(open("ggtbeispiele.txt", "r")):
        x,y,z = line.split()
        res = ggT(int(x), int(y))
        if res != int(z):            
            print("Zeile: {0:2d} Funktion: {1:2d} File: {2:2d}".format(i, res, int(z)))

readFile()

def ggTl(a,b, *c):
    for el in c:
        a = ggT(a, b)
        res =ggT(a, el)
    print("Ergebnis:",res)
    return res

ggTl(10,80,20,75)
ggTl(7,2,2,1,20,11)