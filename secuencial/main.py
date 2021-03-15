from matrix_operations import Matrix
import cProfile
from time import process_time 


def m (fil_col):
    matriz1 = Matrix(fil_col)
    matriz2 = Matrix(fil_col)

    result=list()
    matriz1.product(matriz2, result) 



if __name__ == "__main__":
    #cProfile.run('m(100)')
    print ("hola")
