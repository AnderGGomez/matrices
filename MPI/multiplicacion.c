#include <stdio.h>
#include <mpi.h>
#include <stdlib.h>
#include <unistd.h>
#include <alloca.h>
#include <time.h>
#include <limits.h>

MPI_Status status;


int *createMatrix (int nrows, int ncols, int sw) {
    int *matrix;
    int h, i, j;

    if (( matrix = malloc(nrows*ncols*sizeof(int))) == NULL) {
        printf("Malloc error");
        exit(1);
    }

    if (sw == 1){
        for (h=0; h<nrows*ncols; h++) {
            matrix[h] = rand()%1001;
        }
    }/*else{
        for (h=0; h<nrows*ncols; h++) {
            matrix[h] = 0;
        }
    }*/
    

    return matrix;
}

void printArray (int *row, int nElements, int mod) {
    int i;
    for (i=0; i<nElements; i++) {
        if (i % mod == 0){
            printf("\n");
        }
        printf("%d ", row[i]);
    }
    printf("\n");
}


int main(int argc, char* argv[]){
    int rank, size;
    struct timespec begin, end;
    
    int n_data= atoi(argv[1]);
    int aux;
    int acum;
    int *matrizA;
    int **matrizB;
    int *matrizR;
    

    srand(time(0));
    char hostname[HOST_NAME_MAX + 1];
    gethostname(hostname, HOST_NAME_MAX + 1);


    //Reserva de memoria matriz B
    matrizB=(int **)malloc(n_data*sizeof(int*));
    
    for (int i=0; i<n_data; i++){
        matrizB[i]=(int *)malloc(n_data*sizeof(int));
    }

    matrizR = createMatrix(n_data, n_data, 0); // Master process creates matrix

    
    /* start up mpi */
    MPI_Init(&argc, &argv);
    /* Datos de prueba */
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int tam_buff=n_data*(n_data/size);
    int tam_row=n_data/size;



    //---------------------------------------

    if (rank==0){
        
        printf("Rank: %d, Size: %d, Host: %s\n",rank,size, hostname);

        matrizA = createMatrix(n_data, n_data, 1); // Master process creates matrix

        /* Al crear la matriz B asumimos que la matriz es transpuesta, de esta manera
        Podemos implementar la multiplicacion de matrices de optimizando la memoria*/
        
        for (int i=0; i<n_data; i++){
            for (int j=0; j<n_data; j++){
                matrizB[i][j]=rand()%1001;
            }
        }
        /*printf("Initial matrix A:\n");
        printArray(matrizA, n_data*n_data, n_data);
        printf("Matriz B\n");
        for (int i = 0; i < n_data; i++)
        {
            for (int j = 0; j < n_data; j++)
            {
                printf("%d,",matrizB[i][j]);
            }
            printf("\n");
        }
        printf("\n");*/
        
    }
    int *vec = malloc(sizeof(int) *tam_buff);
    int *procRow = malloc(sizeof(int) *tam_buff);
    MPI_Scatter(matrizA, tam_buff, MPI_INT, // send one row, which contains p integers
                procRow, tam_buff, MPI_INT, // receive one row, which contains p integers
                0, MPI_COMM_WORLD);

    for (int i = 0; i < n_data; i++)
    {
        MPI_Bcast(matrizB[i],n_data,MPI_INT,0,MPI_COMM_WORLD);
    }
    //printArray(procRow,n_data);
    MPI_Barrier(MPI_COMM_WORLD);       
    //printf("Rank: %d, Size: %d, Host: %s\n",rank,size, hostname);

    clock_gettime(CLOCK_REALTIME, &begin);
    aux=0;


    int start=0;
    int fin=start+n_data;
    for (int k = 0; k < tam_row; k++)
    {
        for (int i = 0; i < n_data; i++)
        {
            acum=0;
            for (int j = start; j < fin; j++)
            {
                aux=procRow[j]*matrizB[i][j%n_data];
                acum+=aux;
            }
            vec[i+start]=acum;
        }
        start+=n_data;
        fin+=n_data;
    }

    
    MPI_Barrier(MPI_COMM_WORLD); 
    clock_gettime(CLOCK_REALTIME, &end);

    //printArray(vec,tam_buff,n_data);
    /*
    for (int j = 0; j < n_data; j++)
    {
        printf("%d,",vec[j]);
    }
    printf("\n");*/

    MPI_Gather(vec, tam_buff, MPI_INT, matrizR, tam_buff,  MPI_INT, 0, MPI_COMM_WORLD);
    
    
    //------------------------
    if (rank==0)
    {
        free(matrizA);

        /*printf("Resultado multiplicacion");
        printArray(matrizR, n_data*n_data, n_data);*/

        long seconds = end.tv_sec - begin.tv_sec;
        long nanoseconds = end.tv_nsec - begin.tv_nsec;
        double elapsed = seconds + nanoseconds*1e-9;
        printf("Tiempo de ejecucion : %.6f\n", elapsed);
        FILE *fp;
        fp=fopen("tiempos.csv","ab");
        fprintf(fp, "%.6f,", elapsed);
        //fwrite(tiempos,sizeof(int), sizeof(tiempos), fp);
        fclose(fp);
    }

    free(matrizR);
    free(vec);
    free(procRow);
    MPI_Finalize();

    for (int i=0; i<n_data; i++){
        free(matrizB[i]);
    }
    free(matrizB);
}