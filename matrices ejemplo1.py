var = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

var2 = []
cont = 0 
while cont <= 9:
    var2.append(cont)
    cont += 1

print(var2)

var3 = [
    [0,1, 2],
    [3, 4, 5],
    [6, 7, 8],
]

print(var3[1])
var3[1][2] = "X"
print(var3)

def printMatriz(matriz):
    for fila in matriz:
        for columna in fila:
            print(columna, end= " - "
        print()

print Matriz(var3)

