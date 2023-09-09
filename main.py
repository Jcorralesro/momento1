Elizabeth Zapata / Jose David Corrales
ropero = {   }  # Diccionario sin datos, el cliente los llena
continuar = True # inicializamos

print("Menu:") # menu para seleccionar opciones
print("1. Llenar")
print("2. Imprimir")
print("3. Eliminar")
print("4. Editar")
print("5. Salir")

# iniciamos el proceso de captura de datos
while continuar: 
    opcion = input("Seleccione una opción (1/2/3/4/5): ")
    
    if opcion == '1':
        clave = input('¿Qué parte desea comprar? ') 
        valor = input(clave + ': ')
        ropero[clave] = valor
         # 2. imprimir
    elif opcion == '2':
        print(ropero)
        # eliminar
    elif opcion == '3': 
        clave = input('¿Qué parte desea eliminar? ')
        if clave in ropero:
            ropero.pop(clave)
        else:
            print(f"{clave} no se encontró en el diccionario.")
            # editar
    elif opcion == '4': 
        clave = input('¿Qué parte desea editar? ')
        if clave in ropero:
            valor = input(f'Nuevo valor para {clave}: ')
            ropero[clave] = valor
        else:
            print(f"{clave} no se encontró en el diccionario.")
             # salir
    elif opcion == '5':
        continuar = False
    else:
        print("Opción no válida. Seleccione una opción del menú.")
     
        
  
  
  
  
