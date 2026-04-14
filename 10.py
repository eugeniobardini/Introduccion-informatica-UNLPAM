opcion = 0

while opcion != 4:
    print("\n--- MENÚ ---")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")
    
    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        print("Ud. Eligió la opción 1")
    elif opcion == 2:
        print("Ud. Eligió la opción 2")
    elif opcion == 3:
        print("Ud. Eligió la opción 3")
    elif opcion == 4:
        print("Saliendo del programa...")
    else:
        print("Opción no válida, intente de nuevo.")


# Porque pones la condicion de si opcion es diferente de 4, se vuelve a ejecutar todo y vuelve a pedir el numero, si ahi si es 4 se termina porque 4 no es diferente de 4

# Si ingresas un numero fuera del rango se imprime un cartel de opcion no valida, intente de nuevo