from utils import *

# Ejemplo de uso
carpeta_seleccionada = r"C:\Users\arguejo001\OneDrive - Pirelli\Documents\Desarrollos\Proyecto Altas refacciones\data"
datos = obtener_archivos_por_carpeta(carpeta_seleccionada)

# Imprimir los datos de forma estructurada
totalarchivos=0
for carpeta, contenido in datos.items():
    print(f"\n📂 {carpeta}")
    if "_archivos_" in contenido:
        for archivo in contenido["_archivos_"]:
            print(f"  📄 {archivo}")
    for subcarpeta, archivos in contenido.items():
        if subcarpeta != "_archivos_":
            print(f"  📂 {subcarpeta}")
            for archivo in archivos:
                print(f"    📄 {archivo}")
                totalarchivos=totalarchivos+1
print(f"En total hay {totalarchivos} dentro de las subcarpetas carpeta")