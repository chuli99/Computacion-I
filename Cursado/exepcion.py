#exepciones
num1 = 9
num2 = 0

try:
    #si por alguna razon falla, se puede manejar un error con un exept.
    print("Antes del error")
    print( num1 / num2 )
    print("Después del error")
except Exception as e:
    print(e)
    #printea el tipo de error que tengo
except ValueError as e:
    print(e)
finally:
    #se ejecuta si o si.
    print("Despues de la operación")