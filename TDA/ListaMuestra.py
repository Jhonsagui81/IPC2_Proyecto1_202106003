from colorama import Fore
from .Nodo import NodoMuestra

class ListaMuestra:
##sirve para insertar listas de muestras
    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.Limite = 1
    
    def Insertar(self, codigo, descripcion, limite_vertical, limite_horizontal, celdasvivas):
        NuevoNodo = NodoMuestra(self.Limite,codigo, descripcion, limite_vertical, limite_horizontal, celdasvivas)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
            self.Limite += 1
        else:
            self.Limite += 1
            self.Final.AsignarSiguiente(NuevoNodo)
            self.Final = NuevoNodo

    def BuscarMuestra(self, codigo):
        if self.Inicio == None:
            return None
        Retorno = ""
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerCodigo() == codigo:
                Retorno += Fore.LIGHTGREEN_EX+"La muestra es: "+str(Auxiliar.ObtenerCodigo())+" Y se describe por: "+str(Auxiliar.ObtenerDescripcion())+"\n"
                return Retorno
            else:
                Auxiliar = Auxiliar.Siguiente
        return False

    def BuscarId(self, codigo):
        if self.Inicio == None:
            return None
        Auxiliar = self.Inicio
        while Auxiliar != None:
            if Auxiliar.ObtenerCodigo() == codigo:
                id = Auxiliar.ObtenerId()
                return id
            Auxiliar = Auxiliar.Siguiente

    def LimiteVertical(self, codigo):
        if self.Inicio == None:
            return None
        aux = self.Inicio
        while aux != None:
            if aux.ObtenerCodigo() == codigo:
                return aux.ObtenerLimiteVertical()
            aux = aux.Siguiente

    def LimiteHorizontal(self, codigo):
        if self.Inicio == None:
            return None
        aux = self.Inicio
        while aux != None:
            if aux.ObtenerCodigo() == codigo:
                return aux.ObtenerHorizontal()
            aux = aux.Siguiente
