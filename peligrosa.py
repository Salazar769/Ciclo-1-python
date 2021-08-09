import math
import operator

from pyparsing import (Regex,Literal,Word,Group,Forward,alphas,alphanums,delimitedList,ParseException,CaselessKeyword,Suppress)

contenido = []

def primer_dato(datos_):
    contenido.append(datos_[0])

def datos_unarios (datos_):
    for i in datos_:
        if i == "-":
            contenido.append("unary -")
        else:
            break

validar = None

def validacion():
    global validar
    if not validar:
        pi = CaselessKeyword("PI")
        e = CaselessKeyword("E")

        fnumber = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?")
        ident = Word(alphas, alphanums + "_$")

        plus, minus, mult, div = map(Literal, "+-*/")
        lpar, rpar = map(Suppress, "()")
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")

        expr = Forward()
        expr_list = delimitedList(Group(expr))

        def insert_fn_argcount_tuple(t):
            fn = t.pop(0)
            argumentos_numericos = len(t[0])
            t.insert(0, (fn, argumentos_numericos))

        fn_call = (ident + lpar - Group(expr_list) + rpar).setParseAction(
            insert_fn_argcount_tuple
        )
        atom = (
            addop[...]
            + (
                (fn_call | pi | e | fnumber | ident).setParseAction(primer_dato)
                | Group(lpar + expr + rpar)
            )
        ).setParseAction(datos_unarios)

        factor = Forward()
        factor <<= atom + (expop + factor).setParseAction(primer_dato)[...]
        term = factor + (multop + factor).setParseAction(primer_dato)[...]
        expr <<= term + (addop + term).setParseAction(primer_dato)[...]
        validar = expr
    return validar

def validar_cont(s):
    op, argumentos_numericos = s.pop(), 0
    if isinstance(op, tuple):
        op, argumentos_numericos = op
    if op == "unary -":
        return -validar_cont(s)
    if op in "+-*/^":
        op2 = validar_cont(s)
        op1 = validar_cont(s)
        return opn[op](op1, op2)
    elif op == "PI":
        return math.pi
    elif op == "E":
        return math.e
    elif op in fn:
        args = reversed([validar_cont(s) for _ in range(argumentos_numericos)])
        return fn[op](*args)
    elif op[0].isalpha():
        raise Exception("identificador no válido '%s'" % op)
    else:
        try:
            return int(op)
        except ValueError:
            return float(op)

opn = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv}

fn = {
    "sqroot": math.sqrt,
    "sqr": lambda a: a**2,
    "mult": lambda a, b: a * b,
    "div": lambda a, b: a / b,
    "mod": lambda a,b: a%b,
    "fact": math.factorial,
    "sen": lambda a: math.sin(((a*math.pi)/180)),
    "cos": lambda a: math.cos(((a*math.pi)/180)),
    "tan": lambda a: math.tan(((a*math.pi)/180))}



if __name__ == "__main__":
    def impresion(s):
        contenido[:] = []
        if s != "quit":
            try:
                results = validacion().parseString(s, parseAll=True)
                val = validar_cont(contenido[:])
            except ParseException as pe:
                print("ERROR! Expresion no valida")
            except Exception as e:
                print("ERROR! Expresion no valida")
            else:
                print("respuesta >> ", val)
        else:
            "quit"
            
    menu = ""
    while menu != "quit":
        menu = input("Calculadora >> ")
        impresion(menu)
    print("Saliendo...")
    print("Gracias por usar nuestra calculadora.")