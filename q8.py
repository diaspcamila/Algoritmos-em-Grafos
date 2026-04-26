from q5 import Multigrafo, gerar_grafo_aleatorio

def arvore_geradora_dfs(grafo):
    visitado = set()
    arestas_arvore = [] 

    def dfs(v):
        visitado.add(v)
        for aresta in grafo.iterar_aresta(grafo.vertices[v].cabeca_arestas):
            viz = aresta.dest_id
            if not grafo.vertices[viz].is_active:
                continue
            if viz not in visitado:
                arestas_arvore.append((v, viz, aresta.custo, aresta.atributos))
                dfs(viz)

    for v in grafo.vertices:
        if v.is_active and v.vertice_id not in visitado:
            dfs(v.vertice_id)

    return arestas_arvore


def construir_subgrafo_arvore(grafo):
    arestas = arvore_geradora_dfs(grafo)

    vertices_ativos = [v for v in grafo.vertices if v.is_active]
    mapa_id = {v.vertice_id: i for i, v in enumerate(vertices_ativos)}

    arvore = Multigrafo(f"Árvore Geradora de [{grafo.name}]")

    for v in vertices_ativos:
        arvore.add_vertice(v.custo, v.atributos)

    for (orig, dest, custo, attrs) in arestas:
        arvore.add_aresta(mapa_id[orig], mapa_id[dest], custo, attrs)

    return arvore, arestas, mapa_id


def print_arvore_info(grafo_orig, arvore, arestas, mapa_id):
    vertices_ativos = [v for v in grafo_orig.vertices if v.is_active]
    n = len(vertices_ativos)
    m_orig = sum(
        sum(1 for _ in grafo_orig.iterar_aresta(v.cabeca_arestas))
        for v in grafo_orig.vertices if v.is_active
    )

    print(f"\nGrafo original: {n} vértices, {m_orig} arestas")
    print(f"Árvore geradora: {n} vértices, {len(arestas)} arestas")
    print("\nArestas da árvore geradora (origem -> destino):")
    for (orig, dest, custo, attrs) in arestas:
        print(f"  V{orig} -> V{dest} | custo={custo} | attrs={attrs}")
    print()
    arvore.print_multigrafo()


if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    g1.add_vertice(1, "A")  
    g1.add_vertice(2, "B")  
    g1.add_vertice(3, "C") 
    g1.add_vertice(4, "D")  
    g1.add_vertice(5, "E")  

    g1.add_aresta(0, 1, 1.0, "A->B")
    g1.add_aresta(0, 2, 2.0, "A->C")
    g1.add_aresta(1, 2, 1.5, "B->C")  
    g1.add_aresta(1, 3, 3.0, "B->D")
    g1.add_aresta(2, 4, 2.5, "C->E")
    g1.add_aresta(3, 4, 1.0, "D->E")  

    print("=== GRAFO ORIGINAL ===")
    g1.print_multigrafo()

    arvore1, arestas1, mapa1 = construir_subgrafo_arvore(g1)
    print("\n=== SUBGRAFO MAXIMAL ÁRVORE ===")
    print_arvore_info(g1, arvore1, arestas1, mapa1)

    g2 = Multigrafo("Grafo 2")
    gerar_grafo_aleatorio(g2, num_vertices=6, num_arestas=10)

    print("\n=== GRAFO ORIGINAL ===")
    g2.print_multigrafo()

    arvore2, arestas2, mapa2 = construir_subgrafo_arvore(g2)
    print("\n=== SUBGRAFO MAXIMAL ÁRVORE ===")
    print_arvore_info(g2, arvore2, arestas2, mapa2)