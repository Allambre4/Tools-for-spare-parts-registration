print("importando win32...")
import win32com.client
print("win32 importado")

#Variables en orden de asignación:_________________________________________


material="74014773"  
purchasingGroup="4M5"  #constante
descriptionEnglish="Descripción larga en Ingles"
descriptionSpanish="Descripción larga en Español"
mrpgroup="RM" #constante
mrptype="ND" #constante
reorderPoint="6"
mrpController="SP1" #constante
lotSize="HB" #constante
minimunLotSize="1"
maximunLotSice="1"
maximunSotckLevel="6"
prodStorLocation="4540" #constante
plannedDelivTime="15"
grProcessingTime="1" #constante
forecastModel= "T" #constante
profitCenter="0T000" #constante
#__________________________________________________________________________

# Conectamos con el motor de scripting de SAP GUI
SapGuiAuto = win32com.client.GetObject("SAPGUI")  # Obtenemos el objeto principal de SAP GUI
application = SapGuiAuto.GetScriptingEngine  # Accedemos al motor de scripting
connection = application.Children(0)  # Obtenemos la primera conexión activa
session = connection.Children(0)  # Obtenemos la primera sesión activa dentro de la conexión

# Maximizamos la ventana de SAP
session.findById("wnd[0]").maximize()

# Ejecutamos la transacción MM01 (Crear material)
session.findById("wnd[0]/tbar[0]/okcd").text = "/nMM01"
session.findById("wnd[0]").sendVKey(0)  # Simulamos la tecla Enter

# Ingresamos el número de material y otros datos básicos
session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text =  material # Número de material
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
#session.findById("wnd[0]/usr/subSUB2:SAPLMGD1:2321/cntlLONGTEXT_BESTELL/shellcont/shell").text = "Descripción larga en Español" + "\r\n"

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
session.findById("wnd[1]/usr/btnSPOP-OPTION1").press()
