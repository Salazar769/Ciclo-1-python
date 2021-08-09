"""
Haga un programa que dados dos números despliegue que número es mayor.
	Ejemplo:
		Ingrese un numero: 15
		Ingrese otro numero: 45
		El numero mayor es: 45
"""
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

if num1 > num2: 
    print(f"El numero mayor es: {num1}")
elif num2 > num1:
    print(f"El numero mayor es: {num2}")  