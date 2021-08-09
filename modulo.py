########################################
# Autor: Javier Chavez 21016
# Fecha: 17/05/2021
# Modulo Evaluacion 2
########################################

import pandas as pd

data = pd.read_csv("horarios.csv")

def agregarCurso(dataFrame, nombreNuevoCurso, listaPeriodos):
    """Esta funcion recibe el dataframe en uso, el nombre de un nuevo curso y la lista de periodos que desea ocupar.
    Se tiene una lista con los periodos disponibles y se genera una lista por comprension con los datos nuevos a agregar
    por cada vez que haya coincidencia con los datos que ingresó el usuario se agregará True.
    Retorna el dataframe actualizado.
    """
    periodosDisponibles = ["","Per1","Per2","Per3","Per4","Per5","Per6","Per7","Per8","Per9","Per10","Per11","Per12","Per13","Per14","Per15","Per16","Per17","Per18","Per19","Per20","Per21","Per22","Per23","Per24","Per25","Per26","Per27","Per28","Per29","Per30","Per31","Per32","Per33","Per34","Per35","Per36","Per37","Per38","Per39","Per40","Per41","Per42","Per43","Per44","Per45","Per46","Per47","Per48","Per49","Per50"]
    size = len(dataFrame) #cantidad de cursos actuales
    nuevo = [True if i in listaPeriodos else False for i in periodosDisponibles]
    nuevo[0] = nombreNuevoCurso
    dataFrame.loc[size+1]= nuevo
    return dataFrame

def modificarHorario(dataFrame, cursoPorCambiar, listaPeriodosNuevos):
    """Esta funcion recibe el dataframe en uso, el nombre del curso a modificar y la lista de periodos va a ocupar ahora el curso.
    retorna el dataframe actualizado
    """
    indices = dataFrame["Cursos"].to_list()
    posicionPorCambiar = indices.index(cursoPorCambiar) 
    periodosDisponibles = ["","Per1","Per2","Per3","Per4","Per5","Per6","Per7","Per8","Per9","Per10","Per11","Per12","Per13","Per14","Per15","Per16","Per17","Per18","Per19","Per20","Per21","Per22","Per23","Per24","Per25","Per26","Per27","Per28","Per29","Per30","Per31","Per32","Per33","Per34","Per35","Per36","Per37","Per38","Per39","Per40","Per41","Per42","Per43","Per44","Per45","Per46","Per47","Per48","Per49","Per50"]
    size = len(dataFrame) #cantidad de cursos actuales
    nuevo = [True if i in listaPeriodosNuevos else False for i in periodosDisponibles]
    nuevo[0] = cursoPorCambiar
    dataFrame.loc[posicionPorCambiar]= nuevo
    return dataFrame


def chequeo(dataFrame, listaCursos):
    """recibe el data frame en uso y la lista de cursos a verificar
    se generan las posiciones de los cursos
    y se crea una lista por comprension que tiene los indices de los cursos a comparar
    se crea un subDataframe con los cursos a comparar
    Se cuentan los true de cada periodo y se hace una serie de if para comparar que la cantidad de true por columna(periodo)
    sea menor o igual que 1 para estar seguros que en un mismo periodo no se tiene dos clases (true)
    
    """
    posiciones = dataFrame["Cursos"].to_list()
    posicionCursos = [posiciones.index(i) for i in listaCursos]
    subDataframe = dataFrame.iloc[posicionCursos] #dataframe de solo los cursos por verificar
    per1 = subDataframe["Per1"].to_list().count(True)
    per2 = subDataframe["Per2"].to_list().count(True)
    per3 = subDataframe["Per3"].to_list().count(True)
    per4 = subDataframe["Per4"].to_list().count(True)
    per5 = subDataframe["Per5"].to_list().count(True)
    per6 = subDataframe["Per6"].to_list().count(True)
    per7 = subDataframe["Per7"].to_list().count(True)
    per8 = subDataframe["Per8"].to_list().count(True)
    per9 = subDataframe["Per9"].to_list().count(True)
    per10 = subDataframe["Per10"].to_list().count(True)
    per11 = subDataframe["Per11"].to_list().count(True)
    per12 = subDataframe["Per12"].to_list().count(True)
    per13 = subDataframe["Per13"].to_list().count(True)
    per14 = subDataframe["Per14"].to_list().count(True)
    per15 = subDataframe["Per15"].to_list().count(True)
    per16 = subDataframe["Per16"].to_list().count(True)
    per17 = subDataframe["Per17"].to_list().count(True)
    per18 = subDataframe["Per18"].to_list().count(True)
    per19 = subDataframe["Per19"].to_list().count(True)
    per20 = subDataframe["Per20"].to_list().count(True)
    per21 = subDataframe["Per21"].to_list().count(True)
    per22 = subDataframe["Per22"].to_list().count(True)
    per23 = subDataframe["Per23"].to_list().count(True)
    per24 = subDataframe["Per24"].to_list().count(True)
    per25 = subDataframe["Per25"].to_list().count(True)
    per26 = subDataframe["Per26"].to_list().count(True)
    per27 = subDataframe["Per27"].to_list().count(True)
    per28 = subDataframe["Per28"].to_list().count(True)
    per29 = subDataframe["Per29"].to_list().count(True)
    per30 = subDataframe["Per30"].to_list().count(True)
    per31 = subDataframe["Per31"].to_list().count(True)
    per32 = subDataframe["Per32"].to_list().count(True)
    per33 = subDataframe["Per33"].to_list().count(True)
    per34 = subDataframe["Per34"].to_list().count(True)
    per35 = subDataframe["Per35"].to_list().count(True)
    per36 = subDataframe["Per36"].to_list().count(True)
    per37 = subDataframe["Per37"].to_list().count(True)
    per38 = subDataframe["Per38"].to_list().count(True)
    per39 = subDataframe["Per39"].to_list().count(True)
    per40 = subDataframe["Per40"].to_list().count(True)     
    per41 = subDataframe["Per41"].to_list().count(True)
    per42 = subDataframe["Per42"].to_list().count(True)
    per43 = subDataframe["Per43"].to_list().count(True)
    per44 = subDataframe["Per44"].to_list().count(True)
    per45 = subDataframe["Per45"].to_list().count(True)
    per46 = subDataframe["Per46"].to_list().count(True)
    per47 = subDataframe["Per47"].to_list().count(True)
    per48 = subDataframe["Per48"].to_list().count(True)
    per49 = subDataframe["Per49"].to_list().count(True)
    per50 = subDataframe["Per50"].to_list().count(True)
    if per1 <= 1:
        pass
        if per2 <= 1:
            pass
            if per3 <= 1:
                pass
                if per4 <= 1:
                    pass
                    if per5 <= 1:
                        pass
                        if per6 <= 1:
                            pass
                            if per7 <= 1:
                                pass
                                if per8 <= 1:
                                    pass
                                    if per9 <= 1:
                                        pass
                                        if per10 <= 1:
                                            pass
                                            if per11 <= 1:
                                                pass
                                                if per12 <= 1:
                                                    pass
                                                    if per13 <= 1:
                                                        pass
                                                        if per14 <= 1:
                                                            pass
                                                            if per15 <= 1:
                                                                pass
                                                                if per16 <= 1:
                                                                    pass
                                                                    if per17 <= 1:
                                                                        pass
                                                                        if per18 <= 1:
                                                                            pass
                                                                            if per19 <= 1:
                                                                                pass
                                                                                if per20 <= 1:
                                                                                    pass
                                                                                    if per21 <= 1:
                                                                                        pass
                                                                                        if per22 <= 1:
                                                                                            pass
                                                                                            if per23 <= 1:
                                                                                                pass
                                                                                                if per24 <= 1:
                                                                                                    pass
                                                                                                    if per25 <= 1:
                                                                                                        pass
                                                                                                        if per26 <= 1:
                                                                                                            pass
                                                                                                            if per27 <= 1:
                                                                                                                pass
                                                                                                                if per28 <= 1:
                                                                                                                    pass
                                                                                                                    if per29 <= 1:
                                                                                                                        pass
                                                                                                                        if per30 <= 1:
                                                                                                                            pass
                                                                                                                            if per31 <= 1:
                                                                                                                                pass
                                                                                                                                if per32 <= 1:
                                                                                                                                    pass
                                                                                                                                    if per33 <= 1:
                                                                                                                                        pass
                                                                                                                                        if per34 <= 1:
                                                                                                                                            pass
                                                                                                                                            if per35 <= 1:
                                                                                                                                                pass
                                                                                                                                                if per36 <= 1:
                                                                                                                                                    pass
                                                                                                                                                    if per37 <= 1:
                                                                                                                                                        pass
                                                                                                                                                        if per38 <= 1:
                                                                                                                                                            pass
                                                                                                                                                            if per39 <= 1:
                                                                                                                                                                pass
                                                                                                                                                                if per40 <= 1:
                                                                                                                                                                    pass
                                                                                                                                                                    if per41 <= 1:
                                                                                                                                                                        pass
                                                                                                                                                                        if per42 <= 1:
                                                                                                                                                                            pass
                                                                                                                                                                            if per43 <= 1:
                                                                                                                                                                                pass
                                                                                                                                                                                if per44 <= 1:
                                                                                                                                                                                    pass
                                                                                                                                                                                    if per45 <= 1:
                                                                                                                                                                                        pass
                                                                                                                                                                                        if per46 <= 1:
                                                                                                                                                                                            pass
                                                                                                                                                                                            if per47 <= 1:
                                                                                                                                                                                                pass
                                                                                                                                                                                                if per48 <= 1:
                                                                                                                                                                                                    pass
                                                                                                                                                                                                    if per49 <= 1:
                                                                                                                                                                                                        pass
                                                                                                                                                                                                        if per50 <= 1:
                                                                                                                                                                                                            return "Usted si se puede asignar esos cursos"
                                                                                                                                                                                                                              
    else:
        return "Usted no se puede asignar esos cursos"
    
