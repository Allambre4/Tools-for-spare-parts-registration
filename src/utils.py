import os
import win32com.client
import pandas as pd
import tkinter as tk
from tkinter import filedialog



def extraer_datos_excel():
    # Inicializar ventana de selección de archivo
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    
    # Pedir al usuario que seleccione un archivo
    archivo_excel = filedialog.askopenfilename(title="Selecciona un archivo de Excel", filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
    
    # Verificar si el usuario seleccionó un archivo
    if not archivo_excel:
        print("No se seleccionó ningún archivo.")
        return None
    
    # Cargar el archivo de Excel en un DataFrame
    df = pd.read_excel(archivo_excel, sheet_name="Creacion de material automa")
    
    # Definir las columnas esperadas
    columnas = ["material", "descriptionEnglish", "descriptionSpanish", "reorderPoint", 
                "minimunLotSize", "maximunLotSice", "maximunSotckLevel", "plannedDelivTime"]
    
    # Verificar si las columnas esperadas están en el archivo
    for col in columnas:
        if col not in df.columns:
            print(f"Error: Falta la columna '{col}' en el archivo.")
            return None
    
    # Extraer las filas a partir de la segunda (índice 1, porque la primera es encabezado)
    datos_extraidos = []
    for _, fila in df.iterrows():
        # Si encontramos una fila vacía, terminamos el proceso
        if pd.isnull(fila["material"]):
            break
        
        # Agregamos los datos a la lista como una tupla
        datos_extraidos.append((
            fila["material"],
            fila["descriptionEnglish"],
            fila["descriptionSpanish"],
            fila["reorderPoint"],
            fila["minimunLotSize"],
            fila["maximunLotSice"],
            fila["maximunSotckLevel"],
            fila["plannedDelivTime"]
        ))
    
    return datos_extraidos

def iniciar_sesion_sap():
    """Inicializa la sesión de SAP y la retorna."""
    SapGuiAuto = win32com.client.GetObject("SAPGUI")  # Obtenemos el objeto principal de SAP GUI
    application = SapGuiAuto.GetScriptingEngine  # Accedemos al motor de scripting
    connection = application.Children(0)  # Obtenemos la primera conexión activa
    session = connection.Children(0)  # Obtenemos la primera sesión activa dentro de la conexión
    session.findById("wnd[0]").maximize()  # Maximizamos la ventana de SAP
    return session


def crear_material(session, material, descriptionEnglish, descriptionSpanish, reorderPoint, minimunLotSize, maximunLotSice, maximunSotckLevel, plannedDelivTime):
    
    try:    
    
        #Ajuste de reorder point
        if reorderPoint<maximunSotckLevel:
            reorderPoint=reorderPoint+1
        
        # Variables constantes
        purchasingGroup = "4M5"  # constante
        mrpgroup = "RM"  # constante
        mrptype = "ND"  # constante
        mrpController = "SP1"  # constante
        lotSize = "HB"  # constante
        prodStorLocation = "4540"  # constante
        grProcessingTime = "1"  # constante
        forecastModel = "T"  # constante
        profitCenter = "0T000"  # constante

        # Ejecutamos la transacción MM01 (Crear material)
        session.findById("wnd[0]/tbar[0]/okcd").text = "/nMM01"
        session.findById("wnd[0]").sendVKey(0)  # Simulamos la tecla Enter

        # Ingresamos el número de material y otros datos básicos
        session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = material  # Número de material
        session.findById("wnd[0]/usr/cmbRMMG1-MBRSH").key = "C"  # Sector de material
        session.findById("wnd[0]/usr/cmbRMMG1-MTART").key = "Y4ER"  # Tipo de material
        session.findById("wnd[0]/usr/cmbRMMG1-MTART").setFocus()
        session.findById("wnd[0]").sendVKey(0)  # Continuamos con la tecla Enter
        session.findById("wnd[1]").sendVKey(0)  # Cerramos ventanas emergentes si aparecen
        session.findById("wnd[1]").sendVKey(0)

        # Definimos el grupo de compras
        session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2301/ctxtMARC-EKGRP").text = purchasingGroup
        session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2301/ctxtMARC-EKGRP").setFocus()
        session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2301/ctxtMARC-EKGRP").caretPosition = 3
        session.findById("wnd[0]").sendVKey(0)  # Confirmamos con Enter

        # Editamos la descripción larga en inglés
        session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2321/cntlLONGTEXT_BESTELL/shellcont/shell").text = descriptionEnglish
        session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2321/btnTEAN").press()  # Abrimos la opción de idioma

        # Cambiamos el idioma a español
        session.findById("wnd[1]/usr/cmbDESC_LANGU_NEW").key = "S"
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        # Editamos la descripción en español
        session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2321/cntlLONGTEXT_BESTELL/shellcont/shell").text = descriptionSpanish

        # Continuamos al siguiente paso
        session.findById("wnd[0]/tbar[1]/btn[18]").press()

        # Configuramos parámetros adicionales del material
        session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2481/ctxtMARC-DISGR").text = mrpgroup
        session.findById("wnd[0]/usr/subSUB3:SAPLMGD1:2482/ctxtMARC-DISMM").text = mrptype
        session.findById("wnd[0]/usr/subSUB3:SAPLMGD1:2482/txtMARC-MINBE").text = reorderPoint
        session.findById("wnd[0]/usr/subSUB3:SAPLMGD1:2482/ctxtMARC-DISPO").text = mrpController

        # Definimos estrategias de abastecimiento
        session.findById("wnd[0]/usr/subSUB4:SAPLMGD1:2483/ctxtMARC-DISLS").text = lotSize
        session.findById("wnd[0]/usr/subSUB4:SAPLMGD1:2483/txtMARC-BSTMI").text = minimunLotSize
        session.findById("wnd[0]/usr/subSUB4:SAPLMGD1:2483/txtMARC-BSTMA").text = maximunLotSice
        session.findById("wnd[0]/usr/subSUB4:SAPLMGD1:2483/txtMARC-MABST").text = maximunSotckLevel

        # Datos de almacenamiento y tiempos de entrega
        session.findById("wnd[0]/usr/subSUB6:SAPLMGD1:2484/ctxtMARC-LGPRO").text = prodStorLocation
        session.findById("wnd[0]/usr/subSUB7:SAPLMGD1:2485/txtMARC-PLIFZ").text = plannedDelivTime
        session.findById("wnd[0]/usr/subSUB7:SAPLMGD1:2485/txtMARC-WEBAZ").text = grProcessingTime
        session.findById("wnd[0]/tbar[1]/btn[18]").press()
        session.findById("wnd[0]/tbar[1]/btn[18]").press()
        session.findById("wnd[0]/tbar[1]/btn[18]").press()

        # Definimos el modo de producción
        session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2521/ctxtMPOP-PRMOD").text = forecastModel
        session.findById("wnd[0]/tbar[1]/btn[18]").press()

        # Asignamos el centro de costos
        session.findById("wnd[0]/usr/subSUB5:SAPLMGD1:5801/ctxtMARC-PRCTR").text = profitCenter
        session.findById("wnd[0]/tbar[1]/btn[18]").press()

        # Confirmamos el proceso
        session.findById("wnd[1]/usr/btnSPOP-OPTION1").press() #guarda 
        #session.findById("wnd[1]/usr/btnSPOP-OPTION2").press() #No guardar material.

    except Exception as e:
            print(f"Error al procesar el material {material}: {e}")