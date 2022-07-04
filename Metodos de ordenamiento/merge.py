#METODO DE ORDENAMIENTO MERGE

array = [6,8,2,7,1,5,4,3,9]

def mergeSort(array):
    if len(array) == 1:
        return array
    
    middle = len(array) // 2
    left_array = array[:middle]
    right_array = array[middle:]

    sorted_left_array = mergeSort(left_array)
    sorted_right_array = mergeSort(right_array)
    
    return Merge(sorted_left_array,sorted_right_array)

def Merge(left_array,right_array):
    array_resultado = []
    while len(left_array) > 0 and len(right_array) > 0:
        if left_array[0] > right_array[0]:
            array_resultado.append(right_array[0])
            right_array.pop(0)
        else:
            array_resultado.append(left_array[0])
            left_array.pop(0)
    while len(left_array) > 0:
        array_resultado.append(left_array[0])
        left_array.pop(0)
    while len(left_array) > 0:
        array_resultado.append(right_array[0])
        right_array.pop(0)
    
    return array_resultado

print(mergeSort(array))