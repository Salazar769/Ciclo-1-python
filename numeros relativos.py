import random
import math

def mfc(x,y): #funcion mfc recibe 2 parametros "x,y" que son numeros 
  if y == 0:   #es una condicion donde si "y" es igual a "0" retorna "x"
    return x  
  else:
      return mfc(y, (x % y))




#***************************

def primosRelativos(a,b):
#***************************
# ESCRIBA SU SOLUCION AQUI
    if mfc(a,b) == 1:
        return True
    else:
        return False 
#***************************




#*********************************************
# NO MODIFIQUE CODIGO ABAJO DE ESTA LINEA
#*********************************************

def getIncorrectas(l1,l2):
    inc = []
    for pos in range(len(l1)):
        if l1[pos] != l2[pos]:
            inc.append(pos)
    return inc

def stringPairs(v1, v2, re, li):
    sstr = ''
    for cont in range(len(li)):
        sstr += "(" + str(v1[li[cont]]) + "," + str(v2[li[cont]]) + ") -> "
        if isinstance(re[li[cont]],int):
            sstr += str(re[li[cont]])
        elif re[li[cont]] == "False":
            sstr += "false"
        else:
            sstr += "true"
        sstr += "\n"
    return sstr



def autoevaluacion():
  print("----------------------------------")
  print(" Autoevaluacion - Ejercicio #1")
  print("----------------------------------\n")
  evaluadas = 0
  correctas = 0
  print("Evaluando casos basicos de MFC:")
  # y = 0
  x = random.randint(1,15)
  evaluadas += 1
  if x == mfc(x,0):
      resp = "correcto!"
      correctas += 1
  else:
      resp = "incorrecto :("
  print("- y = 0:", resp)
  # y = 1
  x = random.randint(1,15)
  evaluadas += 1
  if 1 == mfc(x,1):
      resp = "correcto!"
      correctas += 1
  else:
      resp = "incorrecto :("
  print("- y = 1:", resp)
  # x = 1
  y = random.randint(1,15)
  evaluadas += 1
  if 1 == mfc(1,y):
      resp = "correcto!"
      correctas += 1
  else:
      resp = "incorrecto :("
  print("- x = 1:", resp)

  muestras = 20
  evaluadas = evaluadas + muestras
  vec1 = [0] * muestras
  vec2 = [0] * muestras
  for pos in range(muestras):
      vec1[pos] = random.randint(2,16)
      vec2[pos] = random.randint(15,30)

  acomp = list(map(math.gcd, vec1, vec2))
  results = list(map(mfc, vec1, vec2))
  muestrasc = 0
  print("\nSe generaron", muestras, "muestras aleatorias:")
  incorrectas = ""
  linc = []
  if acomp == results:
      muestrasc = muestras
  else:
      linc = getIncorrectas(acomp,results)
      incorrectas = "Muestras incorrectas: \n" + stringPairs(vec1, vec2, results, linc)
      muestrasc = muestras - len(linc)
  correctas = correctas + muestrasc
  print("Se encontaron: ")
  print(muestrasc, " muestras correctas")
  print(incorrectas)

  print("\nEvaluando casos Primos Relativos:")
  evaluadas = evaluadas + muestras
  vecp1 = [0]*muestras
  vecp2 = [0]*muestras
  for pos in range(muestras):
      vecp1[pos] = random.randint(2,15)
      vecp2[pos] = random.randint(10,45)
  comp = lambda a, b : math.gcd(a,b) == 1
  acompp = list(map(comp, vecp1, vecp2))
  resultsp = list(map(primosRelativos, vecp1, vecp2))
  incorrectas = ""
  linc = []
  if acompp == resultsp:
      muestrasc = muestras
  else:
      linc = getIncorrectas(acompp,resultsp)
      incorrectas = "Muestras incorrectas: \n" + stringPairs(vecp1, vecp2, resultsp, linc)
      muestrasc = muestras - len(linc)
  correctas = correctas + muestrasc
  print("Se encontaron: ")
  print(muestrasc, " muestras correctas")
  print(incorrectas)

  print("Evaluadas",evaluadas)
  print("Correctas:",correctas)
  nota = round(100 * (correctas / evaluadas),0)
  print("Nota aprox:",nota,"%\n")

autoevaluacion()
