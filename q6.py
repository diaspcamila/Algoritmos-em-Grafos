from q5 import Multigrafo, gerar_grafo_aleatorio

def inorder(grafo):

    visitado = set()
    em_pilha = set()  
    ordem = []
    tem_ciclo = [False]

    def dfs_inorder(v):
        visitado.add(v)
        em_pilha.add(v)
        ordem.append(v)  

        for aresta in grafo.iterar_aresta(grafo.vertices[v].cabeca_arestas):
            viz = aresta.dest_id
            if not grafo.vertices[viz].is_active:
                continue
            if viz not in visitado:
                dfs_inorder(viz)
            elif viz in em_pilha:
                tem_ciclo[0] = True

        em_pilha.remove(v)

    for v in grafo.vertices:
        if v.is_active and v.vertice_id not in visitado:
            dfs_inorder(v.vertice_id)

    if tem_ciclo[0]:
        print("O grafo contém ciclos. Ordenação topológica estrita não é possível.")
    else:
        print("Grafo acíclico: ordenação topológica válida.")

    return ordem


def rotular_topologico(grafo, ordem):
    rotulos = {}
    for i, vid in enumerate(ordem):
        rotulos[vid] = i + 1
    return rotulos


if __name__ == "__main__":

    g1 = Multigrafo("Grafo 1 - DAG")
    g1.add_vertice(1.0, "A")  
    g1.add_vertice(2.0, "B") 
    g1.add_vertice(3.0, "C")  
    g1.add_vertice(4.0, "D") 
    g1.add_vertice(5.0, "E")

    g1.add_aresta(0, 1, 1.0, "A->B")
    g1.add_aresta(0, 2, 1.0, "A->C")
    g1.add_aresta(1, 3, 1.0, "B->D")
    g1.add_aresta(2, 3, 1.0, "C->D")
    g1.add_aresta(3, 4, 1.0, "D->E")

    g1.print_multigrafo()
    print("\n--- Travessia In-Order (Grafo 1) ---")
    ordem1 = inorder(g1)
    rotulos1 = rotular_topologico(g1, ordem1)
    print(f"Ordem de visita (in-order): {ordem1}")
    print(f"Rótulos topológicos: {rotulos1}")

    g2 = Multigrafo("Grafo 2 - Com Ciclo")
    gerar_grafo_aleatorio(g2, num_vertices=5, num_arestas=7)

    g2.print_multigrafo()
    print("\n--- Travessia In-Order (Grafo 2) ---")
    ordem2 = inorder(g2)
    rotulos2 = rotular_topologico(g2, ordem2)
    print(f"Ordem de visita (in-order): {ordem2}")
    print(f"Rótulos topológicos: {rotulos2}")