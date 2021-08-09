import re

def stringMatcher():
    patron = re.compile("a*b?")
    s = input("ingrese string a hacer match: ")
    match = patron.fullmatch(s)
    if match :
        print("si hace match")
    else:
        print("no hace match")


stringMatcher()

