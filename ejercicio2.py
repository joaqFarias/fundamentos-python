# - Crea una funcion que dado una palabra diga si es palindroma o no.
def esPalindroma(palabra=False):
    if palabra == False:
        print("Ingrese una palabra, por favor")
    else:
        palabra_reverse = palabra[::-1]
        if palabra.lower() == palabra_reverse.lower():
            print("La palabra es 'palindroma'!")
        else:
            print(f"la palbra no es palindroma!")

palabra_prueba1 = "Ana"
palabra_prueba2 = "paralelepipedo"
esPalindroma()
esPalindroma(palabra_prueba1)
esPalindroma(palabra_prueba2)


def esPalindromo(texto = ""):
    if texto == "":
        print("ingrese palabra valida, por favor")
        return
    igual, aux = 0, 0
    for ind in reversed(range(0, len(texto))):
        if texto[ind].lower() == texto[aux].lower():
            igual += 1
        aux += 1
    if len(texto) == igual:
        print("El texto es palindromo!")
    else:  
        print("El texto no es palindromo!")
palabra_prueba1 = "Ana"
palabra_prueba2 = "paralelepipedo"
esPalindromo()
esPalindromo(palabra_prueba1)
esPalindromo(palabra_prueba2)