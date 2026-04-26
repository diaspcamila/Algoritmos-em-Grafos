from q5 import Multigrafo, gerar_grafo_aleatorio
from collections import deque

def bfs(grafo, fonte=None):
    vertices_ativos = [v.vertice_id for v in grafo.vertices if v.is_active]
    dist = {v: -1 for v in vertices_ativos}
    pai  = {v: None for v in vertices_ativos}
    ordem_visita = []
    arestas_arvore = []

    fontes = [fonte] if fonte is not None else vertices_ativos

    for inicio in fontes:
        if dist[inicio] != -1:
            continue
        dist[inicio] = 0
        fila = deque([inicio])
        while fila:
            u = fila.popleft()
            ordem_visita.append(u)
            for aresta in grafo.iterar_aresta(grafo.vertices[u].cabeca_arestas):
                v = aresta.dest_id
                if v not in dist:
                    continue
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    pai[v] = u
                    arestas_arvore.append((u, v))
                    fila.append(v)

    return {
        "dist": dist,
        "pai": pai,
        "ordem_visita": ordem_visita,
        "arestas_arvore": arestas_arvore,
    }


def bfs_kahn(grafo):
    vertices_ativos = [v.vertice_id for v in grafo.vertices if v.is_active]

    grau_entrada = {v: 0 for v in vertices_ativos}
    for v_obj in grafo.vertices:
        if not v_obj.is_active:
            continue
        for aresta in grafo.iterar_aresta(v_obj.cabeca_arestas):
            if grafo.vertices[aresta.dest_id].is_active:
                grau_entrada[aresta.dest_id] += 1

    fila = deque(sorted([v for v in grau_entrada if grau_entrada[v] == 0]))
    ordem = []

    while fila:
        u = fila.popleft()
        ordem.append(u)
        for aresta in grafo.iterar_aresta(grafo.vertices[u].cabeca_arestas):
            v = aresta.dest_id
            if not grafo.vertices[v].is_active:
                continue
            grau_entrada[v] -= 1
            if grau_entrada[v] == 0:
                fila.append(v)

    tem_ciclo = len(ordem) < len(vertices_ativos)
    return ordem, tem_ciclo


def rotular_topologico_bfs(ordem):
    return {vid: i + 1 for i, vid in enumerate(ordem)}


def print_bfs(grafo):
    print(f"\nGrafo: {grafo.name}")
    print(f"{'─'*50}")

    resultado = bfs(grafo)
    print("\nBFS - Distâncias a partir do primeiro vértice ativo:")
    for v in sorted(resultado["dist"]):
        d = resultado["dist"][v]
        p = resultado["pai"][v]
        print(f"  V{v}: distância={d if d != -1 else '∞'}, pai={p}")

    print(f"\nOrdem de visita BFS : {resultado['ordem_visita']}")
    print(f"Arestas de árvore   : {resultado['arestas_arvore']}")

    ordem_top, tem_ciclo = bfs_kahn(grafo)
    rotulos = rotular_topologico_bfs(ordem_top)

    if tem_ciclo:
        print(f"\n⚠ Grafo contém ciclo(s). Ordenação topológica parcial.")
        verts = [v.vertice_id for v in grafo.vertices if v.is_active]
        nao_incluidos = [v for v in verts if v not in ordem_top]
        print(f"  Vértices em ciclo (não ordenados): {nao_incluidos}")
    else:
        print(f"\n✔ Grafo acíclico — ordenação topológica (Kahn/BFS) válida.")

    print(f"\nOrdem topológica BFS (Kahn): {ordem_top}")
    print(f"Rótulos topológicos        : {rotulos}")


if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1 - DAG")
    g1.add_vertice(1, "A") 
    g1.add_vertice(2, "B")  
    g1.add_vertice(3, "C")  
    g1.add_vertice(4, "D") 
    g1.add_vertice(5, "E")  

    g1.add_aresta(0, 1, 1.0, "A->B")
    g1.add_aresta(0, 2, 1.0, "A->C")
    g1.add_aresta(1, 3, 1.0, "B->D")
    g1.add_aresta(2, 3, 1.0, "C->D")
    g1.add_aresta(3, 4, 1.0, "D->E")

    g1.print_multigrafo()
    print_bfs(g1)

    g2 = Multigrafo("Grafo 2 - Com Ciclo")
    gerar_grafo_aleatorio(g2, num_vertices=5, num_arestas=7)
    g2.print_multigrafo()
    print_bfs(g2)