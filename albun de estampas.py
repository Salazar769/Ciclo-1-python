import random

estampitas = ['X', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
comparacion = ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']

def imprimir():
    temp = 1
    for i in range(10):
        print( str(estampitas[temp]) + " - " + str(estampitas[temp+1]) + " - " + str(estampitas[temp+2]) + " - " + str(estampitas[temp+3]) + " - " + str(estampitas[temp+4]) + " - " + str(estampitas[temp+5]) + " - " + str(estampitas[temp+6]) + " - " + str(estampitas[temp+7]) + " - " + str(estampitas[temp+8]) + " - " + str(estampitas[temp+9]))
        temp += 10
    
def aleatorio():
    x = random.randint(1,100)
    if x not in estampitas:
        print(f"Obtuve la estampita: {x}")
        print("Ya tengo esta estampita\n")
    else:
        estampitas[x] = "X"
        print(f"Obtuve la estampita: {x}")
        print("Acabo de obtener una estampita\n")
    imprimir()

imprimir()
infinito = input()
salazar = True

while salazar:
    if infinito == "":
        aleatorio()
        infinito = input()
        if estampitas == comparacion:
            salazar = False
        else:
            pass
    else:
        pass
print("Ya está lleno el album")