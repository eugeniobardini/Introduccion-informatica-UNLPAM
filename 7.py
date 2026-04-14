num = int(input("Ingrese un numero"))

if (num < 0 or num > 100):
    print(f"{num} es negativo 0 es mayor a 100")
else:
    print("No cumple la condicion")


#OR hace que el if sea true si por lo menos una condicion se cumple
#No se imprime la condicion si num es positivo o menor a 100
