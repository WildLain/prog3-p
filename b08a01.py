def h(a,b,c=1000,*d,**e):
      print(a,b,c,d,e)

tup = ('ene','mene','mu')
kw = { 'x':'iks', 'b':'beh', 'lst':[17,17,17] }

h(17,21),
# 17 21 1000 () {}
# a=17, b=21, c=1000 default Wert, d=() leere Menge, e={} leeres Dict

h(10,20,30),
# 10 20 30 () {}
# c = 30, default-Wert wurde ersetzt

h(1,2,3,4,5,6,x=7, y=22)
# 1 2 3 (4, 5, 6) {'x': 7, 'y': 22}
# a=1, b=2, c=3, *d=(4,5,6) Rest als Menge, **e={'x': 7, 'y': 22} ergibt ein Dict{} 

# h(1,2,3,4,5,6,c=7)
# TypeError: h() got multiple values for argument 'c'
# c=3 und c=7 geht nicht

h(*tup),
# ene mene mu () {}
# a='ene, b='mene', c='mu', d=(), e={}

h(1,2,*tup,3),
# 1 2 ene ('mene', 'mu', 3) {}
# a=1, b=2, c= 'ene' (das erste Element von tup), d= ('mene', 'mu', 3) (alle weiteren Argumente nach den ersten beiden), e={} keine Schlüsselwortargumente übergeben
# Die Elemente von tup werden entpackt und als zusätzliche Argumente übergeben:
# c= Das erste Element von tup, also 'ene', wird als drittes Argument übergeben und ersetzt somit den Standardwert von c.
# d= Die restlichen Elemente von tup, also 'mene' und 'mu', werden als zusätzliche Argumente in ndas Tupel d aufgenommen. Schließlich wird 3 als weiteres Argument übergeben.

h(10, **kw)
# a=10, b='beh', c=1000, d=(), e={'x': 'iks', 'lst': [17, 17, 17]}
# b='beh', da das Dictionary 'kw' den Schlüssel 'b' hat, wird der Wert 'beh' diesem Parameter zugewiesen
# e={'x': 'iks', 'lst': [17, 17, 17]}, die restlichen Elemente im Dictionary, die nicht als Parameter verwendet wurden, werden in das Dictionary aufgenommen


h(10,20,*tup, **kw)
# TypeError: h() got multiple values for argument 'b'
# Schlüssel b gibt es im Dictionary kw und versucht Argument b zuzuweisen, wurde aber schon mit 20 gesetzt und kann nicht doppelt zugewiesen werden