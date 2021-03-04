from matrix_operations import Matrix
from time import process_time 


if __name__ == "__main__":

    #Se define el tamaño del circuito.
    tam_circuito=10

    #Se define el conjunto de datos.
    pruebas=[100, 200, 400, 800, 1200, 1400, 1600, 1800, 2000, 2200]

    for circuito in range (tam_circuito):

        #Se crea un lista que almacenara los tiempos de cpu de cada
        #elemento en el conjunto de datos.
        tiempos=list()


        for fil_col in pruebas:

            #Se crean la  matrices con el primer tamaño del conjunto de pruebas
            matriz1 = Matrix(fil_col)
            matriz2 = Matrix(fil_col)

            result=list()

            # Tiempo de inicio
            t1_start = process_time()
                # Multiplicacion de matrices.
            matriz1.product(matriz2, result)

            #tiempo de finalizacion
            t1_stop = process_time() 


            # se añaden los tiempos de CPU a la lista.
            tiempos.append(t1_stop-t1_start)

        print("Circuito {} Completado".format(circuito))

        #Terminado cada circuito se guardan los resultados
        # en un archivo csv.    
        with open("tiempos_secuenciales.csv","a") as file:
            file.write(str(tiempos)+"\n")
