#METODO DE ORDENAMIENTO DE INSERCION 

array = [6,8,2,7,1,5,4,3,9]
print(array)
i = 0
for j in range(1,len(array)):
    actual = array[j]
    
    i = j-1
    while i >= 0 and array[i] > actual:
        array[i+1] = array[i]
        i -= 1
    array[i+1] = actual
print(array)