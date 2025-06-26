import os

def obtener_archivos_por_carpeta(carpeta):
    """Devuelve un diccionario con la estructura de archivos y subcarpetas dentro de la carpeta seleccionada."""
    resultado = {}

    for subcarpeta in sorted(os.listdir(carpeta)):  # Ordena alfabéticamente las carpetas principales
        ruta_subcarpeta = os.path.join(carpeta, subcarpeta)
        if os.path.isdir(ruta_subcarpeta):  # Verifica que sea una carpeta
            resultado[subcarpeta] = {}

            for subsubcarpeta in sorted(os.listdir(ruta_subcarpeta)):  # Recorre las subcarpetas internas
                ruta_subsubcarpeta = os.path.join(ruta_subcarpeta, subsubcarpeta)
                if os.path.isdir(ruta_subsubcarpeta):  # Si es una subcarpeta, almacena sus archivos
                    resultado[subcarpeta][subsubcarpeta] = sorted(os.listdir(ruta_subsubcarpeta))
                else:  # Si es un archivo directamente dentro de la subcarpeta, lo almacena en una clave especial
                    resultado[subcarpeta].setdefault("_archivos_", []).append(subsubcarpeta)

    return resultado


carpeta_seleccionada = r"\\FSS460-01MX.group.pirelli.com\PUBLIC\09. MANTENIMIENTO\Almacén\Altas de refacciones\Spare parts\ALTAS NUEVAS\COTIZACIONES\429"
datos = obtener_archivos_por_carpeta(carpeta_seleccionada)

# Imprimir los datos de forma estructurada
totalarchivos=0
for carpeta, contenido in datos.items():
    print(f"\n📂 {carpeta}")
    if "_archivos_" in contenido:
        for archivo in contenido["_archivos_"]:
            print(f"  📄 {archivo}")
            totalarchivos=totalarchivos+1
    for subcarpeta, archivos in contenido.items():
        if subcarpeta != "_archivos_":
            print(f"  📂 {subcarpeta}")
            for archivo in archivos:
                print(f"    📄 {archivo}")
                totalarchivos=totalarchivos+1
print(f"En total hay {totalarchivos} dentro de las subcarpetas carpeta")

