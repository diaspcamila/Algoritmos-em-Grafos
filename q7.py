from q5 import Multigrafo, gerar_grafo_aleatorio

def posorder(self):
    visitado = set()
    pilha_posordem = []
    pilha_ciclo = set()
    ciclo = [False]

    def dfs(v):
        visitado.add(v)
        pilha_ciclo.add(v)

        for aresta in self.iterar_aresta(self.vertices[v].cabeca_arestas):
            if aresta.dest_id not in visitado:
                dfs(aresta.dest_id)
            elif aresta.dest_id in pilha_ciclo:
                ciclo[0] = True
        
        pilha_ciclo.remove(v)
        
        pilha_posordem.append(v)

    for v in self.vertices:
        if v.is_active and v.vertice_id not in visitado:
            dfs(v.vertice_id)

    if ciclo[0]:
        print("O grafo contém um ciclo. ")


    return pilha_posordem[::-1]
        


if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    g2 = Multigrafo("Grafo 2")

    g1.add_vertice(1.0, "A") # 0
    g1.add_vertice(2.0, "B") # 1
    g1.add_vertice(3.0, "C") # 2
    g1.add_vertice(4.0, "D") # 3
    g1.add_vertice(5.0, "E") # 4

    g1.add_aresta(0, 1, 1.5, "A->B")
    g1.add_aresta(0, 2, 2.5, "A->C")
    g1.add_aresta(1, 4, 1.0, "B->E")
    g1.add_aresta(2, 3, 3.0, "C->D")

    print("Ordenação: ", posorder(g1))