from matrix_operations import Matrix
from time import process_time 



def ver (lista):
    for i in lista:
        print(i)


if __name__ == "__main__":
    fil_col=500
    matriz1 = Matrix(fil_col)
    matriz2 = Matrix(fil_col)

    result=list()
    inicio=process_time()
    matriz1.product(matriz2, result)
    fin=process_time()

    print(fin-inicio)
    #ver(result)

    
