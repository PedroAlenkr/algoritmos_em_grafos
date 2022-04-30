from collections import deque

def loadlista():
    arquivo = open('python\\ex6\\grafo.txt', 'r')
    lista = arquivo.readlines() # ler todas as linhas e salva em lista
    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])    
            lista_adj = [[] for _ in range(N)] 
        else:
            lista_adj[int(linha[0])-1].append(int(linha[1])-1)
    arquivo.close()        
    return lista_adj,N   

def BFS(s):
    for u in range(N):
        cor[u] = "Branco"
        d[u] = None
        pi[u] = None
    cor[s] = "Cinza"
    d[s] = 0
    pi[s] = None
    Q = deque()
    Q.append(s)
    while Q:
        u = Q.popleft()
        for v in lista_adj[u]:
            if cor[v] == "Branco":
                cor[v] = "Cinza"
                pi[v] = u
                d[v] = d[u]+1
                Q.append(v)
        cor[u] = "Preto"
    print(d,pi)
                 
[lista_adj,N]=loadlista()  
cor = [None]*N
d = [None]*N
pi = [None]*N
BFS(0)