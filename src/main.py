import sys
import time
from grafo import Grafo
from algoritmos import (
    encontrar_pontes_naive, 
    encontrar_pontes_tarjan, 
    encontrar_caminho_euleriano
)
from gerador import gerar_grafo_aleatorio

# --- CONFIGURAÇÃO DOS EXPERIMENTOS ---

# O método Naïve é muito lento para grafos grandes. Podendo levar muito tempo para grafos com 1000 vértices ou mais.
# O script abaixo tem uma trava para não rodar o Naïve para grafos >= 10000.
TAMANHOS = [100, 1000, 10000, 100000]
TIPOS = ['euleriano', 'semi-euleriano' , 'nao-euleriano']
ARESTAS_ADICIONAIS_POR_VERTICE = 1 


sys.setrecursionlimit(max(TAMANHOS) + 100)

# --- EXECUÇÃO DOS EXPERIMENTOS ---

print("="*40)
print("INICIANDO ANÁLISE DE DESEMPENHO")
print("="*40)

for tamanho in TAMANHOS:
    for tipo in TIPOS:
        print(f"\n--- Testando Grafo de {tamanho} vértices ({tipo}) ---")
        
        num_arestas_adicionais = tamanho * ARESTAS_ADICIONAIS_POR_VERTICE
        
        # 1. Gerar o grafo
        print(f"Gerando grafo...")
        g = gerar_grafo_aleatorio(tamanho, num_arestas_adicionais, tipo)
        print(f"Grafo gerado com {len(g.get_vertices())} V e {len(g.get_arestas())} E.")

        # 2. Executar com buscador Naïve 
        tempo_naive = float('inf') 
        if tamanho < 10000:
            print("Executando com buscador Naïve...")
            start_time_naive = time.time()
            encontrar_caminho_euleriano(g, encontrar_pontes_naive)
            end_time_naive = time.time()
            tempo_naive = end_time_naive - start_time_naive
            print(f"  -> Tempo gasto: {tempo_naive:.6f} segundos")
        else:
            print("Executando com buscador Naïve... [PULADO DEVIDO AO TAMANHO]")

        # 3. Executar com buscador Tarjan
        print("Executando com buscador Tarjan...")
        start_time_tarjan = time.time()
        encontrar_caminho_euleriano(g, encontrar_pontes_tarjan)
        end_time_tarjan = time.time()
        tempo_tarjan = end_time_tarjan - start_time_tarjan
        print(f"  -> Tempo gasto: {tempo_tarjan:.6f} segundos")
        
        # 4. Imprimir comparação
        if tempo_naive != float('inf'):
            if tempo_tarjan > 0:
                speedup = tempo_naive / tempo_tarjan
                print(f"\n  Comparação: Tarjan foi ~{speedup:.2f}x mais rápido.")
            else:
                print("\n  Comparação: Tarjan foi instantâneo.")

print("\n" + "="*40)
print("ANÁLISE DE DESEMPENHO CONCLUÍDA")
print("="*40)