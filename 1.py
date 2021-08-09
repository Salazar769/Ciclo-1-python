def main(archivo):
    try:
        with open(archivo, "r", encoding='utf-8') as datos:
            contenido = datos.read()
        final = [] 
        listado = contenido.strip().split("\n")
        contador = 1
        for i in listado[:]:
            separador = i.split("\n")
            x = str(separador).replace("]", "")
            y = x.replace("[", "")
            w = y.replace("'","")
            z = w.replace('"','')
            final.append(z)
        return final
    except FileNotFoundError:
        final = None

def printLines(archivo):
    header = ""
    for i in archivo:
        header += str(i) + "\n"
    return header
  
print(printLines(main("archivo1.txt")))
print("El archivo tiene: " + str(len(main("archivo1.txt"))) + " lineas")
