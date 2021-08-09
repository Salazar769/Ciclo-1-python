"""
Miguel Angel Aquino González
Programación para la ciencia y la ingeniería
13-04-2021
"""
def menu():
        print("- - - - CALCULADORA GEOMETRICA - - - -")
        print("1. para hallar el area de un círculo ")
        print("2. para hallar el area y el volumen de un cono ")
        print("3. para hallar el area y volumen de una esfera ")
        print("4. para hallar el area de un segmento ")
        print("5. para hallar el area de un sector ")
        print("6. para hallar el area de un cilindro ")
        print("7. salir ")



from math import*

def circulo(r):
        s=pi*r**2
        return s

def cono(r,h):
    g=((r**2)+(h**2))**0.5
    s=pi*r*g+pi*r**2
    v=pi*r**2*h
    return [s,v]

def esfera(r):
        s=4*pi*r**2
        v=4*pi*r**3/3
        return [s,v]

def segmento(r,a):
        s=r**2*(pi*a-0.5*sin(a))
        return s

def sector(r,a):
        s=pi*r**2*a
        return s

def cilindro(r,h):
        s=2*pi*r*(r+h)
        return s

while True:
        menu()
        opc=int(input("Elija la opción 1,2,3,4,5,6: "))
        if opc==1:
                r=float(input("Ingrese valor del radio: "))
                circulo(r)
                print(circulo(r))
        if opc==2:
                r=float(input("Ingrese valor del radio: "))
                h=float(input("Ingrese la altura "))
                cono(r,h)
                print(cono(r,h))
        if opc==3:
                r=float(input("Ingrese valor del radio: "))
                esfera(r)
                print(esfera(r))
        if opc==4:
                r=float(input("Ingrese valor del radio: "))
                a=float(input("ingrese valo de a: "))
                segmento(r,a)
                print(segmento(r,a))

        if opc==5:
                r=float(input("Ingrese valor del radio: "))
                a=float(input("ingrese valo de a: "))
                sector(r,a)
                print(sector(r,a))
        if opc==6:
                r=float(input("Ingrese valor del radio: "))
                h=float(input("Ingrese la altura "))
                cilindro(r,h)
                print(cilindro(r,h))
                
                break
        else:
                print("opcion incorrecta debe ingresar 1,2,3,4,5 o 6")

