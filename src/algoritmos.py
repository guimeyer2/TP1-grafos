
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