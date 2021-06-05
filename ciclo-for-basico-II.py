# Tamaño grande: dada una lista, escriba una función que cambie todos los
# números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, 
# pero cuyos valores son ahora [-1, "big", "big", -5]
from typing import List


def biggie_size(lista=[]):
    if len(lista) == 0:
        print("ingrese lista valida")
        return False
    else: 
        for i in range(len(lista)):
            if lista[i] > 0:
                lista[i] = "big"
        return lista
output = biggie_size ([- 1, 3, 5, -5])
print(output)

# Contar positivos : dada una lista de números, cree una función para 
# reemplazar el último valor con el número de valores positivos. 
# (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives ([- 1,1,1,1]) cambia la lista original a 
# [-1,1,1,3] y la devuelve
# Ejemplo: count_positives ([1,6, -4, -2, -7, -2]) cambia la lista a 
# [1,6, -4, -2, -7,2] y la devuelve
def count_positives(lista=[]):
    if len(lista) == 0:
        print("ingrese lista valida")
        return False
    else: 
        suma_pos = 0
        for i in range(len(lista)):
            if lista[i] > 0:
                suma_pos += 1
        lista[-1] = suma_pos
        return lista
output1 = count_positives ([- 1,1,1,1])
output2 =  count_positives ([1,6, -4, -2, -7, -2])
print(output1)
print(output2)

# Suma total : crea una función que toma una lista y devuelve la suma de 
# todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7
def sum_total(lista=[]):
    if len(lista) == 0:
        print("ingrese lista valida")
        return False
    else: 
        suma = 0
        for i in range(len(lista)):
            suma += lista[i]
        return suma
output1 = sum_total ([1,2,3,4])
output2 = sum_total ([6,3, -2])
print(output1)
print(output2)

# Promedio : crea una función que toma una lista y devuelve el promedio 
# de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5
def promedio(lista=[]):
    if len(lista) == 0:
        print("ingrese lista valida")
        return False
    else: 
        suma = 0
        for i in range(len(lista)):
            suma += lista[i]
        return suma / len(lista)
output = promedio ([1,2,3,4])
print(output)


# Longitud : crea una función que toma una lista y devuelve la longitud 
# de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0
def longitud(lista):
    return len(lista)
output1 = longitud ([37,2,1, -9])
output2 = longitud ([])
print(output1)
print(output2)

# Mínimo : crea una función que tome una lista de números y devuelva el
# valor mínimo en la lista. Si la lista está vacía, haga que la función
# devuelva False.
#Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False
def minimo(lista=[]):
    if len(lista) == 0:
        #print("ingrese lista valida")
        return False
    else: 
        minimo = lista[0]
        for i in range(len(lista)):
            if lista[i] < minimo:
                minimo = lista[i]
        return minimo
output1 = minimo ([37,2,1, -9])
output2 = minimo ([])
print(output1)
print(output2)

# Máximo : crea una función que toma una lista y devuelve el valor máximo 
# en la matriz. Si la lista está vacía, haga que la función devuelva
# False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False
def maximo(lista=[]):
    if len(lista) == 0:
        #print("ingrese lista valida")
        return False
    else: 
        maximo = lista[0]
        for i in range(len(lista)):
            if lista[i] > maximo:
                maximo = lista[i]
        return maximo
output1 = maximo ([37,2,1, -9]) 
output2 = maximo ([])
print(output1)
print(output2)    

# Análisis final : crea una función que tome una lista y devuelva un
# diccionario que tenga la suma total, promedio, mínimo, máximo y 
# longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver 
# {'totalTotal': 31, 'promedio': 7.75, 'mínimo': -9, 'máximo': 37, 
# 'longitud': 4}
def ultimate_analysis(lista=[]):
    if lista == []:
        print("ingrese lista valida, por favor")
        return {"minimo": False, "maximo": False, "promedio":False, 
                "suma": False}
    else:
        minimo = lista[0]
        maximo = lista[0]
        suma = 0
        promedio = 0
        for i in range(len(lista)):
            if lista[i] < minimo:
                minimo = lista[i]
            if lista[i] > maximo:
                maximo = lista[i]
            suma += lista[i]
        promedio = suma / len(lista)
        return {"totalTotal": suma, "promedio": promedio, "minimo": minimo, 
                "maximo": maximo, "longitud": len(lista)}
output = ultimate_analysis ([37,2,1, -9])
print(output)

# Lista inversa : crea una función que tome una lista y la devuelva con 
# los valores invertidos. Haz esto sin crear una segunda lista. 
# (Se sabe que este desafío aparece durante las entrevistas técnicas 
# básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]
def reverse_list(lista=[]):
    if len(lista) == 0:
        #print("ingrese lista valida")
        return False
    else: 
        return lista[::-1]
output = reverse_list ([37,2,1, -9])
print(output)