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


def sel(a, b, c, inicio, fin):
    for k in range (inicio, fin):
        item1=a[k]
        fil_resul=[]
        for i in range (len(a)):
            sum=mul(item1, b, i)
            fil_resul.append(sum)
        c.append(fil_resul)
    return

def m(l):
    sum=0
    for i in range (len(l[0])):
        sum+=l[0][i]*l[1][i]
    return sum

def m1(a, b, r):
    sum=0
    for i in range (len(a)):
        sum+=a[i]*b[i]
    r.append(sum)


def recorrer1(a, b, l):
    for item1 in a:
        print(item1)
        pro=list()
        with Manager() as manager:
            r=manager.list()
            for item2 in b:
                p=Process(target=m1, args=(item1, item2, r,))
                pro.append(p)
                p.start()
            
            for p in pro:
                p.join()
            
            l.append(list(r))

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
            
# [0, 0, 0] | [0, 1, 2]
# [1, 1, 1] | [0, 1, 2]
# [2, 2, 2] | [0, 1, 2]


#------------------
if __name__ == "__main__":
    n=1000
    l=[]
    a=[]
    b=[]
    t=[]
    llenar(a,n)
    llenar(b,n)

    transpuesta(b, t, n)

    iterable=list()
    for i in range (n):
        iterable.append([a[i], t])
    print("---")
    ti=process_time()
    m=Pool().map(mul, iterable)
    tf=process_time()

    print(tf-ti)


    

    #ti=process_time()
    #recorrer1(a, t, l)
    #tf=process_time()

    #ti=process_time()
    #recorrer(a, t, l)
    #tf=process_time()
    #print(tf-ti)
    #print(Pool().map(m, [[l1,l2]]))



    
