def imprime_lista(N,lista):
    for i in range(N):
        print("Vertice ",i,":",lista[i])

def loadlista():
    arquivo = open('python\\ex2\\grafo.txt', 'r')
    lista = arquivo.readlines() # ler todas as linhas e salva em lista
    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])    
            lista_adj = [[] for _ in range(N)] # criando uma lista de lista
        else:
            lista_adj[int(linha[0])].append(int(linha[1]))
            lista_adj[int(linha[1])].append(int(linha[0]))
            
    imprime_lista(N,lista_adj)
    
loadlista() 