"""
Haga una función llamada substring que reciba de parametro un string, una posición inicial y una posición final y devuelva un nuevo string que contenga los caracteres desde la posición inicial hasta la final sin incluir la posición final. Debe usar ciclos para su solución.
	Ejemplo:
		texto = "Hola mundo"
		texto2 = substring(texto, 1, 6)
		print(texto2)
		# imprime ola m
"""


text = "Hola mundo"
def substring(texto,poso,posf):
    salazar = ""
    for i in texto[poso:posf]:
        salazar += i
    return salazar
        
texto2 = substring(text,1,6)
print(texto2)