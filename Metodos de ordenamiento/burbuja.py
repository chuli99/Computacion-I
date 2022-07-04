#METODO DE ORDENAMIENTO BURBUJA

import time

array = [6,8,2,7,1,5,4,3,9]

for i in range(len(array)):
    for j in range(len(array)-1):
        
        if array [j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            time.sleep(5) 
            print(array)
