from TDA.ListaDibujo import ListaDibujo


def Dibujar(celdas_1, celdas_prosperan, limite_vertical, limite_horizontal):
    ListaElementosDibujar = ListaDibujo(limite_vertical, limite_horizontal)
    
    for rows in range(limite_vertical):
        for cols in range(limite_horizontal):
            #Verificar si en esta posicion hay celdas
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
                color = celdas_1.BuscarColor(rows,cols)
                ListaElementosDibujar.Insertar(rows, cols, color, 'Green')

                if cols+1 < limite_horizontal:
                    ListaElementosDibujar.Insertar(rows, cols+1, 'White', 'Black')
                if rows+1 < limite_vertical and cols-1 >= 0:
                    ListaElementosDibujar.Insertar(rows+1, cols-1, 'White', 'Black')
                if rows+1 < limite_vertical:
                    ListaElementosDibujar.Insertar(rows + 1, cols, 'White', 'Black')
                if rows+1 < limite_vertical and cols+1 < limite_horizontal:
                    ListaElementosDibujar.Insertar(rows+1, cols+1, 'White', 'Black')



            # # Verificar si en esta posicion hay celdas donde prosperan
            # if celdas_prosperan.BuscarPosicion(rows,cols):
            #     #mismos metodos
            #     if cols - 1 >= 0 and rows -1 >= 0:
            #         ListaElementosDibujar.Insertar(rows - 1, cols - 1, 'White', 'Black')
            #     if rows - 1 >= 0:
            #         ListaElementosDibujar.Insertar(rows - 1, cols, 'White', 'Black')
            #     if rows - 1 >= 0 and cols + 1 < limite_horizontal:
            #         ListaElementosDibujar.Insertar(rows - 1, cols+1, 'White', 'Black')
            #     if cols -1 > 0:
            #         ListaElementosDibujar.Insertar(rows, cols-1, 'White', 'Black')

            #     #Quiero graficar la celdaOrganismoProspera 
            #     color = celdas_prosperan.BuscarColor(rows,cols)
            #     ListaElementosDibujar.Insertar(rows, cols, str(color), 'Green')

            #     if cols + 1 < limite_horizontal:
            #         ListaElementosDibujar.Insertar(rows, cols+1, 'White', 'Black')
            #     if rows + 1 < limite_vertical and cols - 1 >= 0:
            #         ListaElementosDibujar.Insertar(rows + 1, cols-1, 'White', 'Black')
            #     if rows + 1 < limite_vertical:
            #         ListaElementosDibujar.Insertar(rows + 1, cols, 'White', 'Black')
            #     if rows+1 < limite_vertical and cols + 1 < limite_horizontal:
            #         ListaElementosDibujar.Insertar(rows + 1, cols + 1, 'White', 'Black')
    ListaElementosDibujar.GenerarDibujo()
