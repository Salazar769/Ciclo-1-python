valor = input("Ingrese su operacion: ").split(" ")

try:
    if valor[1] == "+":
        resultado = (int(valor[0]) + int(valor[2]))
        print(f"El resultado es: {resultado}")
        
    elif valor[1] == "-":
        resultado = (int(valor[0]) - int(valor[2]))
        print(f"El resultado es: {resultado}")
    
    
    elif valor[1] == "*":
        resultado = (int(valor[0]) * int(valor[2]))
        print(f"El resultado es: {resultado}")
    
    
    elif valor[1] == "/":
        resultado = (int(valor[0]) / int(valor[2]))
        print(f"El resultado es: {resultado}")
    else:
        print("Error! expresión inválida. ")
except IndexError:
    print("Error! expresión inválida. ")

