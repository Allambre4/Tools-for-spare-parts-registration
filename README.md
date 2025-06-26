## Herramienta: TestRevisarCotizaciones.py
### Descripción
TestRevisarCotizaciones.py es una utilidad desarrollada para explorar, listar y contabilizar archivos dentro de una estructura de carpetas en una ruta específica. Esta herramienta es especialmente útil para visualizar y auditar el contenido de directorios relacionados con cotizaciones o registros de refacciones, facilitando el control y la gestión documental.

### ¿Qué hace?
Recorre una carpeta principal y sus subcarpetas de manera recursiva (dos niveles).
Muestra la estructura de carpetas y archivos de forma ordenada y jerárquica en la consola.
Cuenta e imprime el total de archivos encontrados.
Diferencia entre archivos y carpetas mediante emojis (📂 para carpetas, 📄 para archivos) para mejorar la legibilidad.
Permite modificar fácilmente la ruta base para adaptarla a diferentes ubicaciones en red o locales.
Uso
### Configuración de la ruta:

Modifica la variable carpeta_seleccionada en el script para apuntar a la carpeta raíz que deseas explorar.
Ejemplo:
Python
carpeta_seleccionada = r"RUTA\A\TU\CARPETA"
###Ejecución:

Ejecuta el script desde consola o desde tu entorno Python.
El script imprimirá la estructura de carpetas y archivos, así como el total de archivos detectados.
Salida esperada:

Code
📂 Carpeta1
  📄 archivo_directo.txt
  📂 SubcarpetaA
    📄 archivo1.xlsx
    📄 archivo2.pdf
📂 Carpeta2
  📂 SubcarpetaB
    📄 archivoX.docx
En total hay 5 dentro de las subcarpetas carpeta

### Ejemplo de uso

'''Python
carpeta_seleccionada = r"\\SERVIDOR\CARPETA\COTIZACIONES"
datos = obtener_archivos_por_carpeta(carpeta_seleccionada)'''

### Dependencias
Python 3.x
Módulo estándar os (no requiere instalación adicional)
###Ubicación
src/TestRevisarCotizaciones.py
