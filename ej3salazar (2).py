def crear(**x):
    return x

def recorrerListaDict(lista, nombre):
    paso = 0
    for i in lista:
        if i["Usuario"] != nombre:
            pass
        else:
            print(i["Usuario"] + " --> " + i["Contraseña"] + "\n\n\n")
            paso = 1
    if paso == 0:
        print("No existe\n\n")

def imprimirTodo(lista):
    for i in lista:
        print("\n" +i["Usuario"] + " --> " + i["Contraseña"])
    print("\n")


def cambiarcontraseña(lista, nombreCambiar, nuevoNombre):
    salazar = 0
    for i in lista:
        if i["Usuario"] != nombreCambiar:
            pass
        else:
            i["Contraseña"] = nuevoNombre
            salazar = 1
    if salazar == 0:
        print("No existe\n\n")

diccionario = []
#diccionario = [{'Usuario': 'salazar', 'Contraseña': '128731kbjn'}, {'Usuario': 'Javier', 'Contraseña': '817231kb'}]
usuarioExistentes = []

usuarioExistentes.clear()
for i in diccionario:
    usuarioExistentes.append(i["Usuario"])

while True:
    print("1. Desplegar")
    print("2. Agregar nuevo estupido")
    print("3. Cambiarle contraseña a un mula")
    print("4. Busqueda de usuario")
    print("5. Salir")
    opcion = int(input("QUE QUIERE MIERDA: "))
    print("\n")
    if opcion == 1:
        if diccionario != []:
            imprimirTodo(diccionario)
        elif diccionario == []:
            print("\nNO HAY NI VERGA MIERDA\n")
    elif opcion == 2:
        w = input("ingrese su puto usuario de mierda: ")
        if w not in usuarioExistentes:
            z = input("ingrese su contraseña culera: ")
            resultado = crear(Usuario= w, Contraseña= z)
            diccionario.append(resultado)
            usuarioExistentes.clear()
            for i in diccionario:
                usuarioExistentes.append(i["Usuario"])
            print("\n")
        elif w in usuarioExistentes:
            print("El usuario ya existe\n")
            print("Desea agregar un nuevo usuario")
            h = input("1. Si\n2. No\n")
            if h == 1:
                w = input("ingrese su puto usuario de mierda: ")
                z = input("ingrese su contraseña culera: ")
            else:
                pass
        else:
            break
    elif opcion == 3:
        cambiar = input("A que usuario le desea cambiar contraseña: ")
        if cambiar not in usuarioExistentes:
            print("\n\nEl usuario no existe\n\n")
        else:
            nuevo = input("Ingrese la nueva contraseña: ")
            cambiarcontraseña(diccionario, cambiar, nuevo)
            print("La contraseña se cambio con exito")
        
    elif opcion == 4:
        nombreBusc = input("Nombre para buscar: ")
        print("\n")
        recorrerListaDict(diccionario, nombreBusc)
    elif opcion == 5:
        print("se está saliendo del programa....")
        break
        #exit()
    else:
        print("\nNo sea mula ingrese una opcion valida\n")

