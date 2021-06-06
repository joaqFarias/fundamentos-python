#Cuenta regresiva : crea una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número 
# como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]
def cuenta_regresiva(num):
    lista = []
    for i in range(num, -1, -1):
        lista.append(i)
    return lista
lista_output = cuenta_regresiva(5)
print(lista_output)

# Imprimir y volver : crea una función que recibirá una lista con dos 
# números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2
def print_and_return(lista=[]):
    if len(lista) < 2:
        print("ingrese una lista valida")
        return False
    else:
        print(lista[0])
        return lista[1]
output = print_and_return([1,2])
print(output)

# First Plus Length : crea una función que acepta una lista y devuelve
# la suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 
# (primer valor: 1 + longitud: 5)
def first_plus_length(lista=[]):
    largo = len(lista)
    if largo < 1:
        print("ingrese lista valida")
        return False
    else:
        return lista[0] + len(lista)
print(first_plus_length([1,2,3,4,5]))

# Valores mayores que el segundo : escribe una función que acepte una
# lista y crea una nueva lista que contenga solo los valores de la lista
# original que sean mayores que su segundo valor. Imprima cuántos valores
# son y luego devuelva la nueva lista. Si la lista tiene menos de 2 
# elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir
# 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False
def values_greater_than_second(lista=[]):
    if len(lista) < 2:
        print("ingrese una lista valida")
        return False
    else:
        lista_output = []
        for i in range(len(lista)):
            if lista[1] < lista[i]:
                lista_output.append(lista[i])
        return lista_output
lista_prueba1 = [5,2,3,2,1,4]
lista_prueba2 = [1]
output = values_greater_than_second(lista_prueba1)
print(output)

# Esta longitud, ese valor : escribe una función que acepte dos enteros 
# como parámetros: tamaño y valor. La función debe crear y devolver una 
# lista cuya longitud es igual al tamaño dado y cuyos valores son todos 
# los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]
def length_and_value(tamanio=False, valor=False):
    if tamanio == False or valor == False:
        print("ingrese valores validos")
        return False
    else:
        lista_output = []
        for i in range(tamanio):
            lista_output.append(valor)
        return lista_output
ejemplo1 = length_and_value(4,7)
print(ejemplo1)
ejemplo2 = length_and_value(6,2)
print(ejemplo2)
