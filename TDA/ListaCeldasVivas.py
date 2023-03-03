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
    
    def BuscarOrganismo(self, muestra, orga, listaCeldas):
        Auxiliar = self.Inicio
        Retorno = "\n"
        while Auxiliar != None:
            if Auxiliar.ObtenerOrganismoVivo() == orga:
                #datos de ficha a estudiar
                
                fila = Auxiliar.ObtenerFila()
                columna = Auxiliar.ObtenerColumna()
                color = Auxiliar.ObtenerColor()
                # Retorno +="Fila: "+str(fila)+"    columna: "+str(columna)+"\n ES COLOR:"+str(color)+"\n" 
                    # Para verificar si tiene en la esquina Comer1: Fila+1, columna+1
                if listaCeldas.BuscarPosicion(fila+1, columna+1, color):
                    print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+1)+" Columna: "+str(columna+1))
                    # Retorno += "\nFila: "+str(Auxiliar.ObtenerFila())+",  Columna: "+str(Auxiliar.ObtenerColumna())+"\n   PUEDECOMER inferior derecha"
                    #comer 2: Fila+1  columna-1
                if listaCeldas.BuscarPosicion(fila+1, columna-1, color):
                    print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila+1)+" Columna: "+str(columna-1))
                    # Retorno += "\nFila: "+str(Auxiliar.ObtenerFila())+",  Columna: "+str(Auxiliar.ObtenerColumna())+"\n   PUEDECOMER inferior izquierda"
                    #comer 3: Fila -1   columna+1
                if listaCeldas.BuscarPosicion(fila-1, columna+1, color):
                    print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-1)+" Columna: "+str(columna+1))
                    # Retorno += "\nFila: "+str(Auxiliar.ObtenerFila())+",  Columna: "+str(Auxiliar.ObtenerColumna())+"\n   PUEDECOMER superior derecha"
                    #comer 4: fila -1   columna-1
                if listaCeldas.BuscarPosicion(fila-1, columna-1, color):
                    print("Auxiliar en:\nFila: "+str(Auxiliar.ObtenerFila())+ " Columna: " + str(Auxiliar.ObtenerColumna())+"\nPuede Comer Ficha en Fila: "+str(fila-1)+" Columna: "+str(columna-1))
                    # Retorno += "\nFila: "+str(Auxiliar.ObtenerFila())+",  Columna: "+str(Auxiliar.ObtenerColumna())+"\n   PUEDECOMER superior izquierda"
            Auxiliar = Auxiliar.Siguiente
        return Retorno
        #debe retornar algo si o si 

    def BuscarPosicion(self, fila, columna, color):
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerColor() != color:   
                if (Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna):
                    return True
            Auxiliar = Auxiliar.Siguiente
        return False
