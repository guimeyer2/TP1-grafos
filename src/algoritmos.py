
from grafo import Grafo

def eh_conexo(grafo: Grafo) -> bool:
    """
    Verifica se um grafo é conexo utilizando uma Busca em Profundidade (DFS).


    Returna:
        bool: True se o grafo for conexo, False caso contrário.
    """
    vertices = grafo.get_vertices()
    
  
    if not vertices:
        return True 

    visitados = set()
    vertice_inicial = vertices[0]
    
    
    pilha = [vertice_inicial]
    
    while pilha:
        vertice_atual = pilha.pop()
        if vertice_atual not in visitados:
            visitados.add(vertice_atual)
            
            # adiciona os vizinhos não visitados à pilha
            for vizinho in grafo.vizinhos(vertice_atual):
                if vizinho not in visitados:
                    pilha.append(vizinho)

    # se o número de vértices visitados for igual ao total de vértices,
    # o grafo é conexo.
    return len(visitados) == len(vertices)

def encontrar_pontes_naive(grafo: Grafo) -> list[tuple]:
    """
    encontra todas as pontes em um grafo usando o método naïve.
    


    Retorna:
        list[tuple]: lista de tuplas, onde cada tupla representa uma aresta ponte.
    """
    pontes = []
   
    arestas_originais = grafo.get_arestas()

    for u, v in arestas_originais:
       
        grafo.remover_aresta(u, v)

      
        if not eh_conexo(grafo):
            
            pontes.append(tuple(sorted((u, v))))

        grafo.adicionar_aresta(u, v)
    
    return pontes

def encontrar_pontes_tarjan(grafo: Grafo) -> list[tuple]:
    """
    encontra todas as pontes em um grafo usando o algoritmo de Tarjan.

    

    Retorna:
        list[tuple]: lista de tuplas, onde cada tupla representa uma aresta ponte.
    """
    visitados = set()
    tempo_descoberta = {}
    low = {}
    parent = {}
    pontes = []
    tempo = [0]  

    def _dfs_tarjan(u):
        visitados.add(u)
        tempo_descoberta[u] = low[u] = tempo[0]
        tempo[0] += 1

        for v in grafo.vizinhos(u):
            if v == parent.get(u):
                continue  

            if v in visitados:
                
                low[u] = min(low[u], tempo_descoberta[v])
            else:
               
                parent[v] = u
                _dfs_tarjan(v)

             
                low[u] = min(low[u], low[v])

               
                # se o menor tempo alcançável por 'v' é maior que o tempo de
                # descoberta de 'u', então a aresta (u, v) é uma ponte.
                if low[v] > tempo_descoberta[u]:
                    
                    pontes.append(tuple(sorted((u, v))))

    
    for vertice in grafo.get_vertices():
        if vertice not in visitados:
            _dfs_tarjan(vertice)
            
    return pontes