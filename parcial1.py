import numpy as np
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
# citar las columnas que piden
    def __llamar_columnas__(self,columna1, columna2):
        respuesta = ""
        for i in range (self.shape[0]):
            respuesta = respuesta + "| " + \
                "{:<10}".format(str(self.entrante[i][columna1])) + "| " \
                + "{:<10}".format(str(self.entrante[i][columna2])) + " |" + "\n" 
        return(respuesta)
 #identificar datos 
    def __identificardatos__(self):
        respuesta =[]
        for j in range(len(self.entrante[0])):
            primer_dato = type(self.entrante[1][j])
            for i in range(1,self.shape[0]):
                if type(self.entrante [i][j]) != primer_dato:
                    respuesta.append("variado")
                    break
            else: 
                if primer_dato == str:
                    respuesta.append("letras")
                else:
                    respuesta.append("numeros")
        return respuesta  

V1 = tablaexcel([["gabriela","ximena","camilo", "andres", "maria", "juan"],\
                  [1,"dos",3453, 567, 4, 1],\
                  [100,200,600, 500, 7, 2],\
                    [148,150,786, 37, 63, "tres"],\
                    [100,24,36, 500, 89, "cuatro"]])

print("\n tabla tipo excel \n")

print(V1)

print("\n imprimir primera fila \n")

print(V1.features)

print("\n identificar que datos tiene la columna \n")

print (V1.__identificardatos__())

print("\n imprimir dos columnas \n")

columna_1 = int(input("primer columna a llamar: "))
columna_2 = int(input("segunda columna a llamar: "))
print("\n su tabla quedara asi: \n")
print(V1.__llamar_columnas__(columna_1,columna_2))

