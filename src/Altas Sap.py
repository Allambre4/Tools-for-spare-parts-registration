from utils import *

registros = extraer_datos_excel()
if registros:
    for r in registros:
        print(r)

# Inicializamos la sesión solo una vez   
session_sap = iniciar_sesion_sap()

if registros:
    while True:
        try:
            num_registro = int(input(f"Ingrese el número de registro a procesar (1-{len(registros)}), o 0 para salir: "))
            
            if num_registro == 0:
                print("Saliendo del programa.")
                break
            
            if 1 <= num_registro <= len(registros):
                print(f"Procesando registros desde el {num_registro} hasta el {len(registros)}...")
                
                for i in range(num_registro - 1, len(registros)):  # Ajustamos índice para listas (empiezan en 0)
                    print(f"Procesando material {i + 1}: {registros[i][0]}")
                    crear_material(session_sap, *registros[i])
                
                print("Proceso completado.")
                break  # Salimos del loop tras procesar todos los registros
                
            else:
                print("Número fuera de rango. Intente de nuevo.")
        
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")
