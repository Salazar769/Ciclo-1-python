#####################################
#
# Autor: Javier Salazar
#
#####################

import re

def stringMatcher(name, number):
    texto = re.compile("[A-Z][a-z]+\s[A-Z][a-z]+")
    encaje = texto.fullmatch(name)
    if encaje:
        texto2 = re.compile("[0-9]+")
        encaje2 = texto2.fullmatch(number)
        if encaje2:
            contador = len(number)
            if contador == 7:
                return(f"Cuenta de ahorro: {number}")
            elif cuenta == 10:
                return(f"Cuenta de deposito: {number[:3]} - {number[3:8]} - {number[8:10]} ")
            else:
                return("El numero de cuenta no es valido.")
        else:
            return("El nombre ingresado no es valido.")

nombreApellido = input("Ingrese  Apellido: ")
numCuenta = input("Ingrese no. de cuenta: ")


print(stringMatcher("Javier Chavez", "1238901"))