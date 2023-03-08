from colorama import Fore
from xml.dom import minidom
import xml.etree.cElementTree as ET 

def LecturaXML(my_muestras,celdas_1,celdas_2,celdas_3,celdas_4,celdas_5,my_organismos):

    contadorTableros = 0
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
            for dato in organismo:
                #Lectura de datos organismos
                codigo = dato.getElementsByTagName("codigo")
                nombre = dato.getElementsByTagName("nombre")
                valor_codigo = str(codigo[0].firstChild.nodeValue)
                valor_nombre = str(nombre[0].firstChild.nodeValue)
                #cantidad de organismos      ##cantidad de muestras
                my_organismos.Insertar(valor_codigo, valor_nombre)        #lectura de listado de Muestras
        listado_muestras = dato_marte.getElementsByTagName("listadoMuestras")
        for list_muestra in listado_muestras:
            #lectura de muestra 
            muestra = list_muestra.getElementsByTagName("muestra")
            for muest in muestra:
                contadorTableros +=1
                codigo_muestra = muest.getElementsByTagName("codigo")
                descripcion = muest.getElementsByTagName("descripcion")
                filas_muestra = muest.getElementsByTagName("filas")
                columnas_muestra = muest.getElementsByTagName("columnas")
                #obtencion de valores                    
                valor_codigo_muest = str(codigo_muestra[0].firstChild.nodeValue)
                descripcio = str(descripcion[0].firstChild.nodeValue)
                valor_fila_muest = int(filas_muestra[0].firstChild.nodeValue)
                valor_columnas_muest = int(columnas_muestra[0].firstChild.nodeValue)
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
                        if contadorTableros == 1:
                            celdas_1.Insertar(val_fila_viva, val_column_viva, val_codigo_orga, color)
                        elif contadorTableros == 2:
                            celdas_2.Insertar(val_fila_viva, val_column_viva, val_codigo_orga, color)
                        elif contadorTableros == 3:
                            celdas_3.Insertar(val_fila_viva, val_column_viva, val_codigo_orga, color)
                        elif contadorTableros == 4:
                            celdas_4.Insertar(val_fila_viva, val_column_viva, val_codigo_orga, color)
                        elif contadorTableros == 5:
                            celdas_5.Insertar(val_fila_viva, val_column_viva, val_codigo_orga, color)
                if contadorTableros == 1:
                    my_muestras.Insertar(valor_codigo_muest, descripcio, valor_fila_muest, valor_columnas_muest,celdas_1)
                elif contadorTableros == 2:
                    my_muestras.Insertar(valor_codigo_muest, descripcio, valor_fila_muest, valor_columnas_muest,celdas_2)
                elif contadorTableros == 3:
                    my_muestras.Insertar(valor_codigo_muest, descripcio, valor_fila_muest, valor_columnas_muest,celdas_3)
                elif contadorTableros == 4:
                    my_muestras.Insertar(valor_codigo_muest, descripcio, valor_fila_muest, valor_columnas_muest,celdas_4)
                elif contadorTableros == 5:
                    my_muestras.Insertar(valor_codigo_muest, descripcio, valor_fila_muest, valor_columnas_muest,celdas_5)        
