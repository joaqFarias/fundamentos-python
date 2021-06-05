# Crea una función que tome una lista y devuelva un diccionario con 
# su mínimo, máximo, promedio y suma.
def estadisticas(lista=[]):
    if lista == []:
        print("ingrese lista valida, por favor")
        return {"minimo": False, "maximo": False, "promedio":False, 
                "suma": False}
    else:
        minimo = 9999999
        maximo = 0
        suma = 0
        promedio = 0
        for i in range(len(lista)):
            if lista[i] < minimo:
                minimo = lista[i]
            if lista[i] > maximo:
                maximo = lista[i]
            suma += i
        promedio = suma / len(lista)
        return {"minimo": minimo, "maximo": maximo, "promedio": promedio, 
                "suma": suma}

lista_prueba = [1, 2, 3, 4, 5]
diccionario = estadisticas(lista_prueba)
print(diccionario)