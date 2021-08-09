"""
Haga una función llamada promedio que reciba de parámetro una lista de números y devuelva el promedio de los mismos.
	Ejemplo:
		lista = [42, 90, 18, 95, 78, 38, 98, 12, 68]
		prom = promedio(lista)
		print("Promedio:", prom)
		# imprime Promedio: 59.888888888888886
"""

lista = [42,90,18,95,78,38,98,12,68]

def promedio(datos):
    salazar = 0
    for i in datos:
        salazar += i
    return salazar/len(datos)
  
prom = promedio(lista)
print(f"Promedio: {prom}")