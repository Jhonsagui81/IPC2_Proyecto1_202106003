from TDA.ListaDibujo import ListaDibujo
import subprocess

def Dibujar(celdas_1, celdas_prosperan, limite_vertical, limite_horizontal):
    ListaElementosDibujar = ListaDibujo(limite_vertical, limite_horizontal)
    
    for rows in range(limite_vertical):
        for cols in range(limite_horizontal):
            # Verificar si en esta posicion hay celdas
            if celdas_1.BuscarPosicion(rows,cols):
                if cols-1 >= 0 and rows-1 >= 0:
                    ListaElementosDibujar.Insertar(rows-1, cols-1, 'White', 'Black')
                if rows-1 >= 0:
                    ListaElementosDibujar.Insertar(rows-1, cols, 'White', 'Black')
                if rows-1 >= 0 and cols+1 < limite_horizontal:
                    ListaElementosDibujar.Insertar(rows-1, cols+1, 'White', 'Black')
                if cols-1 > 0:
                    ListaElementosDibujar.Insertar(rows, cols-1, 'White', 'Black')

                #Quiero graficar la celdaOrganismo
                colorR = celdas_1.BuscarColor(rows,cols)
                ListaElementosDibujar.Insertar(rows, cols, colorR, 'Green')
                if cols+1 < limite_horizontal:
                    ListaElementosDibujar.Insertar(rows, cols+1, 'White', 'Black')
                if rows+1 < limite_vertical and cols-1 >= 0:
                    ListaElementosDibujar.Insertar(rows+1, cols-1, 'White', 'Black')
                if rows+1 < limite_vertical:
                    ListaElementosDibujar.Insertar(rows + 1, cols, 'White', 'Black')
                if rows+1 < limite_vertical and cols+1 < limite_horizontal:
                    ListaElementosDibujar.Insertar(rows+1, cols+1, 'White', 'Black')
            else:
                ListaElementosDibujar.Insertar(rows, cols, 'White', 'Black')

                ##Para celdas que puede comer
            if celdas_prosperan.BuscarPosicion(rows,cols):
                if cols-1 >= 0 and rows-1 >= 0:
                    ListaElementosDibujar.Insertar(rows-1, cols-1, 'White', 'Black')
                if rows-1 >= 0:
                    ListaElementosDibujar.Insertar(rows-1, cols, 'White', 'Black')
                if rows-1 >= 0 and cols+1 < limite_horizontal:
                    ListaElementosDibujar.Insertar(rows-1, cols+1, 'White', 'Black')
                if cols-1 > 0:
                    ListaElementosDibujar.Insertar(rows, cols-1, 'White', 'Black')

                #Quiero graficar la celdaOrganismo
                colorP = celdas_prosperan.BuscarColor(rows,cols)
                ListaElementosDibujar.Insertar(rows, cols, colorP, 'Green')
        
                if cols+1 < limite_horizontal:
                    ListaElementosDibujar.Insertar(rows, cols+1, 'White', 'Black')
                if rows+1 < limite_vertical and cols-1 >= 0:
                    ListaElementosDibujar.Insertar(rows+1, cols-1, 'White', 'Black')
                if rows+1 < limite_vertical:
                    ListaElementosDibujar.Insertar(rows + 1, cols, 'White', 'Black')
                if rows+1 < limite_vertical and cols+1 < limite_horizontal:
                    ListaElementosDibujar.Insertar(rows+1, cols+1, 'White', 'Black')
            else:
                ListaElementosDibujar.Insertar(rows, cols, 'White', 'Black')


    ListaElementosDibujar.GenerarDibujo()
    cmd_str = "dot -Tsvg -O ./Documentacion/Dibujo.dot"
    subprocess.run(cmd_str, shell=True)
