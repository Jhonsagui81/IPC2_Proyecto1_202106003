from .Nodo import NodoDibujo

class ListaDibujo:
    def __init__(self, limite_vertical, limite_horizontal):
        self.limiteVertical = limite_vertical
        self.limiteHorizontal = limite_horizontal
        self.Inicio = None
        self.Final = None
    
    def Insertar(self, fila, columna, color, borde):
        NuevoNodo = NodoDibujo(fila, columna, color, borde)
        if self.Inicio == None:
            self.Inicio = NuevoNodo
            self.Final = NuevoNodo
        else:
            Auxiliar = self.Inicio
            while Auxiliar != None:
                if Auxiliar.ObtenerFila() == fila and Auxiliar.ObtenerColumna() == columna:
                    #Si entramos, quiere decir que existe la posicion almacenada 
                    if color != 'White':
                        #Solo quiero si el tiene color 
                        Auxiliar.setColor(color)
                    if Auxiliar.ObtenerBorde() == 'Black':
                        #solo si el borde es negro -> cambia.  si es verde se queda igual
                        Auxiliar.setBorde(borde)
                    return 
                Auxiliar = Auxiliar.Siguiente
            #Si se llega aqui es porque no existe otra en la misma posicion 
            self.Final.Siguiente = NuevoNodo ##ojo
            self.Final = NuevoNodo

    def GenerarDibujo(self):
        texto = "digraph {\n"
        texto += "\ttb1 [\n"
        texto += "\t\tshape=plaintext\n"
        texto += "\t\tlabel=<\n"
        texto += "\t\t\t<table border='0' cellborder='1' color='blue' cellspacing='0'>\n"
        ContFilaVacia = 0
        #Recorriendo Filas
        for i in range(self.limiteVertical):
            ListaFila = self.ObtenerTodaFila(i)
            if ListaFila.Inicio != None:
                if ContFilaVacia > 0:
                    texto += "\t\t\t\t<tr>\n"
                    texto += "\t\t\t\t\t<td colspan='"+str(self.limiteHorizontal)+"'>...</td>\n"
                    texto += "\t\t\t\t</tr>\n"
                ContFilaVacia = 0
                texto += "\t\t\t\t<tr>\n"
                ContColumnaVacia = 0
                #Recorriendo columnas
                for j in range(self.limiteHorizontal):
                    auxiliar = ListaFila.ObtenerEnColumna(j)
                    if auxiliar != None:
                        if ContColumnaVacia > 0:
                            texto += "\t\t\t\t\t<td colspan='"+str(ContColumnaVacia)+"' bgcolor='pr1'><font color='Black'>\n"
                            texto += "\t\t\t\t\t\t<table color='White'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        ContColumnaVacia = 0
                        if auxiliar.ObtenerColor() == 'Red':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='"+str(auxiliar.ObtenerColor())+"'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        elif auxiliar.ObtenerColor() == 'Navy':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='"+str(auxiliar.ObtenerColor())+"'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                    else:
                        ContColumnaVacia += 1
                    if j+1 == self.limiteHorizontal:
                        if ContColumnaVacia > 0:
                            texto += "\t\t\t\t\t<td colspan='"+str(ContColumnaVacia)+"' bgcolor='pr2'><font color='Black'>\n"
                            texto += "\t\t\t\t\t\t<table color='White'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                texto += "\t\t\t\t</tr>\n"
            else:
                ContFilaVacia += 1
                if i+1 == self.limiteVertical:
                    if ContFilaVacia > 0:
                        texto += "\t\t\t\t<tr>\n"
                        texto += "\t\t\t\t\t<td colspan='"+str(self.limiteHorizontal)+"'>...</td>\n"
                        texto += "\t\t\t\t</tr>\n"
        texto += "\t\t\t</table>\n"
        texto += "\t\t>];\n"
        texto += "}\n"

        Destino = open('/home/jhonatan/Documentos/Universidad_USAC/Semestre5/02_IPC2/clone/App/Documentacion/Dibujo.dot', 'w')
        Destino.write(texto)
        Destino.close()
                

    def ObtenerTodaFila(self, Fila):
        ListaFila = ListaDibujo(self.limiteVertical, self.limiteHorizontal)
        aux = self.Inicio
        while aux != None:
            if aux.ObtenerFila() == Fila:
                ListaFila.Insertar(aux.ObtenerFila(), aux.ObtenerColumna(), aux.ObtenerColor(), aux.ObtenerBorde())
            aux = aux.Siguiente
        return ListaFila

    def ObtenerEnColumna(self, Columna):
        Aux = self.Inicio
        while Aux != None:
            if Aux.ObtenerColumna() == Columna:
                return Aux
            Aux = Aux.Siguiente
        return None
