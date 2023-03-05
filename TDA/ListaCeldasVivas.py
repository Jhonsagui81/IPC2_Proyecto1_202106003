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
    
    def BuscarOrganismoPuedeProsperar(self, muestra, orga, listaCeldas):
        Auxiliar = self.Inicio
        Retorno = "\n"
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() == orga:
                #datos de ficha a estudiar
                fila = Auxiliar.ObtenerFila()
                columna = Auxiliar.ObtenerColumna()
                color = Auxiliar.ObtenerColor()
                ##VALIDACIONES PARA DIAGONALES 
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
                        if not (listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, color)): 
                            print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-contFila_superior_izquierda)+" Columna: "+str(columna-contColu_superior_izquierda))
                            break
                        aux = aux.Siguiente

                #comer 4: fila -1   columna-1
                if listaCeldas.BuscarPosicionDiferente(fila-1, columna-1, color):
                    if listaCeldas.BuscarPosicionIdentica(fila-2, columna-2, color):
                        print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-1)+" Columna: "+str(columna-1))
            Auxiliar = Auxiliar.Siguiente
        return Retorno
        #debe retornar algo si o si 

    def BuscarPosicionDiferente(self, fila, columna, color):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerColor() != color:   
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
            if Auxiliar.ObtenerColor() == color:   
                if (Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna):
                    return True
            Auxiliar = Auxiliar.Siguiente
        return False