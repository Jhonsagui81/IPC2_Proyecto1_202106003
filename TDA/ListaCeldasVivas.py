from .Nodo import NodoCeldas

class ListaCeldas:

    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Limite = 1
    
    def Insertar(self, fila, columna, codigo_organismo, color):
        NuevoNodo = NodoCeldas(fila, columna, codigo_organismo, color)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.Limite += 1
        else:
            self.Limite += 1
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def BuscarOrganismoPuedeProsperar(self, limiteVertical, limiteHorizontal, orga, listaCeldas):
        Auxiliar = self.Inicio
        Retorno = "\n"
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() == orga:
                #datos de ficha a estudiar
                fila = Auxiliar.ObtenerFila()
                columna = Auxiliar.ObtenerColumna()
                color = Auxiliar.ObtenerOrganismoVivo()
                #VALIDACIONES PARA DIAGONALES 
                # --> Inferior Derecha.
                if listaCeldas.BuscarPosicionDiferente(fila+1, columna+1, color): 
                    aux = self.Inicio
                    contFila_inferior_derecha = 2
                    contColu_inferior_derecha = 2
                    while aux != None: 
                        if listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_derecha, columna+contColu_inferior_derecha, color):
                            contFila_inferior_derecha += 1
                            contColu_inferior_derecha += 1
                            aux = self.Inicio  
                            if listaCeldas.BuscarPosicionIdentica(fila+contFila_inferior_derecha, columna+contColu_inferior_derecha, color):
                                break                          
                        if not (listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_derecha, columna+contColu_inferior_derecha, color)): 
                            if (fila+contFila_inferior_derecha < 0 or fila+contFila_inferior_derecha > limiteVertical) and (columna+contColu_inferior_derecha < 0 or columna+contColu_inferior_derecha>limiteHorizontal):
                                #SE excedio del tablero 
                                break
                            else:
                                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+contFila_inferior_derecha)+" Columna: "+str(columna+contColu_inferior_derecha))
                                break
                        aux = aux.Siguiente
                # --> Inferior Izquierda.
                if listaCeldas.BuscarPosicionDiferente(fila+1, columna-1, color): 
                    aux = self.Inicio
                    contFila_inferior_izquierda = 2
                    contColu_inferior_izquierda = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_izquierda, columna-contColu_inferior_izquierda, color):
                            contFila_inferior_izquierda += 1
                            contColu_inferior_izquierda += 1
                            aux = self.Inicio  
                            if listaCeldas.BuscarPosicionIdentica(fila+contFila_inferior_izquierda, columna-contColu_inferior_izquierda, color):
                                break                           
                        if not (listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_izquierda, columna-contColu_inferior_izquierda, color)): 
                            #VALIDAR LIMITE TABLERO
                            if(fila+contFila_inferior_izquierda < 0 or fila+contFila_inferior_izquierda > limiteVertical) and (columna-contColu_inferior_izquierda < 0 or columna-contColu_inferior_izquierda > limiteHorizontal): 
                                break
                            else:
                                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+contFila_inferior_izquierda)+" Columna: "+str(columna-contColu_inferior_izquierda))
                                break
                        aux = aux.Siguiente
                # --> Superior Derecha
                if listaCeldas.BuscarPosicionDiferente(fila-1, columna+1, color): 
                    aux = self.Inicio
                    contFila_superior_derecha = 2
                    contColu_superior_derecha = 2
                    while aux != None:  
                        if listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_derecha, columna+contColu_superior_derecha, color):
                            contFila_superior_derecha += 1
                            contColu_superior_derecha += 1
                            aux = self.Inicio 
                            if listaCeldas.BuscarPosicionIdentica(fila-contFila_superior_derecha, columna+contColu_superior_derecha, color):
                                break                           
                        if not (listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_derecha, columna+contColu_superior_derecha, color)): 
                            if(fila-contFila_superior_derecha < 0 or fila-contFila_superior_derecha > limiteVertical)and(columna+contColu_superior_derecha < 0 or columna+contColu_superior_derecha > limiteHorizontal):
                                break
                            else:
                                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-contFila_superior_derecha)+" Columna: "+str(columna+contColu_superior_derecha))
                                break
                        aux = aux.Siguiente
                # --> Superior Izquierda
                if listaCeldas.BuscarPosicionDiferente(fila-1, columna-1, color): 
                    aux = self.Inicio
                    contFila_superior_izquierda = 2
                    contColu_superior_izquierda = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, color):
                            contFila_superior_izquierda += 1
                            contColu_superior_izquierda += 1
                            aux = self.Inicio
                            if listaCeldas.BuscarPosicionIdentica(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, color):
                                break                            
                        if not (listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, color)): 
                            if(fila-contFila_superior_izquierda < 0 or fila-contFila_superior_izquierda > limiteVertical)and(columna-contColu_superior_izquierda < 0 or columna-contColu_superior_izquierda > limiteHorizontal):
                                break
                            else:
                                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-contFila_superior_izquierda)+" Columna: "+str(columna-contColu_superior_izquierda))
                                break
                        aux = aux.Siguiente
                
                #VALIDACIONES PARA VERTICALES 
                # --> Arriba 
                if listaCeldas.BuscarPosicionDiferente(fila+1, columna, color): 
                    aux = self.Inicio
                    contFila_arriba = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila+contFila_arriba, columna, color):
                            contFila_arriba += 1
                            aux = self.Inicio  
                            if listaCeldas.BuscarPosicionIdentica(fila+contFila_arriba,columna, color):
                                break                            
                        if not (listaCeldas.BuscarPosicionDiferente(fila+contFila_arriba, columna, color)): 
                            if(fila+contFila_arriba < 0 or fila+contFila_arriba > limiteVertical):
                                break
                            else:
                                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+contFila_arriba)+" Columna: "+str(columna))
                                break
                        aux = aux.Siguiente
                # --> Abajo
                if listaCeldas.BuscarPosicionDiferente(fila-1, columna, color): 
                    aux = self.Inicio
                    contFila_abajo = 2
                    while aux != None: 
                        if listaCeldas.BuscarPosicionDiferente(fila-contFila_abajo, columna, color):
                            contFila_abajo += 1
                            aux = self.Inicio
                            if listaCeldas.BuscarPosicionIdentica(fila-contFila_abajo,columna, color):
                                break                            
                        if not (listaCeldas.BuscarPosicionDiferente(fila-contFila_abajo, columna, color)): 
                            if(fila-contFila_abajo < 0 or fila-contFila_abajo > limiteVertical):
                                break
                            else:
                                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-contFila_abajo)+" Columna: "+str(columna))
                                break
                        aux = aux.Siguiente

                #VALIDACIONES PARA HORIZONTALES 
                # --> Derecha
                if listaCeldas.BuscarPosicionDiferente(fila, columna+1, color): 
                    aux = self.Inicio
                    contColum_derecha = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila, columna+contColum_derecha, color):
                            contColum_derecha += 1
                            aux = self.Inicio  
                            if listaCeldas.BuscarPosicionIdentica(fila,columna+contColum_derecha,color):
                                break                          
                        if not (listaCeldas.BuscarPosicionDiferente(fila, columna+contColum_derecha, color)): 
                            if(columna+contColum_derecha < 0 or columna+contColum_derecha > limiteHorizontal):
                                break
                            else:
                                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila)+" Columna: "+str(columna+contColum_derecha))
                                break
                        aux = aux.Siguiente
                # --> Izquierda
                if listaCeldas.BuscarPosicionDiferente(fila, columna-1, color): 
                    aux = self.Inicio
                    contColum_izquierda = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila, columna-contColum_izquierda, color):
                            contColum_izquierda += 1
                            aux = self.Inicio       
                            if listaCeldas.BuscarPosicionIdentica(fila,columna-contColum_izquierda,color):
                                break                      
                        if not (listaCeldas.BuscarPosicionDiferente(fila, columna-contColum_izquierda, color)): 
                            if(columna-contColum_izquierda < 0 or columna-contColum_izquierda > limiteHorizontal):
                                break
                            else:
                                print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila)+" Columna: "+str(columna-contColum_izquierda))
                                break
                        aux = aux.Siguiente

            #para recorrer lista de organismo
            Auxiliar = Auxiliar.Siguiente
        return Retorno 

    def BuscarPosicionDiferente(self, fila, columna, color):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() != color:   
                if (Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna):
                    return True
            Auxiliar = Auxiliar.Siguiente
        return False

    #NO es util aun 
    def VerifivarVacio(self, fila, columna):
        Auxiliar = self.Inicio
        bandera = False
        while Auxiliar != None:
            if (Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna):
                bandera = True
            Auxiliar = Auxiliar.Siguiente

        if bandera == False: #En toda la lista no hay posiciones en esas coordenadas 
            return True
        else:
            return False    #si existe posicion 

    def BuscarPosicionIdentica(self, fila, columna, color):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() == color:   
                if (Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna):
                    return True
            Auxiliar = Auxiliar.Siguiente
        return False

    def pendienteDEusar(self, muestra, orga, listaCeldas):
        Auxiliar = self.Inicio
        Retorno = "\n"
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() == orga:
                #datos de ficha a estudiar
                fila = Auxiliar.ObtenerFila()
                columna = Auxiliar.ObtenerColumna()
                color = Auxiliar.ObtenerOrganismoVivo()
                #VALIDACIONES PARA DIAGONALES 
                # --> Inferior Derecha.
                if listaCeldas.BuscarPosicionDiferente(fila+1, columna+1, color): 
                    aux = self.Inicio
                    contFila_inferior_derecha = 2
                    contColu_inferior_derecha = 2
                    while aux != None: 
                        if listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_derecha, columna+contColu_inferior_derecha, color):
                            contFila_inferior_derecha += 1
                            contColu_inferior_derecha += 1
                            aux = self.Inicio  
                            if listaCeldas.BuscarPosicionIdentica(fila+contFila_inferior_derecha, columna+contColu_inferior_derecha, color):
                                break                          
                        if not (listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_derecha, columna+contColu_inferior_derecha, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+contFila_inferior_derecha)+" Columna: "+str(columna+contColu_inferior_derecha))
                            break
                        aux = aux.Siguiente
                # --> Inferior Izquierda.
                if listaCeldas.BuscarPosicionDiferente(fila+1, columna-1, color): 
                    aux = self.Inicio
                    contFila_inferior_izquierda = 2
                    contColu_inferior_izquierda = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_izquierda, columna-contColu_inferior_izquierda, color):
                            contFila_inferior_izquierda += 1
                            contColu_inferior_izquierda += 1
                            aux = self.Inicio  
                            if listaCeldas.BuscarPosicionIdentica(fila+contFila_inferior_izquierda, columna-contColu_inferior_izquierda, color):
                                break                           
                        if not (listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_izquierda, columna-contColu_inferior_izquierda, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+contFila_inferior_izquierda)+" Columna: "+str(columna-contColu_inferior_izquierda))
                            break
                        aux = aux.Siguiente
                # --> Superior Derecha
                if listaCeldas.BuscarPosicionDiferente(fila-1, columna+1, color): 
                    aux = self.Inicio
                    contFila_superior_derecha = 2
                    contColu_superior_derecha = 2
                    while aux != None:  
                        if listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_derecha, columna+contColu_superior_derecha, color):
                            contFila_superior_derecha += 1
                            contColu_superior_derecha += 1
                            aux = self.Inicio 
                            if listaCeldas.BuscarPosicionIdentica(fila-contFila_superior_derecha, columna+contColu_superior_derecha, color):
                                break                           
                        if not (listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_derecha, columna+contColu_superior_derecha, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-contFila_superior_derecha)+" Columna: "+str(columna+contColu_superior_derecha))
                            break
                        aux = aux.Siguiente
                # --> Superior Izquierda
                if listaCeldas.BuscarPosicionDiferente(fila-1, columna-1, color): 
                    aux = self.Inicio
                    contFila_superior_izquierda = 2
                    contColu_superior_izquierda = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, color):
                            contFila_superior_izquierda += 1
                            contColu_superior_izquierda += 1
                            aux = self.Inicio
                            if listaCeldas.BuscarPosicionIdentica(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, color):
                                break                            
                        if not (listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-contFila_superior_izquierda)+" Columna: "+str(columna-contColu_superior_izquierda))
                            break
                        aux = aux.Siguiente
                
                #VALIDACIONES PARA VERTICALES 
                # --> Arriba 
                if listaCeldas.BuscarPosicionDiferente(fila+1, columna, color): 
                    aux = self.Inicio
                    contFila_arriba = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila+contFila_arriba, columna, color):
                            contFila_arriba += 1
                            aux = self.Inicio  
                            if listaCeldas.BuscarPosicionIdentica(fila+contFila_arriba,columna, color):
                                break                            
                        if not (listaCeldas.BuscarPosicionDiferente(fila+contFila_arriba, columna, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+contFila_arriba)+" Columna: "+str(columna))
                            break
                        aux = aux.Siguiente
                # --> Abajo
                if listaCeldas.BuscarPosicionDiferente(fila-1, columna, color): 
                    aux = self.Inicio
                    contFila_abajo = 2
                    while aux != None: 
                        if listaCeldas.BuscarPosicionDiferente(fila-contFila_abajo, columna, color):
                            contFila_abajo += 1
                            aux = self.Inicio
                            if listaCeldas.BuscarPosicionIdentica(fila-contFila_abajo,columna, color):
                                break                            
                        if not (listaCeldas.BuscarPosicionDiferente(fila-contFila_abajo, columna, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-contFila_abajo)+" Columna: "+str(columna))
                            break
                        aux = aux.Siguiente

                #VALIDACIONES PARA HORIZONTALES 
                # --> Derecha
                if listaCeldas.BuscarPosicionDiferente(fila, columna+1, color): 
                    aux = self.Inicio
                    contColum_derecha = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila, columna+contColum_derecha, color):
                            contColum_derecha += 1
                            aux = self.Inicio  
                            if listaCeldas.BuscarPosicionIdentica(fila,columna+contColum_derecha,color):
                                break                          
                        if not (listaCeldas.BuscarPosicionDiferente(fila, columna+contColum_derecha, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila)+" Columna: "+str(columna+contColum_derecha))
                            break
                        aux = aux.Siguiente
                # --> Izquierda
                if listaCeldas.BuscarPosicionDiferente(fila, columna-1, color): 
                    aux = self.Inicio
                    contColum_izquierda = 2
                    while aux != None:
                        if listaCeldas.BuscarPosicionDiferente(fila, columna-contColum_izquierda, color):
                            contColum_izquierda += 1
                            aux = self.Inicio       
                            if listaCeldas.BuscarPosicionIdentica(fila,columna-contColum_izquierda,color):
                                break                      
                        if not (listaCeldas.BuscarPosicionDiferente(fila, columna-contColum_izquierda, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila)+" Columna: "+str(columna-contColum_izquierda))
                            break
                        aux = aux.Siguiente

            #para recorrer lista de organismo
            Auxiliar = Auxiliar.Siguiente
        return Retorno 