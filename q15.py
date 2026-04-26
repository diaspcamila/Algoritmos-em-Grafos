from q5 import Multigrafo, gerar_grafo_aleatorio
from collections import deque

def corte_fundamental(self):
    v_ativos = [v.vertice_id for v in self.vertices if v.is_active]
    if not v_ativos: return "Grafo Vazio"

    adj_grafo = {v: [] for v in v_ativos}
    # confere se tem uma arvore geradora
    for v_id in v_ativos:
        atual = self.vertices[v_id].cabeca_arestas
        while atual:
            adj_grafo[v_id].append((atual.dest_id, atual.aresta_id))
            if atual.dest_id in adj_grafo:
                adj_grafo[atual.dest_id].append((v_id, atual.aresta_id))
            atual = atual.next
    
    arvore_arestas = set()
    visitados = {v_ativos[0]}
    fila = deque([v_ativos[0]])
    # busca das arestas para saber as ligaçioes e ver qual o t a ser cortado
    while fila:
        atual = fila.popleft()

        for vizinho, aresta_id in adj_grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                arvore_arestas.add(aresta_id)
                fila.append(vizinho)
        
    if len(visitados) < len(v_ativos):
        return "Grafo Desconexo"
    
    t_id = arvore_arestas.pop()
    arvore_arestas.add(t_id)

    S1 = set()

    inicio_S1 = None
    for v in v_ativos:
        for vizinho, aresta_id in adj_grafo[v]:
            if aresta_id == t_id:
                inicio_S1 = v
                break
        if inicio_S1 is not None: break
    
    fila_S1 = deque([inicio_S1])
    S1.add(inicio_S1)

    while fila_S1:
        atual = fila_S1.popleft()

        for vizinho, aresta_id in adj_grafo[atual]:
            if aresta_id in arvore_arestas and aresta_id != t_id and vizinho not in S1:
                S1.add(vizinho)
                fila_S1.append(vizinho)
    
    S2 = set(v_ativos) - S1
    cortes_id = set()

    for v in S1:
        for vizinho, aresta_id in adj_grafo[v]:
            if vizinho in S2:
                cortes_id.add(aresta_id)
                
    return {
        "Aresta t cortada": t_id,
        "Componente S1": S1,
        "Componente S2": S2,
        "Arestas do Corte Fundamental": list(cortes_id)
    }

Multigrafo.corte_fundamental = corte_fundamental

if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, 5, 8)
    g1.print_multigrafo()


    print(f"Corte Fundamental do Grafo: {g1.corte_fundamental()}")