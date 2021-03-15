from multiprocessing import Pool
from time import process_time 
import random

def llenar(lista):
    """
    matriz=es una matriz.

    inicio: Es posicion inicial desde la que se va a comenzar a llenar

    fin: es la posicion final hasta la cual se llena.

    columna: hace referencia al tamaño de la matriz.

    la funcion llena la matriz con numeros enteros aleatorios entre
    0 y 1000
    """
    r=list()
    for i in range (lista[0], lista[1]):
        col=[]
        for j in range(lista[2]):
            col.append(lista[3])
            #col.append(random.randint(0, 5))
        r.append(col)
    return r

#matriz1, matriz2, inicio, fin
def multi(lista):
    """
    matriz1, matriz2: son las matrices que se reciben
    para hacer el producto.

    resultado: es la matriz resultado.

    inicio: es la posicion inicial desde la cual se empezar a
    realizar el producto.

    fin: es la posicion final hasta la cual esta permito realizar
    el producto.

    """
    r=list()
    for k in range (lista[2], lista[3]):
        item1=lista[0][k]
        fil_resul=[]
        for i in range (len(lista[0])):
            b=0
            for j in range (len(lista[1])):
                a=item1[j]*lista[1][j][i]
                b=a+b
            fil_resul.append(b)
        r.append(fil_resul)
    return r


def imprimir (matriz):
    """
    Recibe una matriz y la imprime por pantalla.
    """
    for item in matriz:
        print(item)



def cubo(lista):
    lista[0].append(lista[1]**lista[2])
    return lista[0][0]

if __name__ == "__main__":
    matriz1=list()
    matriz2=list()
    l=[[0,2,4,2],
        [2,4,4,3]]
    a=Pool().map(llenar,l)

    for i in a:
        matriz1+=i

    k=[[0,2,4,4],
        [0,2,4,5]]
    b=Pool().map(llenar,k)

    for i in b:
        matriz2+=i
    
    
    imprimir(matriz1)
    print("-----------")
    imprimir(matriz2)

    inicio=[0, 2]
    fin=[2, 4]
    print(Pool().map(multi, [[matriz1, matriz2, inicio, fin ]]))
    #matriz1, matriz2, inicio, fin

    #r=list()
    #lista1=[r,2,3]
    #lista2=[r,3,4]
    #lista3=[r, 5, 2]
    #print(Pool().map(cubo,[lista1, lista2, lista3]))