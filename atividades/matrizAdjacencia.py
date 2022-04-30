import numpy as np

def imprime(N,mat):
    for i in range(N):
        for j in range(N):
            print(mat[i,j],end=' ')
        print()        
    
def loadMatriz():
    arquivo = open('python\\ex1\\grafo.txt', 'r')
    lista = arquivo.readlines() # ler todas as linhas e salva em lista
   
    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])
            matriz_adj = np.zeros( (N ,N),dtype =np.int64 )         
        else:
            matriz_adj[ int(linha[0]),int(linha[1])] = 1   
            matriz_adj[ int(linha[1]),int(linha[0])] = 1 
    arquivo.close()
    imprime(N,matriz_adj)
    
loadMatriz()    