"""
texto = [x for x in input("Input: ") if x in "{}[]()"]
if len(texto) % 2 != 0 or len(texto) == 0:
    validacion = False
else:
    validacion = True
    i = 0
    while 0 < len(texto) and validacion == "YES":
        if texto[i] in "{[(":
            i += 1
        else:
            if texto[i - 1] + texto[i] in '{}' or \
                    texto[i - 1] + texto[i] in '[]' or \
                    texto[i - 1] + texto[i] in '()':
                texto = texto[:i - 1] + texto[i + 1:]
                i -= 1
            else:
                validacion = False
                
print(validacion)
"""

"""
def validacion(texto):
    lista = list(texto)
    comprobacion = []
    contador1 = lista.count('(')
    contador2 = lista.count(')')
    if contador1 != contador2:
        return False
    else:
        for i in lista:
            if i == "(":
                comprobacion.append(i)
            elif i == ")" and len(comprobacion) > 0:
                comprobacion.pop()
    if len(comprobacion) == 0:
        return True

def main():
    ingreso = input("Input: ")
    print(validacion(ingreso))
    
main()
"""
"""
#EL MEJOR

def main():
    print(
        (
            lambda expr, stack: all(
                len(stack) == 0 if char is None else
                stack.append(char) or True if char in '([{' else
                len(stack) > 0 and {'(': ')', '[': ']', '{': '}'}[stack.pop()] == char if char in ')]}' else
                True
                for char in expr
            )
        )(
            list(input("Input: ")) + [None], []
        )
    )
    
main()
"""



#easy
def es_valida(texto):
    def validacion(izq,der):
        if izq=='[' and der==']':
            return True
        if izq=='{' and der=='}':
            return True
        if izq=='(' and der==')':
            return True
        return False
    lista=[]
    for i in range(len(texto)):
        if texto[i]=='[' or texto[i]=='{' or texto[i]=='(':
            lista.append(texto[i])
        elif texto[i] == ']' or texto[i] == '}' or texto[i] == ')':
            if validacion(lista[-1],texto[i] or len(lista)!=0):
                lista.pop()
            else:
                return False
    if len(lista)==0:
        return True
    else:
        return False

def main():
    text = input("Input: ")
    print(es_valida(text))
    
main()
    
   