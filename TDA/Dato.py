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

class Organismo:
    def __init__(self, codigo, nombre, color):
        self.codigo = codigo
        self.nombre = nombre
        self.color = color