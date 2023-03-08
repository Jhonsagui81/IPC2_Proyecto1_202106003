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
                    texto += "\t\t\t\t\t<td>...</td>\n"
                    texto += "\t\t\t\t</tr>\n"
                ContFilaVacia = 0
                texto += "\t\t\t\t<tr>\n"
                ContColumnaVacia = 0
                #Recorriendo columnas
                for j in range(self.limiteHorizontal):
                    auxiliar = ListaFila.ObtenerEnColumna(j)
                    if auxiliar != None:
                        if ContColumnaVacia > 0:
                            texto += "\t\t\t\t\t<td bgcolor='White'><font color='Black'>\n"
                            texto += "\t\t\t\t\t\t<table color='White'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        ContColumnaVacia = 0
                        if auxiliar.ObtenerColor() == '#d68910':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='"+str(auxiliar.ObtenerColor())+"'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == '#1e8449':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='"+str(auxiliar.ObtenerColor())+"'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == '#1f618d':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='"+str(auxiliar.ObtenerColor())+"'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == '#943126':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='"+str(auxiliar.ObtenerColor())+"'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == '#17202a': ##puede comer
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='Green'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == '#c39bd3':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='Green'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == '#cd6155':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='Green'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == '#3498db':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='Green'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == '#229954':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='Green'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                        if auxiliar.ObtenerColor() == 'White':
                            texto += "\t\t\t\t\t<td bgcolor='"+str(auxiliar.ObtenerColor())+"'><font color='lightblue'>\n"
                            texto += "\t\t\t\t\t\t<table color='White'>\n"
                            texto += "\t\t\t\t\t\t\t<tr>\n"
                            texto += "\t\t\t\t\t\t\t\t<td>"+str(auxiliar.ObtenerFila())+","+str(auxiliar.ObtenerColumna())+"</td>\n"
                            texto += "\t\t\t\t\t\t\t</tr>\n"
                            texto += "\t\t\t\t\t\t</table>\n"
                            texto += "\t\t\t\t\t</font></td>\n"
                    else:
                        ContColumnaVacia += 1
                    if j+1 == self.limiteHorizontal:
                        if ContColumnaVacia > 0:
                            texto += "\t\t\t\t\t<td bgcolor='White'><font color='Black'>\n"
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
                        texto += "\t\t\t\t\t<td>...</td>\n"
                        texto += "\t\t\t\t</tr>\n"
        texto += "\t\t\t</table>\n"
        texto += "\t\t>];\n"
        texto += "}\n"

        Destino = open('./Documentacion/Dibujo.dot', 'w')
        Destino.write(texto)
        Destino.close()
                
    def EScribirDibujo(self):
        Texto = "digraph {\n"
        Texto = Texto + "\ttbl [\n"
        Texto = Texto + "\t\tshape=plaintext\n"
        Texto = Texto + "\t\tlabel=<\n"
        Texto = Texto + "\t\t\t<table border='0' cellborder='1' color='blue' cellspacing='0'>\n"
        ContFilaVacia = 0
        for i in range(self.limiteVertical):
            ListaFila = self.ObtenerTodaFila(i)
            if ListaFila.Inicio != None:
                if ContFilaVacia > 0:
                    Texto = Texto + "\t\t\t\t<tr>\n"
                    Texto = Texto + "\t\t\t\t\t<td colspan='"+str(self.limiteHorizontal)+"'>...</td>\n"
                    Texto = Texto + "\t\t\t\t</tr>\n"
                ContFilaVacia = 0
                Texto = Texto + "\t\t\t\t<tr>\n"
                ContColumnaVacia = 0
                for j in range(self.limiteHorizontal):
                    Auxilar = ListaFila.ObtenerEnColumna(j)
                    if Auxilar != None:
                        if ContColumnaVacia > 0:
                            Texto = Texto + "\t\t\t\t\t<td colspan='"+str(ContColumnaVacia)+"' bgcolor='White'><font color='Black'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='White'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                        ContColumnaVacia = 0
                        if Auxilar.ObtenerBorde() == 'Green':
                            Texto = Texto + "\t\t\t\t\t<td bgcolor='"+str(Auxilar.ObtenerColor())+"'><font color='lightblue'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='Green'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>"+str(Auxilar.ObtenerFila())+","+str(Auxilar.ObtenerColumna())+"</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                        else:
                            Texto = Texto + "\t\t\t\t\t<td bgcolor='"+str(Auxilar.ObtenerColor())+"'><font color='lightblue'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='"+str(Auxilar.ObtenerColor())+"'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>"+str(Auxilar.ObtenerFila())+","+str(Auxilar.ObtenerColumna())+"</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                    else:
                        ContColumnaVacia = ContColumnaVacia + 1
                    if j+1 == self.limiteHorizontal:
                        if ContColumnaVacia > 0:
                            Texto = Texto + "\t\t\t\t\t<td colspan='"+str(ContColumnaVacia)+"' bgcolor='White'><font color='Black'>\n"
                            Texto = Texto + "\t\t\t\t\t\t<table color='White'>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t<tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t\t<td>...</td>\n"
                            Texto = Texto + "\t\t\t\t\t\t\t</tr>\n"
                            Texto = Texto + "\t\t\t\t\t\t</table>\n"
                            Texto = Texto + "\t\t\t\t\t</font></td>\n"
                Texto = Texto + "\t\t\t\t</tr>\n"
            else:
                ContFilaVacia = ContFilaVacia + 1
                if i + 1 == self.limiteVertical:
                    if ContFilaVacia > 0:
                        Texto = Texto + "\t\t\t\t<tr>\n"
                        Texto = Texto + "\t\t\t\t\t<td colspan='"+str(self.limiteHorizontal)+"'>...</td>\n"
                        Texto = Texto + "\t\t\t\t</tr>\n"
        Texto = Texto + "\t\t\t</table>\n"
        Texto = Texto + "\t\t>];\n"
        Texto = Texto + "}\n"
        Destino = open('/home/jhonatan/Documentos/Universidad_USAC/Semestre5/02_IPC2/clone/App/Documentacion/Dibujo.dot', 'w')
        Destino.write(Texto)
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

    def Impimir(self):
        Retorno = "La lista tiene: [ Fila: "
        if self.Inicio == None:
            return "La lista está vacía."
        Auxiliar = self.Inicio
        while Auxiliar != None:
            Retorno += "[ Fila:"+str(Auxiliar.ObtenerFila()) +", Columana: "+str(Auxiliar.ObtenerColumna())+", COlor: "+str(Auxiliar.ObtenerColor
                                                                                                                            )+"\n"
            if Auxiliar.Siguiente != None:
                Retorno += ", "
            Auxiliar = Auxiliar.Siguiente
        Retorno += "]"
        return Retorno
