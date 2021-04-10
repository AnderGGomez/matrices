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
            #col.append(random.randint(0, 9))
        matriz.append(col)
    return


def imprimir(lista):
	for i in lista:
		print(i)

def mul1(lista, matr, n):
    for k in range(len(lista)):
        aux=list()
        for i in range(n):
            suma=0
            for j in range(n):
                suma+=lista[k][0][j]*lista[k][1][j][i]
            aux.append(suma)
        matr.append(aux)
    return


            

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
            with Manager() as manager:

                numero_procesos=8
                #Definicion de las listas (matrices)
                l=manager.list()
                a=[]
                b=[]

                #Se llenan las matrices.
                llenar(a,fil_col)
                llenar(b,fil_col)


                # Se formatean los datos en un interable para la distribucion entre procesos.
                
                iterable=list()
                for i in range (fil_col):
                    iterable.append([a[i], b])

                
                tam_tramo=fil_col//numero_procesos
                lis_inicios=list()
                lis_fines=list()
                inicio=0
                fin=tam_tramo
                aux=fil_col
                for i in range(numero_procesos):
                    aux=aux-tam_tramo
                    lis_inicios.append(inicio)
                    lis_fines.append(fin)
                    try:
                        tam_tramo=aux//(numero_procesos-(i+1))
                    except:
                        tam_tramo=0
                    inicio=fin
                    fin=fin+tam_tramo

                procesos=list()

                ti=process_time()
                for i in range (len(lis_inicios)):
                    p=Process(target=mul1, args=(iterable[lis_inicios[i]:lis_fines[i]], l, fil_col))
                    procesos.append(p)
                    p.start()
                    #print(iterable[lis_inicios[i]:lis_fines[i]])
                
                for p in procesos:
                    p.join()

                tf=process_time()

                tiempos.append(tf-ti)

        
        print("Circuito {} Completado".format(circuito)) 

        #Terminado cada circuito se guardan los resultados
        # en un archivo csv.   
        with open("process_sin.csv","a") as file:
            file.write(str(tiempos)+"\n")



    
