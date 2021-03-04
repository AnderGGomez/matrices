
num_hilos=8

fil=list()
for i in range(800):
    fil.append(i)
fil_col=800

p=fil_col//num_hilos
inicios=list()
fines=list()
inicio=0
fin=p
aux=fil_col
for i in range(num_hilos):
    aux=aux-p
    inicios.append(inicio)
    fines.append(fin)
    try:
        p=aux//(num_hilos-(i+1))
    except:
        p=0
    inicio=fin
    fin=fin+p

for i in range (num_hilos):
    print(fil[inicios[i]:fines[i]])


