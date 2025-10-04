
import random
from grafo import Grafo

def gerar_grafo_aleatorio(num_vertices: int, num_arestas_adicionais: int, tipo: str = 'euleriano') -> Grafo:
    """
    Gera um grafo aleatório conexo com propriedades eulerianas específicas.

    Argumentos:
        num_vertices (int): O número de vértices no grafo.
        num_arestas_adicionais (int): O número de arestas a serem adicionadas
                                      além do ciclo inicial para garantir conectividade.
        tipo (str): O tipo de grafo a ser gerado ('euleriano', 'semi-euleriano' ou 'nao-euleriano').

    Retorna:
        Grafo: O grafo gerado.
    """
    if num_vertices <= 0:
        return Grafo()

    g = Grafo()
    for i in range(num_vertices):
        g.adicionar_vertice(i)

    
    for i in range(num_vertices):
        g.adicionar_aresta(i, (i + 1) % num_vertices)

 
    arestas_adicionadas = 0
    max_iteracoes = num_vertices * num_vertices 
    iteracoes = 0
    
    while arestas_adicionadas < num_arestas_adicionais and iteracoes < max_iteracoes:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)

        
        if u != v and v not in g.vizinhos(u):
            g.adicionar_aresta(u, v)
            arestas_adicionadas += 1
        iteracoes += 1

    
    vertices_impares = [v for v in g.get_vertices() if g.grau(v) % 2 != 0]
    random.shuffle(vertices_impares)

    
    alvo_impares = 0
    if tipo == 'semi-euleriano':
        alvo_impares = 2
    elif tipo == 'nao-euleriano':
      
        alvo_impares = 4


    while len(vertices_impares) > alvo_impares:
        
        u = vertices_impares.pop(0)
        v = vertices_impares.pop(0)

        
        if v in g.vizinhos(u):
            g.remover_aresta(u, v)
        else:
            g.adicionar_aresta(u, v)

    return g