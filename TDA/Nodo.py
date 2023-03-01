from .Dato import *

class NodoCeldas:

    def __init__(self, fila, columna, codigo_organismo,color):
        self.CeldaViva = DatoCelda(fila, columna, codigo_organismo,color)
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo
    
    def ObtenerFila(self):
        return self.CeldaViva.fila
    
    def ObtenerColumna(self):
        return self.CeldaViva.columna
    
    def ObtenerOrganismoVivo(self):
        return self.CeldaViva.codigo_organismo
    
    def ObtenerColor(self):
        return self.CeldaViva.color
    

class NodoMuestra: 

    def __init__(self, codigo, descripcion, limite_vertical, limite_horizontal, celdasvivas):
        self.Muestra = DatoMuestra(codigo, descripcion, limite_vertical, limite_horizontal, celdasvivas)
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def Obtener(self):
        self.Muestra.celda_viva.Imprimir()

class NodoOrganismo:

    def __init__(self, codigo, nombre, color):
        self.Organismo = Organismo(codigo, nombre, color)
        self.Siguiente = None

    def ObtenerSiguiente(self):
        return self.Siguiente
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerCodigo(self):
        return self.Organismo.codigo
    
    def ObtenerNombre(self):
        return self.Organismo.nombre
    
    def ObtenerColor(self):
        return self.Organismo.color