def bubleSort(arr=[]):
    if arr == []:
        print("ingrese array valido")
        return arr
    else:
        count = 0
        sin_cambios = False
        while sin_cambios == False:
            sin_cambios = True
            for i in range(1,len(arr)):
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
                    sin_cambios = False
                count += 1
        print(f"Numero de iteraciones: {count}")
        return arr

array_test = [1, 5, 3, 2, 0, 8] * 1000
array_ordenado = bubleSort(array_test)
#print(array_ordenado)