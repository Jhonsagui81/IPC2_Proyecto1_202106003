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
        return self.CeldaViva.ObtenerFila()
    
    def ObtenerColumna(self):
        return self.CeldaViva.ObtenerColumna()
    
    def ObtenerOrganismoVivo(self):
        return self.CeldaViva.ObtenerCodigo()
    
    def ObtenerColor(self):
        return self.CeldaViva.ObtenerColor()
    
    def setFila(self, fila):
        self.CeldaViva.SetFila(fila)
    
    def setColumna(self, columna):
        self.CeldaViva.setColumna(columna)
    
    def setCodigo(self, codigo):
        self.CeldaViva.setCodigo(codigo)
        
    def setColor(self, color):
        self.CeldaViva.setColor(color)

class NodoMuestra: 

    def __init__(self, id, codigo, descripcion, limite_vertical, limite_horizontal, celdasvivas):
        self.Muestra = DatoMuestra(id, codigo, descripcion, limite_vertical, limite_horizontal, celdasvivas)
        self.Siguiente = None
    
    def ObtenerId(self):
        return self.Muestra.id
    
    def ObtenerSiguiente(self):
        return self.Siguiente
    
    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerCodigo(self):
        return self.Muestra.codigo
    
    def ObtenerDescripcion(self):
        return self.Muestra.descripcion
    
    def ObtenerLimiteVertical(self):
        return self.Muestra.limite_vert
    
    def ObtenerHorizontal(self):
        return self.Muestra.limite_hori
    
    def ObtenerCeldaViva(self):
        return self.Muestra.celda_viva

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

class NodoDibujo:
    def __init__(self, fila, columna, color, borde):
        self.dibujo = DibujoCelda(fila, columna, color, borde)
        self.Siguiente = None

    def AsignarSiguiente(self, Nodo):
        self.Siguiente = Nodo

    def ObtenerFila(self):
        return self.dibujo.ObtenerFila()
    
    def ObtenerColumna(self):
        return self.dibujo.ObtenerColumna()
    
    def ObtenerColor(self):
        return self.dibujo.ObtenerColor()
    
    def ObtenerBorde(self):
        return self.dibujo.ObtenerBorde()
    
    def setFila(self, fila):
        self.dibujo.setFila(fila)
    
    def setColumna(self, columna):
        self.dibujo.setColumna(columna)
    
    def setColor(self, color):
        self.dibujo.setColor(color)

    def setBorde(self, borde):
        self.dibujo.setBorde(borde)