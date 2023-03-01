from .Nodo import NodoOrganismo
from .ListaCeldasVivas import ListaCeldas
class ListaOrganismos:
    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.limite = 1

    def Insertar(self, codigo, nombre):
        if self.limite == 1:
            color = "Red"
        if self.limite == 2:
            color = "Black"
        if self.limite == 3:
            color = "Green"
        if self.limite == 4:
            color = "teal"
        if self.limite == 5:
            color = "Purple"                            
        if self.limite == 6:
            self.color = "gray"
        if self.limite == 7:
            self.color = "yellow"   
        if self.limite == 8:
            self.color = "Orange"                             

        NuevoNodo = NodoOrganismo(codigo, nombre, color)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.limite += 1
        else:
            self.limite += 1
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo        
    
    def ValidaCeldaViva(self, codigo_organismo):
        aux = self.Inicio
        while aux != None:
            if codigo_organismo == aux.ObtenerCodigo():
                return aux.ObtenerColor()  
            aux = aux.Siguiente        
