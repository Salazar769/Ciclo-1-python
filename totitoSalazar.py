#########################################
#
# Autor: Javier Perez asumakina
#
#########################################

interfaz = [" " for i in range(9)]
interfaz_pos = ('1-A', '1-B', '1-C', '2-A', '2-B', '2-C', '3-A', '3-B', '3-C')

def mostrar_datos(datos):
    print("   | A | B | C |")
    print("---+---+---+---+-")
    print("1  | " + datos[0] + " | " + datos[1] + " | " + datos[2] + " | ")
    print("---+---+---+---+-")
    print("2  | " + datos[3] + " | " + datos[4] + " | " + datos[5] + " | ")
    print("---+---+---+---+-")
    print("3  | " + datos[6] + " | " + datos[7] + " | " + datos[8] + " | ")
    print("---+---+---+---+-")

def posicion(ingresoUsuario):
    if ingresoUsuario in interfaz_pos:
        return interfaz_pos.index(ingresoUsuario)

def agregar(signo, pos):
    interfaz[pos] = signo

def hay_espacio(pos):
    return interfaz[pos] == " "

def seleccionAzar(j1, j2):
    import random
    decision = random.randint(1,5)
    if decision == 1 or decision == 3 or decision == 5:
        seleccionado = [j1, j2]
    elif decision == 2 or decision == 4 or decision == 6:
        seleccionado = [j2,j1]
    return seleccionado
    
def jugadaUsuario(user):
    ingreso = input(f"{user[0]} Ingrese en que casilla quiere tirar: FORMATO FILA-COLUMNA  -> ").upper()
    if ingreso in interfaz_pos:
        if hay_espacio(posicion(ingreso)):
            agregar(user[2], posicion(ingreso))
            return True
        else:
            print("\nEsa casilla ya está ocupada no sea meco\n")

    else:
        print("\nIngrese una casilla valida, FORMATO FILA-COLUMNA\n")

def marcarPC(user):
    #global defenderSgn
    import random
    
    movimientosDisponibles = [i for i in interfaz_pos if interfaz[posicion(i)] == " "]
    
    
    esquinasDisponibles = [i for i in movimientosDisponibles if i in ["1-A", "1-C", "3-A", "3-C", "2-B"]]
    cruzDisponibles = [i for i in movimientosDisponibles if i in ['1-B', '2-A', '2-C', '3-B', "2-B"]]
    
    #user[2] = "SIGNO"
    
    if user[2] == "O":
        defenderSgn = [i for i in interfaz_pos if interfaz[posicion(i)] == "X"]

    else:
        defenderSgn = [i for i in interfaz_pos if interfaz[posicion(i)] == "O"]
    
    entro = 0
    if len(defenderSgn) == 2:
        entro = 1
        if set(defenderSgn) == {"1-A", "2-B"}:
            if hay_espacio(posicion("3-C")):
                agregar(user[2], posicion("3-C"))
            else:
                entro = 0
        elif set(defenderSgn) == {"2-A", "2-B"}:
            if hay_espacio(posicion("2-C")):
                agregar(user[2], posicion("2-C"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-C", "2-B"}:
            if hay_espacio(posicion("1-A")):
                agregar(user[2], posicion("1-A"))
            else:
                entro = 0
        elif set(defenderSgn) == {"2-C", "2-B"}:
            if hay_espacio(posicion("2-A")):
                agregar(user[2], posicion("2-A"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-A", "2-B"}:
            if hay_espacio(posicion("1-C")):
                agregar(user[2], posicion("1-C"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-C", "2-B"}:
            if hay_espacio(posicion("3-A")):
                agregar(user[2], posicion("3-A"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-B", "2-B"}:
            if hay_espacio(posicion("3-B")):
                agregar(user[2], posicion("3-B"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-B", "2-B"}:
            if hay_espacio(posicion("1-B")):
                agregar(user[2], posicion("1-B"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-A", "1-B"}:
            if hay_espacio(posicion("1-C")):
                agregar(user[2], posicion("1-C"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-C", "1-B"}:
            if hay_espacio(posicion("3-C")):
                agregar(user[2], posicion("3-C"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-A", "3-B"}:
            if hay_espacio(posicion("3-C")):
                agregar(user[2], posicion("3-C"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-C", "3-B"}:
            if hay_espacio(posicion("3-A")):
                agregar(user[2], posicion("3-A"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-A", "2-A"}:
            if hay_espacio(posicion("3-A")):
                agregar(user[2], posicion("3-A"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-A", "2-A"}:
            if hay_espacio(posicion("1-A")):
                agregar(user[2], posicion("1-A"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-C", "2-C"}:
            if hay_espacio(posicion("3-C")):
                agregar(user[2], posicion("3-C"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-C", "2-C"}:
            if hay_espacio(posicion("1-C")):
                agregar(user[2], posicion("1-C"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-A", "3-C"}:
            if hay_espacio(posicion("2-B")):
                agregar(user[2], posicion("2-B"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-A", "1-C"}:
            if hay_espacio(posicion("2-B")):
                agregar(user[2], posicion("2-B"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-A", "1-C"}:
            if hay_espacio(posicion("1-B")):
                agregar(user[2], posicion("1-B"))
            else:
                entro = 0
        elif set(defenderSgn) == {"2-A", "2-C"}:
            if hay_espacio(posicion("2-B")):
                agregar(user[2], posicion("2-B"))
            else:
                entro = 0
        elif set(defenderSgn) == {"3-A", "3-C"}:
            if hay_espacio(posicion("3-B")):
                agregar(user[2], posicion("3-B"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-A", "3-C"}:
            if hay_espacio(posicion("2-A")):
                agregar(user[2], posicion("2-A"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-B", "3-B"}:
            if hay_espacio(posicion("2-B")):
                agregar(user[2], posicion("2-B"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-A", "3-A"}:
            if hay_espacio(posicion("2-A")):
                agregar(user[2], posicion("2-A"))
            else:
                entro = 0
        elif set(defenderSgn) == {"1-C", "3-C"}:
            if hay_espacio(posicion("2-C")):
                agregar(user[2], posicion("2-C"))
            else:
                entro = 0
    else:
        entro = 0
        #pass
        
    if entro == 0:       
        if len(esquinasDisponibles) > 0:
            ingreso = esquinasDisponibles[random.randint(0,len(esquinasDisponibles)-1)]
            
        elif len(cruzDisponibles) > 0:
            ingreso = cruzDisponibles[random.randint(0,len(cruzDisponibles)-1)]
        else:
            ingreso = ""
            
        if ingreso in interfaz_pos:
            if hay_espacio(posicion(ingreso)):
                agregar(user[2], posicion(ingreso))
            
    return True


def ganadorXO(casillas, comando, ganador):
    #horizontales
    if casillas[0] ==  casillas[1] ==  casillas[2] != " ":    
        comando = True
        ganador = casillas[0]
        return comando, ganador
    
    elif casillas[3] == casillas[4] == casillas[5] != " ":
        comando = True
        ganador = casillas[3]
        return comando, ganador
    
    elif casillas[6] == casillas[7] == casillas[8] != " ":
        comando = True
        ganador = casillas[6]
        return comando, ganador
    
    #diagonales
    elif casillas[2] == casillas[4] == casillas[6] != " ":
        comando = True
        ganador = casillas[2]
        return comando, ganador
    
    elif casillas[0] == casillas[4] == casillas[8] != " ":        
        comando = True
        ganador = casillas[0]
        return comando, ganador
    
    #verticales
    elif casillas[0] == casillas[3] == casillas[6] != " ":       
        comando = True
        ganador = casillas[0]
        return comando, ganador
    
    elif casillas[1] == casillas[4] == casillas[7] != " ":        
        comando = True
        ganador = casillas[1]
        return comando, ganador
    
    elif casillas[2] == casillas[5] == casillas[8] != " ":       
        comando = True
        ganador = casillas[2]
        return comando, ganador
    elif set(casillas) == {"X", "O"}:
        comando = True
        ganador = "E"
        return comando, ganador
    else:
        comando = False
        ganador = " "
        return comando, ganador

def modo_de_juego():
    #modo de juego
    # 0 nada
    # 1 jugador vs jugador
    # 2 jugador vs pc
    modo = 0
    respuesta = input("[1] Jugador vs Jugador\n[2] Jugador vs PC\n[3] Salir\n-> ")
    while True:
        if respuesta.isnumeric():
            if int(respuesta) == 1:
                return 1         
            elif int(respuesta) == 2:
                return 2
            elif int(respuesta) == 3:
                return 3
            else:
                respuesta = input("\nIngrese un opcion válida: 1 o 2\n\n[1] Jugador vs Jugador\n[2] Jugador vs PC \n-> ")
        else:
            respuesta = input("\nIngrese una respuesta númerica: 1 o 2\n\n[1] Jugador vs Jugador\n[2] Jugador vs PC \n-> ")   

def playerVSplayer():
    global jugador1, jugador2
    jugador1 = input("Ingrese nombre jugador 1: ")
    jugador2 = input("Ingrese nombre jugador 2: ")
    datos = seleccionAzar(jugador1, jugador2)
    jugador1 = [datos[0], 0, "X"]
    jugador2 = [datos[1], 0, "O"]

    def marcador():
        print("\n\n")
        print(f"\tJugador\t\tPuntaje")
        print(f"\t{jugador1[0]}\t\t{jugador1[1]}")
        print(f"\t{jugador2[0]}\t\t{jugador2[1]}")
        print("\n\n")
        
    def partida():
        global resultado
        print(f"\nEl jugador #1 es: {jugador1[0]} con {jugador1[1]} partidas ganadas -> {jugador1[2]}")
        print(f"El jugador #2 es: {jugador2[0]} con {jugador2[1]} partidas ganadas -> {jugador2[2]}")
        print("\nEl tablero está así:")
        finPartida = False
        resultado = ""  
        while finPartida != True:
            
            finPartida = ganadorXO(interfaz, finPartida, resultado)[0]
            resultado = ganadorXO(interfaz, finPartida, resultado)[1]
            if resultado != "E":
                if resultado == " ":  
                    x = False
                    while x != True:
                        mostrar_datos(interfaz)
                        x = jugadaUsuario(jugador1)
                                       
                finPartida = ganadorXO(interfaz, finPartida, resultado)[0]
                resultado = ganadorXO(interfaz, finPartida, resultado)[1]

                if resultado == " ":
                    y = False
                    while y != True:
                        mostrar_datos(interfaz)
                        y = jugadaUsuario(jugador2)

                finPartida = ganadorXO(interfaz, finPartida, resultado)[0]
                resultado = ganadorXO(interfaz, finPartida, resultado)[1]
                               
        if resultado in jugador1:
            jugador1[1] += 1
            resultado = jugador1
        elif resultado in jugador2:
            jugador2[1] += 1
            resultado = jugador2 
        else:
            print(":O el tablero se lleno")
        
        mostrar_datos(interfaz)
        try:
            print(f"\nEl ganador es {resultado[0]} con un punteo de {resultado[1]} pts.")
            marcador()
        except IndexError:
            print("\n\nHubo un empate, sin puntos para nadie.")
            marcador()
        
    def continuacion():
        continuar = input("\n¿Desea continuar? Y/N\n-> ").lower()
        salir = False
        while salir != True:
            if continuar == "y":
                global interfaz, jugador1, jugador2
                interfaz = [" " for i in range(9)]
                if resultado[0] == jugador1[0]:
                    jugador1, jugador2 = jugador2, jugador1
                    jugador1[2] = "X"
                    jugador2[2] = "O"
                    partida()
                    continuar = input("\n¿Desea continuar? Y/N\n-> ").lower()
                    
                else:
                    partida()
                    continuar = input("\n¿Desea continuar? Y/N\n-> ").lower()
            elif continuar == "n":
                interfaz = [" " for i in range(9)]
                jugador1 = [datos[0], 0, "X"]
                jugador2 = [datos[1], 0, "O"]
                salir = True
            else:
                continuar = input("\n¿Desea continuar? Y/N\n-> ").lower()
    partida()
    continuacion()

def playerVScomputer():
    global jugador1, jugador2
    jugador1 = input("Ingrese su nombre: ")
    jugador2 = "PC"
    #datos = seleccionAzar(jugador1, jugador2)
    jugador1 = [jugador1, 0, "X"]
    jugador2 = [jugador2, 0, "O"]
    
    def marcador():
        print("\n\n")
        print(f"\tJugador\t\tPuntaje")
        print(f"\t{jugador1[0]}\t\t{jugador1[1]}")
        print(f"\t{jugador2[0]}\t\t{jugador2[1]}")
        print("\n\n")

    def partida():
        global resultado
        print(f"\nEl jugador #1 es: {jugador1[0]} con {jugador1[1]} partidas ganadas -> {jugador1[2]}")
        print(f"El jugador #2 es: {jugador2[0]} con {jugador2[1]} partidas ganadas -> {jugador2[2]}")
        print("\nEl tablero está así:")
        finPartida = False
        resultado = ""  
        while finPartida != True:
            
            finPartida = ganadorXO(interfaz, finPartida, resultado)[0]
            resultado = ganadorXO(interfaz, finPartida, resultado)[1]
            if resultado != "E":
                if resultado == " ":  
                    x = False
                    while x != True:
                        mostrar_datos(interfaz)
                        x = jugadaUsuario(jugador1)
                finPartida = ganadorXO(interfaz, finPartida, resultado)[0]
                resultado = ganadorXO(interfaz, finPartida, resultado)[1]
                if resultado == " ":
                    y = False
                    while y != True:
                        print()
                        mostrar_datos(interfaz)
                        print("\nLa computadora movió")
                        y = marcarPC(jugador2)
                        print()
                finPartida = ganadorXO(interfaz, finPartida, resultado)[0]
                resultado = ganadorXO(interfaz, finPartida, resultado)[1]
                
        if resultado in jugador1:
            jugador1[1] += 1
            resultado = jugador1
        elif resultado in jugador2:
            jugador2[1] += 1
            resultado = jugador2 
        else:
            print("\n:O el tablero se llenó\n")
        
        mostrar_datos(interfaz)
        try:
            print(f"\nEl ganador es {resultado[0]} con un punteo de {resultado[1]} pts.")
            marcador()
        except IndexError:
            print("\n\nHubo un empate, sin puntos para nadie.")
            marcador()
        
    def continuacion():
        continuar = input("\n¿Desea continuar? Y/N\n-> ").lower()
        salir = False
        while salir != True:
            if continuar == "y":
                global interfaz, jugador1, jugador2
                interfaz = [" " for i in range(9)]
                if resultado[0] == jugador1[0]:
                    #activar si se quiere que cuando la PC pierda se pase a jugador 1
                    #jugador1, jugador2 = jugador2, jugador1
                    #jugador1[2] = "X"
                    #jugador2[2] = "O"
                    partida()
                    continuar = input("\n¿Desea continuar? Y/N\n-> ").lower()
                    
                else:
                    partida()
                    continuar = input("\n¿Desea continuar? Y/N\n-> ").lower()
            elif continuar == "n":
                interfaz = [" " for i in range(9)]
                jugador1 = ["", 0, "X"]
                jugador2 = ["PC", 0, "O"]
                salir = True
            else:
                continuar = input("\n¿Desea continuar? Y/N\n-> ").lower()
    partida()
    continuacion()   

def main():
    while True:
        y = modo_de_juego()
        if y == 1:
            playerVSplayer()
            
        elif y == 2:
            playerVScomputer()
        
        elif y == 3:
            quit()
    
main()
