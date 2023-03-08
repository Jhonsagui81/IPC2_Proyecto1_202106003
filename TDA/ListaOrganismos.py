from .Nodo import NodoOrganismo
from .ListaCeldasVivas import ListaCeldas
class ListaOrganismos:
    def __init__(self):
        self.Inicio = None
        self.Final = None
        self.limite = 1

    def Insertar(self, codigo, nombre):
        if self.limite == 1:
            color = '#d68910'
        if self.limite == 2:
            color = '#1e8449'
        if self.limite == 3:
            color = '#1f618d'
        if self.limite == 4:
            color = '#943126'
        if self.limite == 5:
            color = '#c39bd3'                            
        if self.limite == 6:
            self.color = '#cd6155'
        if self.limite == 7:
            self.color = '#3498db'   
        if self.limite == 8:
            self.color = '#229954'                             

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
                color = aux.ObtenerColor()
                return color  
            aux = aux.Siguiente        

    def ObtenerNodos(self):
        return self.limite

    def ImprimirOrganismos(self):
        Auxiliar = self.Inicio
        Retorno = ""
        while Auxiliar != None:
            Retorno += "--> Organismo: "+str(Auxiliar.ObtenerNombre())+"   Codigo : "+str(Auxiliar.ObtenerCodigo())+"\n"
            Auxiliar = Auxiliar.Siguiente
        return Retorno
