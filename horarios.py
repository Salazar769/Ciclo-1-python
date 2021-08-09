########################################
# Autor: Javier Chavez 21016
# Fecha: 17/05/2021
# Evaluacion 2
########################################

#Importo modulos
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from modulo import *

#Asi solo tienen que modificar la variable archivo con el nombre del archivo csv
archivo = "horarios.csv"
df = pd.read_csv(archivo)

#Menu siempre activo hasta romper el ciclo
while True:
    print("[1] Ingreso de horario de nuevo curso")
    print("[2] Modificación del horario de un curso")
    print("[3] Chequeo de horario")
    print("[4] Gráficos")
    print("[5] Actualizar csv")
    print("[6] Salir")
    op = input("\nSelecciona una opcion agradable sujeto: ") #recibe la opcion
    if int(op.isnumeric()): #si la opcion no es numerica la pide de nuevo
        if int(op) == 1:
            print("\n\n")
            nuevoCurso = input("¿Cual será el nombre del nuevo curso? -> ")
            periodosOcupados = input("\n¿Cuales periodos ocupará el nuevo curso?\nIngreselos separados por comas.\n -> ").split(", ")
            agregarCurso(df, nuevoCurso, periodosOcupados) #aplica la funcion agregar curso
            print("\n\n")
            print("Se agregó correctamente, para guardar los cambios no olvide usar la opcion 5:)\n\n")
        elif int(op) == 2:
            print("\n\n")
            cursoCambiar = input("Ingrese el nombre del curso que desea cambiar -> ")
            if cursoCambiar not in df["Cursos"].to_list(): #un poco de programacion defensiva para que no ingresen cursos que no existen :p
                print("\nEse curso no existe, ingrese uno que si\n")
            else:
                nuevosPeriodos = input("Cuales periodos ocupará ahora?\nIngreselos separados por comas.\n -> ").split(", ")
                modificarHorario(df, cursoCambiar, nuevosPeriodos) #aplico la funcion modificar horario
                print("\n\n")
                print("Se modificó correctamente, para guardar los cambios no olvide usar la opcion 5:)\n\n")
        elif int(op) == 3:
            print("\n\n")
            cursos = input("¿Que cursos desea chequear?\nIngreselos separados por comas y un espacio -> ").split(", ")
            print()
            try:
                print(chequeo(df, cursos)) #programacion defensiva por si truena al no encontrar el curso, lo mismo que arriba
            except ValueError:
                print("Ese curso no existe, ingrese de nuevo.")
            print()
        elif int(op) == 4:
            #Hago cada periodo una lista y los sumo segun los intervalos de los dias y cuento los true de la lista obtenida
            lunes = ( df["Per1"].to_list() + df["Per2"].to_list()  + df["Per3"].to_list()  + df["Per4"].to_list()  + df["Per5"].to_list()  + df["Per6"].to_list()  + df["Per7"].to_list()  + df["Per8"].to_list()  + df["Per9"].to_list() + df["Per10"].to_list() ).count(True)
            martes = ( df["Per11"].to_list() + df["Per12"].to_list()  + df["Per13"].to_list()  + df["Per14"].to_list()  + df["Per15"].to_list()  + df["Per16"].to_list()  + df["Per17"].to_list()  + df["Per18"].to_list()  + df["Per19"].to_list() + df["Per20"].to_list() ).count(True)
            miercoles = ( df["Per21"].to_list() + df["Per22"].to_list()  + df["Per23"].to_list()  + df["Per24"].to_list()  + df["Per25"].to_list()  + df["Per26"].to_list()  + df["Per27"].to_list()  + df["Per28"].to_list()  + df["Per29"].to_list() + df["Per30"].to_list() ).count(True)
            jueves = ( df["Per31"].to_list() + df["Per32"].to_list()  + df["Per33"].to_list()  + df["Per34"].to_list()  + df["Per35"].to_list()  + df["Per36"].to_list()  + df["Per37"].to_list()  + df["Per38"].to_list()  + df["Per39"].to_list() + df["Per40"].to_list() ).count(True)
            viernes = ( df["Per41"].to_list() + df["Per42"].to_list()  + df["Per43"].to_list()  + df["Per44"].to_list()  + df["Per45"].to_list()  + df["Per46"].to_list()  + df["Per47"].to_list()  + df["Per48"].to_list()  + df["Per49"].to_list() + df["Per50"].to_list() ).count(True)
            x = np.array(["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]) #defino el eje x
            y = np.array([lunes, martes, miercoles, jueves, viernes]) #defino el eje y con los valores numericos obtenidos de las variables dias
            plt.bar(x,y) #creo la grafica
            plt.show() #muestro la grafica
        elif int(op) == 5:
            df.to_csv(archivo, index=False) #actualizo el archivo
            print("\nEl documento a sido actualizado con exito\n")
        elif int(op) == 6:
            print("\n\n")
            print("Saliendo...")#Le indico que se está saliendo y rompo el ciclo while
            break
        elif int(op) == 9999: #para tener a la mano el dataframe
            print(df)
    else:
        print("Ingrese un dato válido.")


        