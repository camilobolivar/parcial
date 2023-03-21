class tablaexcel:
    def _init_(self,entrante):
        self.entrante = entrante
        filas = len(entrante)
        columnas = len(entrante[0])
        self.shape = [filas,columnas]

    def _str_(self):
         if self.shape[0]==1:
            respuesta = self._imprimir_tabla_(0)
            return(respuesta)
         else:
            respuesta = ""
            for i in range(self.shape[0]-1):
                respuesta = respuesta + self._imprimir_vector_(i)+"\n"
            respuesta = respuesta + self._imprimir_vector_(self.shape[0]-1)
            return(respuesta)
    def _imprimir_tabla_(self,fila):
         respuesta = "|"
         for i in range(self.shape[1]-1):
            respuesta = respuesta + str(self.valores[fila][i])
            respuesta = respuesta + " "
            
         respuesta = respuesta + str(self.valores[fila][self.shape[1]-1]) + "|"
         return(respuesta)




V1= tablaexcel([[1,2,3, 5, 690, 0],[100,200,300, 500, 600, 0]])
V2= tablaexcel([[10,20,30, 0, 10, 30],[11,21,31, 0, 10, 30]])