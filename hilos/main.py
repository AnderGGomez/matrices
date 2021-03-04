import threading
from time import process_time 
import random



def llenar(matriz, inicio, fin, columnas):
    """
    matriz=es una matriz.

    inicio: Es posicion inicial desde la que se va a comenzar a llenar

    fin: es la posicion final hasta la cual se llena.

    columna: hace referencia al tamaño de la matriz.

    la funcion llena la matriz con numeros enteros aleatorios entre
    0 y 1000
    """
    for i in range (inicio, fin):
        col=[]
        for j in range(columnas):
            col.append(random.randint(0, 1000))
        matriz.append(col)
    return


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

            #Se establece el numero de hilos a utilizar.
            numero_hilos=4

            #Definicion de las listas (matrices)
            matriz1=[]
            matriz2=[]
            resultado=[]

            """
            Se calcula el tamaño del segmento para cada hilo.
            
            Ejemplo si la matrices es 10x10 la division de la carga
            para estos 4 hilos es de.
              fil_col     hilos   asignacion
                10    //    4   :  2
                8     //    3   :  2
                6     //    2   :  3
                3     //    1   :  3

            Esto quiere decir que, con una matriz de 10x10 al primer
                le corresponden 2 filas
                al segundo hilo 2 filas
                al tercer hilo 3 filas
                al cuarto hilo 3 filas

            Los limites se almacenan en las lista de inicios y fines.

            """
            tam_tramo=fil_col//numero_hilos
            lis_inicios=list()
            lis_fines=list()
            inicio=0
            fin=tam_tramo
            aux=fil_col
            for i in range(numero_hilos):
                aux=aux-tam_tramo
                lis_inicios.append(inicio)
                lis_fines.append(fin)
                try:
                    tam_tramo=aux//(numero_hilos-(i+1))
                except:
                    tam_tramo=0
                inicio=fin
                fin=fin+tam_tramo

        # Se crean los hilos y se inicia el llenado de la matriz 1.
        # Cada hilo creando es agregado a una lista.
            hilos=list()
            for i in range(numero_hilos):
                t= threading.Thread(target=llenar, args=(matriz1, lis_inicios[i], lis_fines[i], fil_col))
                hilos.append(t)
                t.start()

            # Por medio de la lista de hilos
            # pedimos que se sincronicen los procesos.
            for i in hilos:
                i.join()

            # Se limpia la lista.
            hilos.clear()


        # Se crean los hilos y se inicia el llenado de la matriz 2.
        # Cada hilo creando es agregado a una lista.
            for i in range(numero_hilos):
                t= threading.Thread(target=llenar, args=(matriz2, lis_inicios[i], lis_fines[i], fil_col))
                hilos.append(t)
                t.start()

            # Por medio de la lista de hilos
            # pedimos que se sincronicen los procesos.         
            for i in hilos:
                i.join()

            hilos.clear()
            
            
            #######################################################
            # Se inicia la medicion de tiempo para un elemento del conjuto de pruebas.
            t1_start = process_time()

            # Se ejecuta la multiplicacion.
            for i in range(numero_hilos):
                t= threading.Thread(target=multi, args=(matriz1, matriz2, resultado, lis_inicios[i], lis_fines[i]))
                hilos.append(t)
                t.start()
            
            # se sincronizan los hilos.
            for i in hilos:
                i.join()

            # finaliza la medicion de tiempo
            t1_stop = process_time() 
            #################################################

            # se añade el tiempo a la lista de tiempos.
            tiempos.append(t1_stop-t1_start)

        
        print("Circuito {} Completado".format(circuito)) 

        #Terminado cada circuito se guardan los resultados
        # en un archivo csv.   
        with open("tiempos_hilos.csv","a") as file:
            file.write(str(tiempos)+"\n")
    
    




