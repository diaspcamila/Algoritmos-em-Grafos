from q5 import Multigrafo, gerar_grafo_aleatorio
from q12 import excentricidade

#raio - rad(g) é o raio de um vertice central de g
# um vertice é central se possui o menor raio do grafo
# o centro é um subconjunto de vertices de excentricidade minima
# diam(g) - é o maior raio dentre os vertice de g

def val(self):
    excentricidades1 = self.excentricidade()
    
    valores = list(excentricidades1.values())
    raio = min(valores)
    diam = max(valores)

    centro = []
    for vertice, valor in excentricidades1.items():
        if valor == raio:
            centro.append(vertice)
        
    return{
        "Raio ": raio,
        "Diametro ": diam,
        "Centro ": centro
    }

Multigrafo.val = val

if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, 5, 5)
    g1.print_multigrafo()

    ans = g1.val()

    print(f"Raio: {ans["Raio "]}")
    print(f"Diametro: {ans["Diametro "]}")
    print(f"Centro: {ans["Centro "]}")

    