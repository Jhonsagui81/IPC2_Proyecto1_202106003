from colorama import Fore
from xml.dom import minidom

def LecturaXML(my_muestras,my_celdas_vivas,my_organismos):
# try:
    print(Fore.LIGHTMAGENTA_EX+"\n\t")
    ruta = input(Fore.LIGHTMAGENTA_EX+"-> Ingrese la direccion del archivo que Generara las muestras iniciales: "+Fore.CYAN)
    doc = minidom.parse(str(ruta))
    print("--------Leyendo el documento-----------")
    datos_marte = doc.getElementsByTagName("datosMarte")
    #Datos marte
    for dato_marte in datos_marte:
        #lectura organismos vivos
        organismos_vivos = dato_marte.getElementsByTagName("listaOrganismos")
        for orga in organismos_vivos:
            #lectura de organimos
            organismo = orga.getElementsByTagName("organismo")
            print("Usted cuenta con "+str(len(organismo))+" Organismos los cuales son: ")
            for dato in organismo:
                #Lectura de datos organismos
                codigo = dato.getElementsByTagName("codigo")
                nombre = dato.getElementsByTagName("nombre")
                valor_codigo = str(codigo[0].firstChild.nodeValue)
                valor_nombre = str(nombre[0].firstChild.nodeValue)
                #cantidad de organismos
                my_organismos.Insertar(valor_codigo, valor_nombre)
                print("--> Organismo: "+valor_nombre) 
        #lectura de listado de Muestras
        listado_muestras = dato_marte.getElementsByTagName("listadoMuestras")
        for list_muestra in listado_muestras:
            #lectura de muestra 
            muestra = list_muestra.getElementsByTagName("muestra")
            for muest in muestra:
                codigo_muestra = muest.getElementsByTagName("codigo")
                descripcion = muest.getElementsByTagName("descripcion")
                filas_muestra = muest.getElementsByTagName("filas")
                columnas_muestra = muest.getElementsByTagName("columnas")
                #obtencion de valores                    
                valor_codigo_muest = str(codigo_muestra[0].firstChild.nodeValue)
                descripcio = str(descripcion[0].firstChild.nodeValue)
                valor_fila_muest = int(filas_muestra[0].firstChild.nodeValue)
                valor_columnas_muest = int(columnas_muestra[0].firstChild.nodeValue)
                ##cantidad de muestras
                print("Usted cuenta con las siguientes muestras: "+valor_codigo_muest)
                #lectura de lista de celdas vivas
                list_celdas_vivas = muest.getElementsByTagName("listadoCeldasVivas")
                for listcellive in list_celdas_vivas:
                    #lectura de celda viva
                    celda_viva = listcellive.getElementsByTagName("celdaViva")
                    for dato_celdaviva in celda_viva:
                        fila_viva = dato_celdaviva.getElementsByTagName("fila")
                        columa_viva = dato_celdaviva.getElementsByTagName("columna")
                        codigo_organismo = dato_celdaviva.getElementsByTagName("codigoOrganismo")
                        #obtencion de valores
                        val_fila_viva = int(fila_viva[0].firstChild.nodeValue)
                        val_column_viva = int(columa_viva[0].firstChild.nodeValue)
                        val_codigo_orga = str(codigo_organismo[0].firstChild.nodeValue)
                        #Rellenando la lista
                        color = my_organismos.ValidaCeldaViva(val_codigo_orga)
                        my_celdas_vivas.Insertar(val_fila_viva, val_column_viva, val_codigo_orga, color)
                        
                my_muestras.Insertar(valor_codigo_muest, descripcio, valor_fila_muest, valor_columnas_muest,my_celdas_vivas)
# except Exception as err:
#     print(Fore.RED+"\n\tSe acaba de producir un error :( " + str(err))
#     print(Fore.RED+"\tAsegurate de leer el MANUAL DE USUARIO")
    my_muestras.Imprimir()