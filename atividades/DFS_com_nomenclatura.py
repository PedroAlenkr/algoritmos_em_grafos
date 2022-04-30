def imprime(d,f,N):
    for i in range(N):
        print("Vertice ",i+1,":",d[i],f[i])

def loadlista():
    arquivo = open('python\\ex9\\grafo.txt', 'r')
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
            
def DFS_visit(u):
    global mark
    cor[u] = "Cinza"
    mark = mark + 1
    d[u] = mark
    for v in lista_adj[u]:   #nomenclatura
        if cor[v]=="Branco":
            print('aresta', u,'-', v, 'arvore')
            DFS_visit(v)
        elif cor[v]=="Cinza":
            print('aresta', u,'-', v, 'retorno')
        elif d[u]<f[v]:
            print('aresta', u,'-', v, 'avanco')
        else:
            print('aresta', u,'-', v, 'cruzamento')
    cor[u] = "Preto"
    mark = mark + 1
    f[u] = mark
            
def DFS():
    for u in V:
        cor[u]="Branco"
    for u in V:
        if cor[u] == "Branco":
            DFS_visit(u)

       
[lista_adj,N]=loadlista()  
#V = list(range(0,N))
V = [2,0,1,3,4,5,6,7]
cor = [0]*N    
d = [0]*N
f = [0]*N
mark = 0
DFS() 
imprime(d,f,N)