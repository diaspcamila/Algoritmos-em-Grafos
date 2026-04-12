import random

class Aresta:
    def __init__(self, aresta_id, dest_id, custo, atributos):
        self.aresta_id = aresta_id
        self.dest_id = dest_id
        self.custo = custo
        self.atributos = atributos
        self.next = None
    
class Vertice:
    def __init__(self, vertice_id, custo, atributos):
        self.vertice_id = vertice_id
        self.custo = custo
        self.atributos = atributos
        self.cabeca_arestas = None
        self.is_active = True

class Multigrafo:
    def __init__(self, name = "Grafo direcionado"):
        self.name = name
        self.vertices = []
        self.arestas_cont = 0
    
    # funcoes de editar o grafo

    def destruir_grafo(self):
        self.vertices.clear()
        self.arestas_cont = 0
        print(f"Grafo '{self.name}' destruído com sucesso.")

    # funcoes editar vertices

    def add_vertice(self, custo, atributos):
        vertice_id = len(self.vertices)
        novo_vertice = Vertice(vertice_id, custo, atributos)
        self.vertices.append(novo_vertice)
        return vertice_id
    
    def edit_vertice(self, vertice_id, novo_custo, nova_atributos):
        v = self.buscar_vertice(vertice_id)
        if v:
            if novo_custo is not None: v.custo = novo_custo
            if nova_atributos is not None: v.atributos = nova_atributos
            return True
        return False

    def remove_vertice(self, vertice_id):
        if vertice_id >= len(self.vertices) or not self.vertices[vertice_id].is_active:
            return False

        for v in self.vertices:
            if v.is_active and v.vertice_id != vertice_id:
                self.remove_arestas_por_destino(v.vertice_id, vertice_id)

        self.vertices[vertice_id].is_active = False
        self.vertices[vertice_id].cabeca_arestas = None
        return True
    
    def buscar_vertice(self, vertice_id):
        if vertice_id < len(self.vertices) and self.vertices[vertice_id].is_active:
            return self.vertices[vertice_id]
        return None


    # funcoes de grau do vertice

    def grau_entrada(self, vertice_id):
        grau_cont = 0

        if not self.buscar_vertice(vertice_id):
            return -1

        for v in self.vertices:
            if v.is_active:
                atual = v.cabeca_arestas
                while atual:
                    if atual.dest_id == vertice_id:
                        grau_cont += 1
                    atual = atual.next
        return grau_cont

    def grau_saida(self, vertice_id):
        grau_cont = 0
        v = self.buscar_vertice(vertice_id)

        if not v:
            return -1

        atual = v.cabeca_arestas
        while atual:
            grau_cont += 1
            atual = atual.next
        return grau_cont
    
    def soma_graus(self, vertice_id):
        if self.grau_saida(vertice_id) == -1:
            return -1
        return self.grau_entrada(vertice_id) + self.grau_saida(vertice_id)


    # funcoes editar arestas

    def add_aresta(self, origem_id, dest_id, custo, atributos):
        if not self.buscar_vertice(origem_id) or not self.buscar_vertice(dest_id):
            return -1

        self.arestas_cont += 1
        e_id = self.arestas_cont

        nova_aresta_origem = Aresta(e_id, dest_id, custo, atributos)
        nova_aresta_origem.next = self.vertices[origem_id].cabeca_arestas
        self.vertices[origem_id].cabeca_arestas = nova_aresta_origem

        return e_id
    
    def edit_aresta(self, origem_id, aresta_id, novo_custo, nova_atributos):
        if not self.buscar_vertice(origem_id):
            return False
        
        self.edit_arestas_lista(origem_id, aresta_id, novo_custo, nova_atributos)
        return True

    def remove_aresta(self, origem_id, aresta_id):
        if not self.buscar_vertice(origem_id):
            return False
        
        self.remove_aresta_lista(origem_id, aresta_id)
        return True

    # funcoes utilitarias auxiliares

    def remove_arestas_por_destino(self, origem_id, dest_id_alvo):
        atual = self.vertices[origem_id].cabeca_arestas
        prev = None
        while atual:
            if atual.dest_id == dest_id_alvo:
                if prev:
                    prev.next = atual.next
                else:
                    self.vertices[origem_id].cabeca_arestas = atual.next
                atual = atual.next
            else:
                prev = atual
                atual = atual.next

    def remove_aresta_lista(self, vertice_id, aresta_id):
        atual = self.vertices[vertice_id].cabeca_arestas
        
        prev = None
        while atual:
            if atual.aresta_id == aresta_id:
                if prev:
                    prev.next = atual.next
                else:
                    self.vertices[vertice_id].cabeca_arestas = atual.next
                return
            prev = atual
            atual = atual.next

    def edit_arestas_lista(self, vertice_id, aresta_id, novo_custo, nova_atributos):
        atual = self.vertices[vertice_id].cabeca_arestas

        while atual:
            if atual.aresta_id == aresta_id:
                atual.custo = novo_custo
                atual.atributos = nova_atributos
                return
            atual = atual.next

    def print_multigrafo(self):
        print(f"\nMultigrafo: {self.name}")
        for v in self.vertices:
            if v.is_active:
                grau_saida = self.grau_saida(v.vertice_id)
                grau_entrada = self.grau_entrada(v.vertice_id)

                print(f"Vertice {v.vertice_id}: Custo={v.custo}, atributos={v.atributos}")
                atual = v.cabeca_arestas
                if not atual:
                    print(" -> Nenhuma saída")
                while atual:
                    print(f" -> Aponta para V{atual.dest_id} | ID Aresta: {atual.aresta_id} | Custo = {atual.custo} | atributos = {atual.atributos}")
                    atual = atual.next

    def iterar_aresta(self, cabeca):
        atual = cabeca
        while atual:
            yield atual
            atual = atual.next

def gerar_grafo_aleatorio(grafo, num_vertices, num_arestas):
        for i in range(num_vertices):
            grafo.add_vertice(custo=random.randint(1, 100), atributos=f"Nome_V{i}")

        vertices_ids = [v.vertice_id for v in grafo.vertices if v.is_active]

        for _ in range(num_arestas):
            v1 = random.choice(vertices_ids)
            v2 = random.choice(vertices_ids)
            custo = random.randint(1, 10)
            grafo.add_aresta(v1, v2, custo, atributos=f"Aresta_{v1}_para_{v2}")

if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, num_vertices=3, num_arestas=5)
    g2 = Multigrafo("Grafo 2")
    gerar_grafo_aleatorio(g2, num_vertices=5, num_arestas=7)

    g1.print_multigrafo()

    g2.print_multigrafo()
    