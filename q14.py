from q5 import Multigrafo, gerar_grafo_aleatorio

def cortes(grafo):
    vertices_ativos = [v.vertice_id for v in grafo.vertices if v.is_active]
    n = len(vertices_ativos)

    visitado = {}
    disc = {}      
    low = {}       
    pai = {}
    timer = [0]

    articulacoes = set()
    pontes = []

    def dfs(u):
        visitado[u] = True
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        filhos = 0

        for aresta in grafo.iterar_aresta(grafo.vertices[u].cabeca_arestas):
            v = aresta.dest_id
            if not grafo.vertices[v].is_active:
                continue

            if v not in visitado:
                filhos += 1
                pai[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])

                if pai.get(u) is None and filhos > 1:
                    articulacoes.add(u)
                if pai.get(u) is not None and low[v] >= disc[u]:
                    articulacoes.add(u)
                if low[v] > disc[u]:
                    pontes.append((u, v))

            elif v != pai.get(u):
                low[u] = min(low[u], disc[v])

    for v in vertices_ativos:
        if v not in visitado:
            pai[v] = None
            dfs(v)

    return sorted(articulacoes), pontes


def print_cortes(grafo):
    arts, pts = cortes(grafo)

    print(f"\nGrafo: {grafo.name}")
    if arts:
        print(f"Pontos de articulação (corte em vértices): {arts}")
        print("  -> Remover qualquer um desses vértices desconecta o grafo.")
    else:
        print("Nenhum ponto de articulação encontrado (grafo 2-conexo ou vazio).")

    if pts:
        print(f"Pontes (corte em arestas): {pts}")
        print("  -> Remover qualquer uma dessas arestas desconecta o grafo.")
    else:
        print("Nenhuma ponte encontrada.")

    return arts, pts


if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1 - com articulação")
    g1.add_vertice(1, "A")  
    g1.add_vertice(2, "B") 
    g1.add_vertice(3, "C") 
    g1.add_vertice(4, "D")  
    g1.add_vertice(5, "E") 

    g1.add_aresta(0, 1, 1.0, "A->B")
    g1.add_aresta(1, 0, 1.0, "B->A")
    g1.add_aresta(1, 2, 1.0, "B->C")
    g1.add_aresta(2, 1, 1.0, "C->B")
    g1.add_aresta(2, 3, 1.0, "C->D")  
    g1.add_aresta(3, 4, 1.0, "D->E")
    g1.add_aresta(4, 3, 1.0, "E->D")

    g1.print_multigrafo()
    print_cortes(g1)

    g2 = Multigrafo("Grafo 2 - aleatório")
    gerar_grafo_aleatorio(g2, num_vertices=6, num_arestas=8)
    g2.print_multigrafo()
    print_cortes(g2)

    g3 = Multigrafo("Grafo 3 - ciclo (sem articulação)")
    for i in range(4):
        g3.add_vertice(i, f"V{i}")
    g3.add_aresta(0, 1, 1.0, "0->1"); g3.add_aresta(1, 0, 1.0, "1->0")
    g3.add_aresta(1, 2, 1.0, "1->2"); g3.add_aresta(2, 1, 1.0, "2->1")
    g3.add_aresta(2, 3, 1.0, "2->3"); g3.add_aresta(3, 2, 1.0, "3->2")
    g3.add_aresta(3, 0, 1.0, "3->0"); g3.add_aresta(0, 3, 1.0, "0->3")

    g3.print_multigrafo()
    print_cortes(g3)