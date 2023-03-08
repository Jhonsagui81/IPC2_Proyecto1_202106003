from TDA.ListaMuestra import ListaMuestra
from TDA.ListaCeldasVivas import ListaCeldas
from TDA.ListaOrganismos import ListaOrganismos
from Componentes.Dibujo import *
from Componentes.lectura import LecturaXML

from colorama import Fore


my_muestras = ListaMuestra()
celdas_1 = ListaCeldas()
celdas_2 = ListaCeldas()
celdas_3 = ListaCeldas()
celdas_4 = ListaCeldas()
celdas_5 = ListaCeldas()
my_organismos = ListaOrganismos()

while True:
    try:
        print(Fore.CYAN + '----------------------------------------------------')
        print(Fore.CYAN + '|              BIENVEDIO AL PROGRAMA               |')
        print(Fore.CYAN + '|                                                  |')
        print(Fore.CYAN + '| INTRODUCCION A LA PROGRAMACION 2     - Seccion A-|')
        print(Fore.CYAN + '| Jhonatan Alexander Aguilar Reyes     - 202106003 |')
        print(Fore.CYAN + '|                                                  |')
        print(Fore.CYAN + '----------------------------------------------------')
        input(Fore.CYAN + '\nPresione ENTER para contuniar')
        while True:
            print(Fore.CYAN +"----------------------------------------------------")
            print(Fore.CYAN +"|                    MENU PRINCIPAL                |")
            print(Fore.CYAN +"|                                                  |")
            print(Fore.CYAN +"|    [1]. Cargar archivo de entrada                |")
            print(Fore.CYAN +"|    [2]. Seleccionar muestra a trabaja            |")
            print(Fore.CYAN +"|    [3]. Generar xml con muestras actualizadas    |")
            print(Fore.CYAN +"|    [4]. Salir                                    |")
            print(Fore.CYAN +"|                                                  |")
            print(Fore.CYAN +"----------------------------------------------------")
            menu_principal_str = input(Fore.CYAN +"Ingrese un valor para seleccionar una opcion: ")
            menu_principal = int(menu_principal_str)    #Parseando opcion 
            if menu_principal == 1:   #Opcion 1 del menu principal
                LecturaXML(my_muestras,celdas_1,celdas_2,celdas_3,celdas_4,celdas_5, my_organismos)   #funcion para cargar archivo
                print(Fore.GREEN+"\nEn este documento se encuentran "+str(my_organismos.ObtenerNodos())+" organismos los cuales son: ")
                print(Fore.GREEN+ my_organismos.ImprimirOrganismos())

            if menu_principal == 2:     #Opcion 2 del menu principal
                # GestionadorPeliculas() #funcion para mostrar sub menu Gestionador
                codig_muestra = input("Por favor ingrese el codigo de la muestra a analizar: ")
                print(my_muestras.BuscarMuestra(codig_muestra))
                
                organis = input(Fore.CYAN+"\nIngrese el codigo del organismo que desea estudiar: ")
                print(Fore.LIGHTYELLOW_EX+"El organismo puede prosperar en las siguientes posiciones: \n")
                color_organis = celdas_1.BuscarColorCodigo(organis) #para tener el color asignado al organismo que estudia
                print("Este es el color del organismo: "+color_organis)
                numero_muestra = my_muestras.BuscarId(codig_muestra) #Para saber que lista de la muestra usar 
                limite_vertical = my_muestras.LimiteVertical(codig_muestra) #Obtener limite vertical
                limite_horizontal = my_muestras.LimiteHorizontal(codig_muestra) #obtener limite horizontal

                ##Pruebas 

                if numero_muestra == 1:
                    ListaProstera1 = celdas_1.ObtenerOrganismoProspe(limite_vertical,limite_horizontal, organis, celdas_1)
                    Dibujar(celdas_1, ListaProstera1,limite_vertical, limite_horizontal) ##para intentar dibujar 
                    while True:
                        print(Fore.LIGHTYELLOW_EX + '\n----------------------------------------------------')
                        print(Fore.LIGHTYELLOW_EX + '|            ¿Desea agregar un organismo?          |')
                        print(Fore.LIGHTYELLOW_EX + '|    [1]. Si                                       |')
                        print(Fore.LIGHTYELLOW_EX + '|    [0]. No                                       |')
                        print(Fore.LIGHTYELLOW_EX + '----------------------------------------------------')
                        sub_menu_2_str = input(Fore.LIGHTYELLOW_EX +"Ingrese un valor para seleccionar una opcion: ") ##pedir opcion 
                        sub_menu_2 = int(sub_menu_2_str)
                        if sub_menu_2 == 1:
                            fila_m1 = int(input("Ingrese la fila: "))
                            columna_m1 = int(input("Ingrese la columna: "))
                            #Validar que la posicion este libre
                            bandera = celdas_1.CeldaEstaVacia(fila_m1, columna_m1)
                            if bandera == True: #ya existe en coordenada
                                print(Fore.RED +"En esta celda ya existe un organismo")
                            else: #No existe, entonces agrega la posicion
                                # celdas_1.Insertar(fila_m1,columna_m1,organis,color_organis)
                                celdas_1.AgregarOrganismoMuestra(limite_vertical, limite_horizontal, fila_m1,columna_m1,organis,color_organis,celdas_1, ListaProstera1)
                                DibujarModificacion(celdas_1,limite_vertical, limite_horizontal)
                        if sub_menu_2 == 0:
                            print(Fore.LIGHTYELLOW_EX +"Salida del xml con la muestra nueva y termina ciclo ")
                            break
                if numero_muestra == 2:
                    ListaProstera2 = celdas_2.ObtenerOrganismoProspe(limite_vertical,limite_horizontal, organis, celdas_2)
                    Dibujar(celdas_2, ListaProstera2,limite_vertical, limite_horizontal)
                    while True:
                        print(Fore.LIGHTYELLOW_EX + '\n----------------------------------------------------')
                        print(Fore.LIGHTYELLOW_EX + '|            ¿Desea agregar un organismo?          |')
                        print(Fore.LIGHTYELLOW_EX + '|    [1]. Si                                       |')
                        print(Fore.LIGHTYELLOW_EX + '|    [0]. No                                       |')
                        print(Fore.LIGHTYELLOW_EX + '----------------------------------------------------')
                        sub_menu_3_str = input(Fore.LIGHTYELLOW_EX +"Ingrese un valor para seleccionar una opcion: ") ##pedir opcion 
                        sub_menu_3 = int(sub_menu_3_str)
                        if sub_menu_3 == 1:
                            fila_m2 = int(input("Ingrese la fila: "))
                            columna_m2 = int(input("Ingrese la columna: "))
                            #Validar que la posicion este libre
                            bandera_2 = celdas_2.CeldaEstaVacia(fila_m2, columna_m2)
                            if bandera_2 == True: #ya existe en coordenada
                                print(Fore.RED +"En esta celda ya existe un organismo")
                            else: #No existe, entonces agrega la posicion
                                # celdas_1.Insertar(fila_m1,columna_m1,organis,color_organis)
                                celdas_2.AgregarOrganismoMuestra(limite_vertical, limite_horizontal, fila_m2,columna_m2,organis,color_organis,celdas_2, ListaProstera2)
                                DibujarModificacion(celdas_2,limite_vertical, limite_horizontal)
                        if sub_menu_3 == 0:
                            print(Fore.LIGHTYELLOW_EX +"Salida del xml con la muestra nueva y termina ciclo ")
                            break
                if numero_muestra == 3:
                    ListaProstera3 = celdas_3.ObtenerOrganismoProspe(limite_vertical,limite_horizontal, organis, celdas_3)
                    Dibujar(celdas_3, ListaProstera3,limite_vertical, limite_horizontal)
                    while True:
                        print(Fore.LIGHTYELLOW_EX + '\n----------------------------------------------------')
                        print(Fore.LIGHTYELLOW_EX + '|            ¿Desea agregar un organismo?          |')
                        print(Fore.LIGHTYELLOW_EX + '|    [1]. Si                                       |')
                        print(Fore.LIGHTYELLOW_EX + '|    [0]. No                                       |')
                        print(Fore.LIGHTYELLOW_EX + '----------------------------------------------------')
                        sub_menu_4_str = input(Fore.LIGHTYELLOW_EX +"Ingrese un valor para seleccionar una opcion: ") ##pedir opcion 
                        sub_menu_4 = int(sub_menu_4_str)
                        if sub_menu_4 == 1:
                            fila_m3 = int(input("Ingrese la fila: "))
                            columna_m3 = int(input("Ingrese la columna: "))
                            #Validar que la posicion este libre
                            bandera3 = celdas_3.CeldaEstaVacia(fila_m3, columna_m3)
                            if bandera3 == True: #ya existe en coordenada
                                print(Fore.RED +"En esta celda ya existe un organismo")
                            else: #No existe, entonces agrega la posicion
                                # celdas_1.Insertar(fila_m1,columna_m1,organis,color_organis)
                                celdas_3.AgregarOrganismoMuestra(limite_vertical, limite_horizontal, fila_m3,columna_m3,organis,color_organis,celdas_3, ListaProstera3)
                                DibujarModificacion(celdas_3,limite_vertical, limite_horizontal)
                        if sub_menu_4 == 0:
                            print(Fore.LIGHTYELLOW_EX +"Salida del xml con la muestra nueva y termina ciclo ")
                            break
                if numero_muestra == 4:
                    ListaProstera4 = celdas_4.ObtenerOrganismoProspe(limite_vertical,limite_horizontal, organis, celdas_4)
                    Dibujar(celdas_4, ListaProstera4,limite_vertical, limite_horizontal)
                    while True:
                        print(Fore.LIGHTYELLOW_EX + '\n----------------------------------------------------')
                        print(Fore.LIGHTYELLOW_EX + '|            ¿Desea agregar un organismo?          |')
                        print(Fore.LIGHTYELLOW_EX + '|    [1]. Si                                       |')
                        print(Fore.LIGHTYELLOW_EX + '|    [0]. No                                       |')
                        print(Fore.LIGHTYELLOW_EX + '----------------------------------------------------')
                        sub_menu_5_str = input(Fore.LIGHTYELLOW_EX +"Ingrese un valor para seleccionar una opcion: ") ##pedir opcion 
                        sub_menu_5 = int(sub_menu_5_str)
                        if sub_menu_5 == 1:
                            fila_m5 = int(input("Ingrese la fila: "))
                            columna_m5 = int(input("Ingrese la columna: "))
                            #Validar que la posicion este libre
                            bandera4 = celdas_4.CeldaEstaVacia(fila_m5, columna_m5)
                            if bandera4 == True: #ya existe en coordenada
                                print(Fore.RED +"En esta celda ya existe un organismo")
                            else: #No existe, entonces agrega la posicion
                                # celdas_1.Insertar(fila_m1,columna_m1,organis,color_organis)
                                celdas_4.AgregarOrganismoMuestra(limite_vertical, limite_horizontal, fila_m5,columna_m5,organis,color_organis,celdas_4, ListaProstera4)
                                DibujarModificacion(celdas_4,limite_vertical, limite_horizontal)
                        if sub_menu_5 == 0:
                            print(Fore.LIGHTYELLOW_EX +"Salida del xml con la muestra nueva y termina ciclo ")
                            break
                if numero_muestra == 5:
                    ListaProstera5 = celdas_5.ObtenerOrganismoProspe(limite_vertical,limite_horizontal, organis, celdas_5)
                    Dibujar(celdas_5, ListaProstera5,limite_vertical, limite_horizontal)
                    while True:
                        print(Fore.LIGHTYELLOW_EX + '\n----------------------------------------------------')
                        print(Fore.LIGHTYELLOW_EX + '|            ¿Desea agregar un organismo?          |')
                        print(Fore.LIGHTYELLOW_EX + '|    [1]. Si                                       |')
                        print(Fore.LIGHTYELLOW_EX + '|    [0]. No                                       |')
                        print(Fore.LIGHTYELLOW_EX + '----------------------------------------------------')
                        sub_menu_6_str = input(Fore.LIGHTYELLOW_EX +"Ingrese un valor para seleccionar una opcion: ") ##pedir opcion 
                        sub_menu_6 = int(sub_menu_6_str)
                        if sub_menu_6 == 1:
                            fila_m6 = int(input("Ingrese la fila: "))
                            columna_m6 = int(input("Ingrese la columna: "))
                            #Validar que la posicion este libre
                            bandera6 = celdas_5.CeldaEstaVacia(fila_m6, columna_m6)
                            if bandera6 == True: #ya existe en coordenada
                                print(Fore.RED +"En esta celda ya existe un organismo")
                            else: #No existe, entonces agrega la posicion
                                # celdas_1.Insertar(fila_m1,columna_m1,organis,color_organis)
                                celdas_5.AgregarOrganismoMuestra(limite_vertical, limite_horizontal, fila_m6,columna_m6,organis,color_organis,celdas_5, ListaProstera5)
                                DibujarModificacion(celdas_5,limite_vertical, limite_horizontal)
                        if sub_menu_6 == 0:
                            print(Fore.LIGHTYELLOW_EX +"Salida del xml con la muestra nueva y termina ciclo ")
                            break
                
                '''
                [1].  Ingrese el codigo de la muestra
                    -Estas son las corrdenadas donde puede vivir x organismo de la propia muestra (repite con todos organismos)
                    -?Desea ingresar organismos [s/n]
                        -ingrese la coordenada
                            -mostrar cambios, si muere o ya no se pueden ingresar mas(posiciones donde puedar seguir metiendo organismos). REGRESAR A ?desea ingresar
                '''
            if menu_principal == 3:     #Opcion tres del menu Principal
                # Filtros()               #funcion para mostrar sub menu Filtro
                '''
                [1]. Codigo de la muestra a modificar 
                    -ingrese cordenadas y organismo que desea agregar
                    -desea agregar mas? [s/n] (si -perdir info) (no -desea crear una muestra nueva con estos datos #o actualizar la muestra[s/n])  
                '''
            if menu_principal == 5:        #if que simula el do-while
                print(Fore.RED+"Hasta la proxima :)")
                break
    except Exception as err:
        print(Fore.RED+"\n\tSe acaba de producir un error :( " + str(err))
        print(Fore.RED+"\tAsegurate de leer el MANUAL DE USUARIO")
    else:
        break

