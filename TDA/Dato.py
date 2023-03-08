class DatoMuestra:

    def __init__(self, id, codigo, descripcion, limite_vertical, limite_horizontal, celda_viva):
        self.id = id
        self.codigo = codigo
        self.descripcion = descripcion
        self.limite_vert = limite_vertical
        self.limite_hori = limite_horizontal
        self.celda_viva = celda_viva

class DatoCelda:
    def __init__(self, fila, columna, codigo_organismo,color):
        self.fila = fila
        self.columna = columna
        self.codigo_organismo = codigo_organismo
        self.color = color
    #get
    def ObtenerFila(self):
        return self.fila
    def ObtenerColumna(self):
        return self.columna
    def ObtenerCodigo(self):
        return self.codigo_organismo
    def ObtenerColor(self):
        return self.color
    #set
    def SetFila(self, fila):
        self.fila = fila
    def setColumna(self, columna):
        self.columna = columna
    def setCodigo(self, codigo):
        self.codigo_organismo = codigo
    def setColor(self, color):
        self.color = color

class Organismo:
    def __init__(self, codigo, nombre, color):
        self.codigo = codigo
        self.nombre = nombre
        self.color = color

class DibujoCelda:
    def __init__(self, Fila, Columna, Color, Borde):
        self.Columna = Columna
        self.Fila = Fila
        self.Color = Color
        self.Borde = Borde

    def ObtenerFila(self):
        return self.Fila
    
    def ObtenerColumna(self):
        return self.Columna
    
    def ObtenerColor(self):
        return self.Color
    
    def ObtenerBorde(self):
        return self.Borde
    
    def setFila(self, fila):
        self.Fila = fila
    
    def setColumna(self, columna):
        self.Columna = columna
    
    def setColor(self, color):
        self.Color = color

    def setBorde(self, borde):
        self.Borde = borde