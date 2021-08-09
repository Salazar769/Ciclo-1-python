"""
Haga un programa que calcule el área y perímetro de un cuadrado tomando como entrada la base y la altura.
	Ejemplo:
		Ingrese la base: 10
		Ingrese la altura: 5
		Area: 50
		Perimetro: 30

"""
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))

print("Area: " + str((base*altura)))
print("Perimetro: " + str((2*base+2*altura)))