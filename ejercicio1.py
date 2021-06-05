# Crea una función que tome una lista y devuelva el primer y el último
# valor de la lista. Si la longitud de la lista es menor que 2,
# haga que devuelva False.

def ejercicio(lista=[]):
    if len(lista) < 2:
        return False, False
    else:
        primer = lista[0]
        #ultimo = lista[-1]
        ultimo = lista[len(lista)-1]
        return primer, ultimo
    
lista_prueba1 = [1, 2, 3, 4]
lista_prueba2 = [2]
primer, ultimo = ejercicio(lista_prueba2)
print(f"el primero es {primer} y el ultimo es {ultimo}")