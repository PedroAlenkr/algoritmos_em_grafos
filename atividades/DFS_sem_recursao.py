def imprime(d,f,N):
    for i in range(N):
        print("Vertice ",i+1,":",d[i],f[i])

def loadlista():
    arquivo = open('python\\ex5\\grafo.txt', 'r')
    lista = arquivo.readlines() # ler todas as linhas e salva em lista
    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])    
            lista_adj = [[] for _ in range(N)] # criando uma lista de lista
        else:
            lista_adj[int(linha[0])-1].append(int(linha[1])-1)
    arquivo.close()        
    return lista_adj,N       
            
def DFS_visit_sem_recusao(u):
    global mark
    fecho = 0
    pilha = [(u,0)]
    while pilha:
        if fecho:
            cor[u] = "Preto"
            mark = mark + 1
            f[u] = mark
            [u,i] = pilha.pop()
        else:
            cor[u] = "Cinza"
            mark = mark + 1
            d[u] = mark
            i=0
        fecho = 1
        while fecho and i < len(lista_adj[u]):
            v = lista_adj[u][i]
            if cor[v]=="Branco":
                fecho = 0
                pilha.append([u,i])
                u = v
            else:
                i=i+1            
            
def DFS():
    for u in V:
        cor[u]="Branco"
    for u in V:
        if cor[u] == "Branco":
            DFS_visit_sem_recusao(u)

       
[lista_adj,N]=loadlista()  
V = list(range(0,N))
#V = [0,1,2,3,4,5,6,7]
cor = [0]*N    
d = [0]*N
f = [0]*N
mark = 0
DFS() 
imprime(d,f,N)