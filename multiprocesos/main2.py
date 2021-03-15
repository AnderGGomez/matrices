from multiprocessing import Pool, Process, Manager
from time import process_time
import os
import random


def llenar(matriz, fil_Col):
    """
    matriz=es una matriz.
    inicio: Es posicion inicial desde la que se va a comenzar a llenar
    fin: es la posicion final hasta la cual se llena.
    columna: hace referencia al tamaño de la matriz.
    la funcion llena la matriz con numeros enteros aleatorios entre
    0 y 1000
    """
    for i in range (fil_Col):
        col=[]
        for j in range(fil_Col):
            col.append(i)
            #col.append(random.randint(0, 5))
        matriz.append(col)
    return

def transpuesta(a, t, fil_col):
    for j in range (fil_col):
        fila=[]
        for i in range (fil_col):
            fila.append(a[i][j])
        t.append(fila)



def imprimir(lista):
	for i in lista:
		print(i)
	
def mul(l):
    lista=list()
    for i in l[1]:
        suma=0
        for j in range(len(i)):
            suma+=l[0][j]*i[j]
        lista.append(suma)
    return lista
            

#------------------
if __name__ == "__main__":

    #Se define el tamaño del circuito.
    tam_circuito=10

    #Se define el conjunto de datos.
    pruebas=[100, 200, 400, 800, 1200, 1400, 1600, 1800, 2000, 2200]

    for circuito in range (tam_circuito):

        #Se crea un lista que almacenara los tiempos de cpu de cada
        #elemento en el conjunto de datos.
        tiempos=list()

        #Una vez elegido un tamaño de la se procede a crearlas.
        for fil_col in pruebas:

            #Definicion de las listas (matrices)
            l=[]
            a=[]
            b=[]
            t=[]

            #Se llenan las matrices.
            llenar(a,fil_col)
            llenar(b,fil_col)

            
            transpuesta(b, t, fil_col)


            # Se formatean los datos en un interable para la distribucion entre procesos.
            
            iterable=list()
            for i in range (fil_col):
                iterable.append([a[i], t])


            #Se llama a la funcion multiplicar de manera concurrente con los valores datos en el iterable.
            ti=process_time()
            m=Pool().map(mul, iterable)
            tf=process_time()

            tiempos.append(tf-ti)

        
        print("Circuito {} Completado".format(circuito)) 

        #Terminado cada circuito se guardan los resultados
        # en un archivo csv.   
        with open("tiempos_procesos.csv","a") as file:
            file.write(str(tiempos)+"\n")



    
