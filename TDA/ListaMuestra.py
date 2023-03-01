from .Nodo import NodoMuestra

class ListaMuestra:
##sirve para insertar listas de muestras
    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Limite = 1
    
    def Insertar(self, codigo, descripcion, limite_vertical, limite_horizontal, celdasvivas):
        NuevoNodo = NodoMuestra(codigo, descripcion, limite_vertical, limite_horizontal, celdasvivas)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.Limite += 1
        else:
            self.Limite += 1
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo
    
    def Imprimir(self):
        Aux = self.Inicio
        Aux.Obtener()
        print("Este es metodo de Lista muestra ")