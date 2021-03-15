from multiprocessing import Process, Manager
import random

def llenar(matriz, inicio, fin, columnas, val, lock):
    """
    matriz=es una matriz.

    inicio: Es posicion inicial desde la que se va a comenzar a llenar

    fin: es la posicion final hasta la cual se llena.

    columna: hace referencia al tamaño de la matriz.

    la funcion llena la matriz con numeros enteros aleatorios entre
    0 y 1000
    """
    with lock:
        for i in range (inicio, fin):
            col=[]
            for j in range(columnas):
                col.append(val)
                #col.append(random.randint(0, 1000))
            matriz.append(col)


def multi(matriz1, matriz2, resultado, inicio, fin):
    """
    matriz1, matriz2: son las matrices que se reciben
    para hacer el producto.

    resultado: es la matriz resultado.

    inicio: es la posicion inicial desde la cual se empezar a
    realizar el producto.

    fin: es la posicion final hasta la cual esta permito realizar
    el producto.

    """
    for k in range (inicio, fin):
        item1=matriz1[k]
        fil_resul=[]
        for i in range (len(matriz1)):
            b=0
            for j in range (len(matriz2)):
                a=item1[j]*matriz2[j][i]
                b=a+b
            fil_resul.append(b)
        resultado.append(fil_resul)
    return

def imprimir (matriz):
    """
    Recibe una matriz y la imprime por pantalla.
    """
    for item in matriz:
        print(item)

def cubo(lista):
    lista[0].put(lista[1]**lista[2])
    return

if __name__ == "__main__":
    with Manager() as manager:
        matriz=manager.list()
        lock=manager.Lock()

        fil_col=4
        numero_procesos=4

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
        for i in range(numero_procesos):
            p=Process(target=llenar, args=(matriz, lis_inicios[i], lis_fines[i], fil_col, i, lock))
            procesos.append(p)
            p.start()

        for i in procesos:
            i.join()

        imprimir(matriz)
    #for i in l:
    #    p=mp.Process(target=cubo, args=(i,))
    #    pro.append(p)
    #    p.start()
    #
    #for i in pro:
    #    i.join()