
"""Realizr una programa para crear la clase Calcular, ingresa los atributos
necesarios. Utilice el método constructor. Agregaremos el soporte 
adecuado para operaciones matemáticas del atributo utilizando la 
sobrecarga de operadores. 
    Realizar la sobrecarga de operadores de multiplicación, resta,
    división y modulo. 
Recuerde que todos los métodos se muestran por medio del objeto, se
muestran los resultados obtenidos"""

class Calcular:
    def __init__(self, a_1):
        self.a_1 = a_1 

    def __mul__(self, num_2):
        return self.a_1 * num_2

    def __sub__(self,num_2):
        return self.a_1 - num_2

    def __divmod__(self, num_2):
        return self.a_1 / num_2
    
    def __mod__(self, num_2):
        return self.a_1 % num_2

calc = Calcular(5)
print("El valor de la multiplicación es: ", calc * 12)
print("El valor de la resta es: ", calc - 23)
print("El valor de la división es: ", calc / 2)
print("El valor del modulo es igual a: ", calc % 7)
