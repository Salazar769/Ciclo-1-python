import re
import math
import time


funciones = ['sqroot', 'cos', 'sen', 'tan']
simbolos = ['+', '-']


def sub_remove_parentesis(exp):
    #quita mediante expresiones regulares los parentesis de "exp"
    return re.sub('[()]', '', exp)


def split_en_tokens(exp):
    #separa en tokens (uno o mas caracteres) una expresion, de forma que se puedan agrupar
    #para validarlos en funciones
    token = ''
    token_list = []
    for char in exp:
        if token in funciones:
            token_list.append(token)
            token = ''
        token += char
    token_list.append(token)
    if len(token_list) > 0:
        if token_list[0] not in funciones:
            token_list = []
    return token_list


def prepare_result(token_list, operacion):
    #opera las cadenas almacenadas en el arreglo token_list para que se puedan convertir en la correspondiente operacion
    # aritmetica. Cuando hay 2 valores y una operacion (simbolo) lo operac segun su simbolo
    if operacion != '':
        try:
            if operacion == "+":
                resultado = float(sub_remove_parentesis(token_list[0])) + float(sub_remove_parentesis(token_list[1]))
            elif operacion == '-':
                resultado = float(sub_remove_parentesis(token_list[0])) - float(sub_remove_parentesis(token_list[1]))
            #agregar multiplicacion y division
            return resultado
        except ValueError:
            #si algo falla, se captura el error para que el programa no se interrumpa
            raise SyntaxError("Expresion invalida")
    else:
        # si algo falla, se captura el error para que el programa no se interrumpa
        raise SyntaxError("Expresion invalida")

def operaciones(exp):
    #se separa la expresion en caracteres para que podamos operarlo posteriormente en la funcion "prepare_result"
    # se opera cada dos elementos (de izq a derecha) para facilidad
    token = ''
    operacion = ""
    resultado = 0
    token_list = []
    for char in exp:
        if char in simbolos:
            token_list.append(token)
            token = ''
            try:
                if len(token_list) == 2:
                    resultado = prepare_result(token_list, operacion)
                    token_list = [ str(resultado) ]
                    operacion = ''
            except SyntaxError:
                # si algo falla, se captura el error para que el programa no se interrumpa
                print("Expresion Invalida")
            operacion = char
        else:
            token += char.replace(" ", "")

    token_list.append(token)
    if len(token_list) == 2:
        resultado = prepare_result(token_list, operacion)
    # una vez se obtienen los resultado de todos los numeros se genera el resultado
    return resultado


def op(calculadora):
    val1 = re.compile("[0-9]+")
    val = re.compile("[(].+[)]")
    match = val.findall(calculadora)
    if match:
        #si la expresion tiene parentesis entra aqui 
        func_list = split_en_tokens(calculadora)
        if len(func_list) > 0 : # funciones validas
            funcion = func_list[0]
            value = float(sub_remove_parentesis(func_list[1]))
            if funcion == 'sqroot':
                return print (math.sqrt(value))
            elif funcion == 'sen':
                return print(math.sin(value))
            elif funcion == 'cos':
                return print(math.cos(value))
            elif funcion == 'tan':
                return print(math.tan(value))
            else:
                return print("ERROR! Expresion no valida")
        else:
            try:
                calculadora = sub_remove_parentesis(calculadora)
                return print(operaciones(calculadora))
            except SyntaxError:
                return print("ERROR! Expresion no valida")
    else:
        #si la expresion no tiene parentesis entra aca (unicamente operaciones aritmeticas)
        try:
            return print(operaciones(calculadora))
        except SyntaxError:
            return print("ERROR! Expresion no valida")

print("!BIENVENIDO A LA 'CALCULADORA SIN INTERFAZ' USUARIO")
print("Producida por: Pablo Orozco y asociados")
while True:
    calculadora = input()
    if calculadora.lower() == "quit":
        print("saliendo...")
        #time.sleep(2)
        print("Gracias por usar nuestra calculadora.")
        break
    else:
        op(calculadora)