class tablaexcel:
    def __init__(self, entrante):
        self.entrante = entrante
       
        filas = len(entrante)
        columnas = len(entrante[0])
        self.shape = [filas, columnas]
        self.features = entrante[0]
        self.data = entrante [1:]

#metodo para imprimir las listas de listas alineadas

    def __str__(self):
        if self.shape[0]==1:
            respuesta = self._imprimir_tabla_(0)
            return(respuesta)
        else:
            respuesta = ""
            for i in range(self.shape[0]-1):
                respuesta = respuesta + self._imprimir_tabla_(i)+"\n"
            respuesta = respuesta + self._imprimir_tabla_(self.shape[0]-1)
            return(respuesta)
    
    def _imprimir_tabla_(self,fila):
        respuesta = "| "
        for i in range(self.shape[1]):
            respuesta = respuesta +  "{:<10}".format(str((self.entrante[fila][i]))) 
            respuesta = respuesta + "| "
        return(respuesta)
    

V1 = tablaexcel([["gabriela","ximena","camilo", "andres", "maria", "juan",], [100,"150",300, 500, 600, 1], [100.8,200,600, 500, 600, 2], [100,150,300, 500, 600, "5"], [100.8,200,600, 500, 600, "5"]])

print(V1)

print(V1.features)
