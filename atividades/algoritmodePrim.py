import heapq
import sys

def loadlista():
    arquivo = open('python\\ex8\\grafo.txt', 'r')
    lista = arquivo.readlines() # ler todas as linhas e salva em lista
    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])    
            W = []
            for i in range(N):
                W.append( [0] * N )
            lista_adj = [[] for _ in range(N)] 
        else:
            lista_adj[int(linha[0])-1].append(int(linha[1])-1)
            lista_adj[int(linha[1])-1].append(int(linha[0])-1)
            W[int(linha[0])-1][int(linha[1])-1] = int(linha[2]) 
            W[int(linha[1])-1][int(linha[0])-1] = int(linha[2]) 
    arquivo.close()
    return lista_adj,N,W   

def dijkstra(s):
    for u in range(N): 
        dist[u] = sys.maxsize
        pi[u] = None
    dist[s] = 0
    Q = []
    heapq.heapify(Q)
        
    for i in range(N): 
        heapq.heappush(Q,(i,0))
        while Q: 
            [u,b] = heapq.heappop(Q)
            for v in lista_adj[u]:
                if dist[v] > W[u][v]: 
                    dist[v] = W[u][v]
                    pi[v] = u
                    heapq.heappush(Q,(v,dist[v]))


[lista_adj,N,W]=loadlista()  
dist = [0]*N
pi = [None]*N
dijkstra(0)
print(dist,pi)