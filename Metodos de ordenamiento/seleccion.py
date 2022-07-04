#METODO DE ORDENAMIENTO SELECCION 

array = [6,8,2,7,1,5,4,3,9]

for i in range(0,len(array)):
    minimo = i
    for j in range(i+1, len(array)):
        if array[minimo] > array[j]:
            minimo = j

    temp = array[i]
    array[i] = array[minimo]
    array[minimo] = temp


print(array)