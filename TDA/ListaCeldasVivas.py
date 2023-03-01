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
    
    def Imprimir(self):
        aux = self.Inicio
        print("Este metodo es de la lista de celdas vivas")
        print("La primera celda viva esta en la fila: "+str(aux.ObtenerFila())+"   y en la columna: "+str(aux.ObtenerColumna()))
        print("Y el organismo es de tipo: "+str(aux.ObtenerOrganismoVivo()))
        print("Y este organismo se le asigno el color: "+str(aux.ObtenerColor()))
        print("La cantidad de nodos es: "+str(self.Limite))