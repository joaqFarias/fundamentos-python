def selectionSort(arr=[]):
    if arr == []:
        print("ingrese array valido")
        return arr
    else:
        count = 0
        for i in range(len(arr)):
            minimo = arr[i]
            lugar_min = i
            lugar_min = False
            for j in range(i, len(arr)):
                if minimo > arr[j]:
                    minimo = arr[j]
                    lugar_min = j
                count += 1
            #print(f"minimo en iteracion {i}: {minimo} y el lugar: {lugar_min}")
            if lugar_min == False:
                break
            else: 
                arr[i], arr[lugar_min] = arr[lugar_min], arr[i] 
                #print(f"en iteracion {i} el array es {arr}")
        print(f"Numero de iteraciones: {count}")
        return arr

array_test = [1, 5, 3, 2, 0, 8] * 1000
array_ordenado = selectionSort(array_test)
#print(array_ordenado)