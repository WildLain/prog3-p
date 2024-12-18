#Schreiben Sie folgende for-Schleife als while-Schleife um.
# lst = [1,2,3] for e in lst:
# print(e)

lst = [1,2,3]
i = 0
while i < len(lst):
    print(lst[i])
    i = i+1

# Schreiben Sie folgende while-Schleife als for-Schleife um.
# m = [5,3,6,8,1] i=0
# while i < len(m):
#         z = m[i]
#         print(z, "hoch zwei ist", z**2)
#         i = i+1

m = [5,3,6,8,1]
for e in m:
    print(e, "hoch zwei ist", e**2)

