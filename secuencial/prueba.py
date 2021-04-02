import random
from time import process_time 
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
            #col.append(i)
            col.append(random.randint(0, 9))
        matriz.append(col)
    return

def transpuesta(a, t, fil_col):
    for j in range (fil_col):
        fila=[]
        for i in range (fil_col):
            fila.append(a[i][j])
        t.append(fila)

def ver (lista):
    for i in lista:
        print(i)


def mul(matriz1, m_transpuesta, result, n):
    for i in range(n):
        aux=list()
        for j in range(n):
            suma = 0
            for c in range(n):
                suma+=matriz1[i][c]*m_transpuesta[j][c]
            aux.append(suma)
        result.append(aux)


    
             
    

if __name__ == '__main__':
    n=500

    #definicion de las matrices
    matriz1=[]
    matriz2=[]
    m_transpuesta=[]
    result=[]

    #llenado de las matrices.
    llenar(matriz1, n)
    llenar(matriz2, n)

    #transpuesta
    transpuesta(matriz2, m_transpuesta, n)

    #multiplicacion
    inicio=process_time()
    mul(matriz1, m_transpuesta, result, n)
    fin=process_time()

    print(fin-inicio)