from TDA.ListaMuestra import ListaMuestra
from TDA.ListaCeldasVivas import ListaCeldas
from TDA.ListaOrganismos import ListaOrganismos
from colorama import Fore
from lectura import LecturaXML

my_muestras = ListaMuestra()
my_celdas_vivas = ListaCeldas()
my_organismos = ListaOrganismos()

while True:
# try:
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
        print(Fore.CYAN +"|    [3]. Actualizar informacion de una muestra    |")
        print(Fore.CYAN +"|    [4]. Generar xml con muestras actualizadas    |")
        print(Fore.CYAN +"|    [5]. Carga de archivo + lo del anterior (??)  |")
        print(Fore.CYAN +"|                                                  |")
        print(Fore.CYAN +"----------------------------------------------------")
        menu_principal_str = input(Fore.CYAN +"Ingrese un valor para seleccionar una opcion: ")
        menu_principal = int(menu_principal_str)    #Parseando opcion 
        if menu_principal == 1:   #Opcion 1 del menu principal
            LecturaXML(my_muestras,my_celdas_vivas, my_organismos)   #funcion para cargar archivo
        if menu_principal == 2:     #Opcion 2 del menu principal
            # GestionadorPeliculas() #funcion para mostrar sub menu Gestionador
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
        if menu_principal == 4:     #Opcion 4 del menu princiapal
            # print(Fore.LIGHTMAGENTA_EX+"Procesando relaciones...")   
            # mi_peliculas.GraficaRelacion()
            '''
            [1].  Generar archivo con todas las muestras + las actualizadas - se recomienda generar una salida cada que deje de de modificar la muestra
            '''
        if menu_principal == 5:        #if que simula el do-while
            print(Fore.RED+"Hasta la proxima :)")
            break
# except Exception as err:
#     print(Fore.RED+"\n\tSe acaba de producir un error :( " + str(err))
#     print(Fore.RED+"\tAsegurate de leer el MANUAL DE USUARIO")
# else:
#     break

