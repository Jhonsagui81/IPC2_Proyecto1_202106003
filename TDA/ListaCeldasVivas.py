from .Nodo import NodoCeldas
from colorama import Fore

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
    ##METODOS PARA VALIDAR QUE CELDAS PUEDEN PROSPERAR, CUALQUIER ORGANISMO
    def ObtenerOrganismoProspe(self, limiteVertical, limiteHorizontal, orga, listaCeldas):
        ListaProspera = ListaCeldas()
        Auxiliar = self.Inicio
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
                                #ingresa la posicion donde prospera 
                                ListaProspera.Insertar(fila+contFila_inferior_derecha,columna+contColu_inferior_derecha, orga, "Silver")
                                print("Fila: "+str(fila+contFila_inferior_derecha)+" , Columna: "+str(columna+contColu_inferior_derecha))
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
                                ListaProspera.Insertar(fila+contFila_inferior_izquierda,columna-contColu_inferior_izquierda,orga,"Silver")
                                print("Fila: "+str(fila+contFila_inferior_izquierda)+" , Columna: "+str(columna-contColu_inferior_izquierda))
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
                                ListaProspera.Insertar(fila-contFila_superior_derecha, columna+contColu_superior_derecha, orga, "Silver")
                                print("Fila: "+str(fila-contFila_superior_derecha)+" , Columna: "+str(columna+contColu_superior_derecha))
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
                                ListaProspera.Insertar(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, orga, "Silver")
                                print("Fila: "+str(fila-contFila_superior_izquierda)+" , Columna: "+str(columna-contColu_superior_izquierda))
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
                                ListaProspera.Insertar(fila+contFila_arriba,columna,orga,"Silver")
                                print("Fila: "+str(fila+contFila_arriba)+" , Columna: "+str(columna))
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
                                ListaProspera.Insertar(fila-contFila_abajo,columna,orga,"Silver")
                                print("Fila: "+str(fila-contFila_abajo)+" , Columna: "+str(columna))
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
                                ListaProspera.Insertar(fila,columna+contColum_derecha, orga, "Silver")
                                print("Fila: "+str(fila)+" , Columna: "+str(columna+contColum_derecha))
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
                                ListaProspera.Insertar(fila, columna-contColum_izquierda, orga, "Silver")
                                print("Fila: "+str(fila)+" , Columna: "+str(columna-contColum_izquierda))
                                break
                        aux = aux.Siguiente

            #para recorrer lista de organismo
            Auxiliar = Auxiliar.Siguiente
        return ListaProspera

    def BuscarPosicionDiferente(self, fila, columna, codigo):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() != codigo:   
                if (Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna):
                    return True
            Auxiliar = Auxiliar.Siguiente
        return False

    def Imiprimir(self):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            print("Fila: " + str(Auxiliar.ObtenerFila()))
            print("Columna: "+ str(Auxiliar.ObtenerColumna()))
            Auxiliar = Auxiliar.Siguiente

    def BuscarPosicionIdentica(self, fila, columna, color):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() == color:   
                if (Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna):
                    return True
            Auxiliar = Auxiliar.Siguiente
        return False
    
    def BuscarPosicion(self, Fila, Columna):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            #print("Fila: "+str(Fila+1) + " Columna: "+str(Columna+1))
            #print(Auxiliar.ObtenerFila(), Auxiliar.ObtenerColumna())
            if (Auxiliar.ObtenerFila() == Fila and Auxiliar.ObtenerColumna() == Columna):
                return True
            Auxiliar = Auxiliar.Siguiente
        return False
    
    def BuscarColor(self, Fila, Columna):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            #print("Fila: "+str(Fila+1) + " Columna: "+str(Columna+1))
            #print(Auxiliar.ObtenerFila(), Auxiliar.ObtenerColumna())
            if (Auxiliar.ObtenerFila() == Fila and Auxiliar.ObtenerColumna() == Columna):
                return Auxiliar.ObtenerColor()
            Auxiliar = Auxiliar.Siguiente


    ##METODOS PARA PINTAR LAS CELDAS QUE INGRESE USUARIO
    def BuscarColorCodigo(self, codigo):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() == codigo:
                return Auxiliar.ObtenerColor()
            Auxiliar = Auxiliar.Siguiente

    def CeldaEstaVacia(self, fila, columna):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna:
                return True
            Auxiliar = Auxiliar.Siguiente
        return False
    
    def BuscarPosicionDiferenteParaPintar(self, fila, columna, codigo, color):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() != codigo:   
                if (Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna):
                    Auxiliar.setCodigo(codigo)
                    Auxiliar.setColor(color)
                    return True
            Auxiliar = Auxiliar.Siguiente
        return False
    
    def AgregarOrganismoMuestra(self, limiteVertical, limiteHorizontal, fila, columna, codigo, color, listaCeldas, listaProspera1):
        ListaProspera = ListaCeldas()
        #Valida si la fila y columna esta en lista que almacena donde puede comer 
        if listaProspera1.CeldaEstaVacia(fila, columna):
            #agrega la ficha a su lista
            print("Las celdas que se come esta nueva ficha son: ")
            #VALIDACIONES PARA DIAGONALES 
            # --> Inferior Derecha.
            if listaCeldas.BuscarPosicionDiferente(fila+1, columna+1, codigo): 
                aux = self.Inicio
                contFila_inferior_derecha = 2
                contColu_inferior_derecha = 2
                while aux != None: 
                    if listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_derecha, columna+contColu_inferior_derecha, codigo):
                        contFila_inferior_derecha += 1
                        contColu_inferior_derecha += 1
                        aux = self.Inicio  
                        #La siguiente posicion es hermano por tanto ya no puede comer 
                        if listaCeldas.BuscarPosicionIdentica(fila+contFila_inferior_derecha, columna+contColu_inferior_derecha, codigo):
                            for i1 in range(1,contColu_inferior_derecha):
                                print("FIla: "+str(fila+(i1 ))+"  ,  Columna: "+str(columna+(i1 )))
                                listaCeldas.BuscarPosicionDiferenteParaPintar(fila+(i1 ), columna+(i1 ), codigo,color)
                            break
                    aux = aux.Siguiente
            
            # --> Inferior Izquierda.
            if listaCeldas.BuscarPosicionDiferente(fila+1, columna-1, codigo): 
                aux = self.Inicio
                contFila_inferior_izquierda = 2
                contColu_inferior_izquierda = 2
                while aux != None:
                    if listaCeldas.BuscarPosicionDiferente(fila+contFila_inferior_izquierda, columna-contColu_inferior_izquierda, codigo):
                        contFila_inferior_izquierda += 1
                        contColu_inferior_izquierda += 1
                        aux = self.Inicio  
                        if listaCeldas.BuscarPosicionIdentica(fila+contFila_inferior_izquierda, columna-contColu_inferior_izquierda, codigo):
                            for i2 in range(1,contColu_inferior_izquierda):
                                print("FIla: "+str(fila+(i2 ))+"  ,  Columna: "+str(columna-(i2 )))
                                listaCeldas.BuscarPosicionDiferenteParaPintar(fila+(i2 ), columna-(i2 ), codigo,color)
                            break                           
                    aux = aux.Siguiente
            # --> Superior Derecha
            if listaCeldas.BuscarPosicionDiferente(fila-1, columna+1, codigo): 
                aux = self.Inicio
                contFila_superior_derecha = 2
                contColu_superior_derecha = 2
                while aux != None:  
                    if listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_derecha, columna+contColu_superior_derecha, codigo):
                        contFila_superior_derecha += 1
                        contColu_superior_derecha += 1
                        aux = self.Inicio 
                        if listaCeldas.BuscarPosicionIdentica(fila-contFila_superior_derecha, columna+contColu_superior_derecha, codigo):
                            for i3 in range(1,contColu_superior_derecha):
                                print("FIla: "+str(fila-(i3 ))+"  ,  Columna: "+str(columna+(i3 )))
                                listaCeldas.BuscarPosicionDiferenteParaPintar(fila-(i3 ), columna+(i3 ), codigo,color)
                            break                            
                    aux = aux.Siguiente
            # --> Superior Izquierda
            if listaCeldas.BuscarPosicionDiferente(fila-1, columna-1, codigo): 
                aux = self.Inicio
                contFila_superior_izquierda = 2
                contColu_superior_izquierda = 2
                while aux != None:
                    if listaCeldas.BuscarPosicionDiferente(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, codigo):
                        contFila_superior_izquierda += 1
                        contColu_superior_izquierda += 1
                        aux = self.Inicio
                        if listaCeldas.BuscarPosicionIdentica(fila-contFila_superior_izquierda, columna-contColu_superior_izquierda, codigo):
                            for i4 in range(1,contColu_superior_izquierda):
                                print("FIla: "+str(fila-(i4 ))+"  ,  Columna: "+str(columna-(i4 )))
                                listaCeldas.BuscarPosicionDiferenteParaPintar(fila-(i4 ), columna-(i4 ), codigo,color)
                            break                            
                    aux = aux.Siguiente

            #VALIDACIONES PARA VERTICALES 
            # --> Arriba 
            if listaCeldas.BuscarPosicionDiferente(fila+1, columna, codigo): 
                aux = self.Inicio
                contFila_arriba = 2
                while aux != None:
                    if listaCeldas.BuscarPosicionDiferente(fila+contFila_arriba, columna, codigo):
                        contFila_arriba += 1
                        aux = self.Inicio  
                        if listaCeldas.BuscarPosicionIdentica(fila+contFila_arriba,columna, codigo):
                            for i5 in range(1,contFila_arriba):
                                print("FIla: "+str(fila+(i5 ))+"  ,  Columna: "+str(columna))
                                listaCeldas.BuscarPosicionDiferenteParaPintar(fila+(i5 ), columna, codigo,color)
                            break                            
                    aux = aux.Siguiente
            # --> Abajo
            if listaCeldas.BuscarPosicionDiferente(fila-1, columna, codigo): 
                aux = self.Inicio
                contFila_abajo = 2
                while aux != None: 
                    if listaCeldas.BuscarPosicionDiferente(fila-contFila_abajo, columna, codigo):
                        contFila_abajo += 1
                        aux = self.Inicio
                        if listaCeldas.BuscarPosicionIdentica(fila-contFila_abajo,columna, codigo):
                            for i6 in range(1,contFila_abajo):
                                print("FIla: "+str(fila+(i6 ))+"  ,  Columna: "+str(columna))
                                listaCeldas.BuscarPosicionDiferenteParaPintar(fila+(i6 ), columna, codigo,color)
                            break                             
                    aux = aux.Siguiente
            #VALIDACIONES PARA HORIZONTALES 
            # --> Derecha
            if listaCeldas.BuscarPosicionDiferente(fila, columna+1, codigo): 
                aux = self.Inicio
                contColum_derecha = 2
                while aux != None:
                    if listaCeldas.BuscarPosicionDiferente(fila, columna+contColum_derecha, codigo):
                        contColum_derecha += 1
                        aux = self.Inicio  
                        if listaCeldas.BuscarPosicionIdentica(fila,columna+contColum_derecha,codigo):
                            for i7 in range(1,contColum_derecha):
                                print("FIla: "+str(fila)+"  ,  Columna: "+str(columna+(i7 )))
                                listaCeldas.BuscarPosicionDiferenteParaPintar(fila, columna+(i7 ), codigo,color)
                            break                          
                    aux = aux.Siguiente
            # --> Izquierda
            if listaCeldas.BuscarPosicionDiferente(fila, columna-1, codigo): 
                aux = self.Inicio
                contColum_izquierda = 2
                while aux != None:
                    if listaCeldas.BuscarPosicionDiferente(fila, columna-contColum_izquierda, codigo):
                        contColum_izquierda += 1
                        aux = self.Inicio       
                        if listaCeldas.BuscarPosicionIdentica(fila,columna-contColum_izquierda,codigo):
                            for i8 in range(1,contColum_izquierda):
                                print("FIla: "+str(fila)+"  ,  Columna: "+str(columna-(i8 )))
                                listaCeldas.BuscarPosicionDiferenteParaPintar(fila, columna-(i8 ), codigo,color)
                            break                       
                    aux = aux.Siguiente
        #En caso no este fila y columna en lista de posible comida
            listaCeldas.Insertar(fila, columna, codigo, color)
        else:
            print(Fore.RED+"El organismo muere o no prospera")

        return ListaProspera


    #Sin el intento de validar el tablero 
    def BuscarOrganismoPuedeProsperar(self, muestra, orga, listaCeldas):
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