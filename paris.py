
def isPair(lista):
    if len(lista) == 2:
        return True
    return False

def pairToString(lista2):
    if isPair(lista2):
        return f"({lista2[0]},{lista2[1]})"
    return "No jalo"


def displayList(listaPar):
    final = [True if len(i) == 2 else False for i in listaPar]
    for j in final:
        if j:
            texto = ""
            texto += f" {listaPar[j]}"
            return texto
        return "No jalo"

 
juana = [2,5]
juana2 = [[1,2],[3,4,5], [5,6]]

print(isPair(juana))
#print(pairToString(juana))
#print(displayList(juana2))
