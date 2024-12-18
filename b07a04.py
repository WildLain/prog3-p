def devocalize(s):
    "nimm string s und entferne die Vokale"
    res = ""
    for c in s:
        if c not in "aeiou":
            res = res + c
    return res

print(devocalize("Das ist ein Baerenspass"))
help(devocalize)