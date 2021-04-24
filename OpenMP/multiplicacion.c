#include <stdio.h>
#include <stdlib.h>
#include <alloca.h>
#include <time.h>

void llenar(int **matriz, int n){
    for (int i=0; i<n; i++){
        for (int j=0; j<n; j++){
            matriz[i][j]=rand()%1001;
        }
    }
}

void mult (int **matrizA, int **matrizB, int **matrizR, int n){
    int acum=0;
    int aux=0;
    //private(acum, n) schedule(static, 4)
    //#pragma omp parallel for private(acum, aux) schedule(static, 4)
    #pragma omp parallel for private(acum,aux) schedule(static,4)
    for (int k=0; k<n; k++)
    {
        //#pragma omp parallel for
        for (int i=0; i<n; i++){
            acum=0;
            for (int j=0; j<n; j++){
                aux=matrizA[k][j]*matrizB[j][i];
                acum+=aux;
            }
            matrizR[k][i]=acum;
        }
    }
}
void mult1 (int **matrizA, int **matrizB, int **matrizR, int n){
    int acum=0;
    int aux=0;
    for (int k=0; k<n; k++)
    {
        for (int i=0; i<n; i++){
            acum=0;
            for (int j=0; j<n; j++){
                aux=matrizA[k][j]*matrizB[i][j];
                acum+=aux;
            }
            matrizR[k][i]=acum;
        }
    }
}



void main(int argc, int **argv){
    //printf("%s",argv[1]);
    int n=10;
    double tiempos[10];
    int segment[]={100, 200, 400, 800, 1200, 1400, 1600, 1800, 2000, 2200};

    int tam = sizeof(segment)/sizeof(int);

    for(int p=0; p< n; p++){
        for(int q=0; q<tam; q++){
            int **matrizA;
            int **matrizB;
            int **matrizR;
            struct timespec begin, end;

            //Reserva de memoria matriz A
            matrizA=(int **)malloc(segment[q]*sizeof(int*));
            
            for (int i=0; i<segment[q]; i++){
                matrizA[i]=(int *)malloc(segment[q]*sizeof(int));
            }


            //Reserva de memoria matriz B
            matrizB=(int **)malloc(segment[q]*sizeof(int*));
            
            for (int i=0; i<segment[q]; i++){
                matrizB[i]=(int *)malloc(segment[q]*sizeof(int));
            }

            //Reserva de memoria matriz R
            matrizR=(int **)malloc(segment[q]*sizeof(int*));
            
            for (int i=0; i<segment[q]; i++){
                matrizR[i]=(int *)malloc(segment[q]*sizeof(int));
            }
            srand(time(0));
            llenar(matrizA,segment[q]);
            llenar(matrizB,segment[q]);
            

        //############LLENADO DE MATRICES#################

            clock_gettime(CLOCK_REALTIME, &begin);

            mult(matrizA, matrizB, matrizR, segment[q]);
            //mult1(matrizA, matrizB, matrizR, segment[q]);

            clock_gettime(CLOCK_REALTIME, &end);

            long seconds = end.tv_sec - begin.tv_sec;
            long nanoseconds = end.tv_nsec - begin.tv_nsec;
            double elapsed = seconds + nanoseconds*1e-9;
            printf("Tiempo de ejecucion : %.3f\n", elapsed);
            tiempos[q]=elapsed;
            
            /*
            for (int i=0; i<n; i++){
                for (int j=0; j<n; j++){
                    printf("MA[%d][%d] : %d\n", i,j, matrizA[i][j]);
                }
            }

            for (int i=0; i<n; i++){
                for (int j=0; j<n; j++){
                    printf("MB[%d][%d] : %d\n", i,j, matrizB[i][j]);
                }
            }
            
            for (int i=0; i<n; i++){
                for (int j=0; j<n; j++){
                    printf("MR[%d][%d] : %d\n", i,j, matrizR[i][j]);
                }
            }*/
            
            for (int i=0; i<segment[q]; i++){
                free(matrizA[i]);
            }
            free(matrizA);

            for (int i=0; i<segment[q]; i++){
                free(matrizB[i]);
            }
            free(matrizB);

            for (int i=0; i<segment[q]; i++){
                free(matrizR[i]);
            }
            free(matrizR);
        }
        FILE *fp;
        fp=fopen("tiemposC2.csv","ab");
        for (int i=0; i<tam; i++){
            fprintf(fp, "%.3f,", tiempos[i]);
        }
        fprintf(fp, "%s","\n");
        //fwrite(tiempos,sizeof(int), sizeof(tiempos), fp);
        fclose(fp);
    }
    

    
}
