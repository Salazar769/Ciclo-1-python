def verificandoTipos(lista_de_datos):
    lista_resultante = []
    for i in lista_de_datos:
        if type(i) == str:
           lista_resultante.append(i.upper())
        elif type(i) == int:
           lista_resultante.append(i*i*i)
        elif type(i) == float:
            lista_resultante.append(round(i, 3))
    return lista_resultante
lista = [7, 'Hola mundo', 3.2745, 8, 9.399996]
print(verificandoTipos(lista))