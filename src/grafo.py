class Grafo:
    """
    Classe para representar um grafo simples não-direcionado usando lista de adjacência.

    """

    def __init__(self):
        
        self._adj = {}

    def get_vertices(self):
        
        return list(self._adj.keys())

    def get_arestas(self):
       
        arestas = set()
        for u in self._adj:
            for v in self._adj[u]:
              
                if u < v:
                    arestas.add((u, v))
        return list(arestas)

    def __len__(self):
        """retorna o número de vértices no grafo."""
        return len(self._adj)

    def __str__(self):
       
        if not self._adj:
            return 
        
        resultado = []
        for u in self._adj:
            vizinhos = ", ".join(map(str, self._adj[u]))
            resultado.append(f"{u}: [{vizinhos}]")
        return "\n".join(resultado)

    def adicionar_vertice(self, u):
       
        if u not in self._adj:
            self._adj[u] = []

    def adicionar_aresta(self, u, v):
        
        self.adicionar_vertice(u)
        self.adicionar_vertice(v)
        
        if v not in self._adj[u]:
            self._adj[u].append(v)
        if u not in self._adj[v]:
            self._adj[v].append(u)
            
    def remover_aresta(self, u, v):
        
        try:
            self._adj[u].remove(v)
            self._adj[v].remove(u)
        except (KeyError, ValueError):
      
            pass
            
    def grau(self, u):
        
        return len(self._adj.get(u, []))

    def vizinhos(self, u):
        
        return self._adj.get(u, [])