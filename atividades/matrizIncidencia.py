import numpy as np

def imprime(V,A,mat):
    for i in range(A):
        for j in range(V):
            print(mat[i,j],end=' ')
        print()        
    
def loadMatriz():
    arquivo = open('python\\ex3\\grafo.txt', 'r')
    lista = arquivo.readlines() # ler todas as linhas e salva em lista
   
    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            V = int(linha[0]) #vertices
            A = int(linha[1]) #arestas
            matriz_inc = np.zeros( (A ,V),dtype =np.int64 )         
        else:
            if i == 1 :j=0
            matriz_inc[ j,int(linha[0])] = 1   
            matriz_inc[ j,int(linha[1])] = 1 
            j+=1
    arquivo.close()
    imprime(V,A,matriz_inc)
    
loadMatriz() 