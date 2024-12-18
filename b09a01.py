#Aufgabe 1 (List Comprehension)

# a)
print("a) List Comprehension")
print("I:  ",     [i**3 for i in range(1,11) if i%2==0])
print("II :",    [[z for z in range(2,y) if y % z == 0] for y in [123,12345,123456]])
print("II :",    [z for y in [123, 12345, 123456] for z in range(2,y) if y%z == 0 ])
print("III:",   [p for p in range(10000, 10101) if sum([t for t in range(2,p) if p%t == 0]) ==0])

# b)
print("b) Functional Programming")
print("I:  ",    list(filter(lambda x: x%2 == 0,map(lambda x:x**3, range(1,11)))))
print("II: ",   list(map(lambda y: list(filter(lambda z: y % z == 0, range(2, y))), [123, 12345, 123456])))
print("III:", list(filter(
    lambda p: sum(filter(lambda t: p%t == 0, range(2,p))) == 0,
    range(10000,10101)
)))
