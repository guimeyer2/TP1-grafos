from collections.abc import Callable
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


 



def encontrar_caminho_euleriano(grafo: Grafo, buscador_de_pontes: Callable[[Grafo], list[tuple]]) -> list:
    """
    Encontra um caminho ou ciclo Euleriano em um grafo usando o algoritmo de Fleury.

    Argumentos:
        grafo (Grafo): O grafo original.
        buscador_de_pontes (Callable): A função a ser usada para encontrar pontes 
                                     

    Retorna:
        list: Uma lista de vértices representando o caminho/ciclo Euleriano.
              lista vazia se não houver caminho.
    """
    
    
    vertices_grau_impar = [v for v in grafo.get_vertices() if grafo.grau(v) % 2 != 0]
    
    # um grafo só pode ter um caminho Euleriano se tiver 0 ou 2 vértices de grau ímpar.
    if len(vertices_grau_impar) not in [0, 2]:
        print("Não há caminho Euleriano: número de vértices de grau ímpar não é 0 ou 2.")
        return []

    if grafo.get_arestas() and not eh_conexo(grafo):
        print("Não há caminho Euleriano: o grafo não é conexo.")
        return []

    
    g_copia = grafo.copy()
    
    
    if vertices_grau_impar:
        vertice_atual = vertices_grau_impar[0] 
    else:
      
        primeiro_vertice = next((v for v in g_copia.get_vertices() if g_copia.grau(v) > 0), None)
        if primeiro_vertice is None: return [] 
        vertice_atual = primeiro_vertice

    caminho = [vertice_atual]
    
    

    while g_copia.get_arestas():
        vizinhos = g_copia.vizinhos(vertice_atual)
        if not vizinhos: break
        proximo_vertice = None

        if len(vizinhos) == 1:
           
            proximo_vertice = vizinhos[0]
        else:
       
            pontes_atuais = buscador_de_pontes(g_copia)
          
            pontes_normalizadas = {tuple(sorted(p)) for p in pontes_atuais}

            
            arestas_nao_ponte = [
                v for v in vizinhos 
                if tuple(sorted((vertice_atual, v))) not in pontes_normalizadas
            ]

            if arestas_nao_ponte:
                proximo_vertice = arestas_nao_ponte[0]
            else:
                
                proximo_vertice = vizinhos[0]

        g_copia.remover_aresta(vertice_atual, proximo_vertice)
        vertice_atual = proximo_vertice
        caminho.append(vertice_atual)

    return caminho