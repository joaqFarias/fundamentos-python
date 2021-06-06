def insertionSort(arr=[]):
    if arr == []:
        print("ingrese array valido")
        return arr
    else:
        count = 0
        i = 1
        while i <= len(arr)-1:
            for j in range(i, 0, -1):
                count += 1
                if arr[j] <= arr[j-1]:
                    arr[j], arr[j-1] = arr[j-1], arr[j]   
                else:
                    break
            i += 1
            #print(f"minimo en iteracion {i}: {minimo} y el lugar: {lugar_min}")
        print(f"Numero de iteraciones: {count}")
        return arr

array_test = [1, 5, 3, 2, 0, 8] * 1000
array_ordenado = insertionSort(array_test)
#print(array_ordenado)