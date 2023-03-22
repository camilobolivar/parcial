class tablaexcel:
    def __init__(self, entrante):
        self.entrante = entrante
       
        filas = len(entrante)
        columnas = len(entrante[0])
        self.shape = [filas, columnas]
        self.features = entrante[0]
        self.data = entrante [1:]

    


    def __identificardatos__(self):
        if (type(self.data[0][0]) ==  type(1)) or (type(self.data[0][0]) ==  type(1.2)):
            respuesta = "numero"
            return(respuesta)
        else:
            respuesta = "letra"
            return(respuesta)
        

    def __columnas__(self):
        respuesta = "|" + str(self.entrante [0][2]) + "|" + str(self.entrante [0][4]) + "|" + "\n" + "|" + str(self.entrante [1][2]) + "|" + str(self.entrante [1][4]) + "|" + "\n" + "|" + str(self.entrante [2][2]) + "|" + str(self.entrante [2][4]) + "|" 
        return(respuesta)



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
        respuesta = "|"
        for i in range(self.shape[1]-1):
            respuesta = respuesta + str(self.entrante[fila][i])
        
            respuesta = respuesta + "|"
        respuesta = respuesta + str(self.entrante[fila][self.shape[1]-1]) + "|"
        return(respuesta)

   

V1= tablaexcel([[1,2,3, 5, 690, 0],["100.8","ers",300, 500, 600, 0],[100.8,"ana",600, 500, 600, 0]])
V2= tablaexcel([[10,20,30, 0, 10, 30],[11,21,31, 0, 10, 30]])
#print(V1)
#print(V1.__identificardatos__())
print(V1.__columnas__())