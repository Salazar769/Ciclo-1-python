#1

"""
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

print("Area: " + str((base*altura)))
print("Perimetro: " + str((2*base+2*altura)))
"""

#2

"""
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 > num2: 
    print(f"El numero mayor es: {num1}")
elif num2 > num1:
    print(f"El numero mayor es: {num2}")  
"""

#3

"""
fecha1 = int(input("Ingrese año 1: "))
fecha2 = int(input("Ingrese año 2: "))
print(f"Resultado: {abs(fecha2-fecha1)}")
"""

#4

"""
text = "Hola mundo"
def substring(texto,poso,posf):
    salazar = ""
    for i in texto[poso:posf]:
        salazar += i
    return salazar
        
texto2 = substring(text,1,6)
print(texto2)
"""

#5

"""
lista = [42,90,18,95,78,38,98,12,68]

def promedio(datos):
    salazar = 0
    for i in datos:
        salazar += i
    return salazar/len(datos)
  
prom = promedio(lista)
print(f"Promedio: {prom}")
"""







