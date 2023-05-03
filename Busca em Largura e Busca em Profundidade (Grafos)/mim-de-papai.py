class Grafo:
    def __init__(self, usuarios):
        self.usuarios = usuarios
        self.grafo = [[] for i in range(usuarios)]

    def busca_profundidade(self, no):
        self.visitados[no] = True
        for vizinho in self.grafo[no]:
            if not self.visitados[vizinho]:
                self.busca_profundidade(vizinho)

    def vertices_alcancaveis(self, no):
        self.visitados = [False] * self.usuarios
        self.busca_profundidade(no)
        alcancaveis = [i for i in range(self.usuarios) if self.visitados[i]]
        return alcancaveis


usuarios, conexoes = input().split()
usuarios = int(usuarios)
conexoes = int(conexoes)
grafo = Grafo(usuarios)

for i in range(conexoes):
    conexoes = input().split()
    conexoes_int = [int(i) for i in conexoes]
    grafo.grafo[conexoes_int[0]-1].append(conexoes_int[1]-1)
    grafo.grafo[conexoes_int[1]-1].append(conexoes_int[0]-1)

lista_inteiros = []
for usuario in range(usuarios):
    usuarios_saberiam_noticia = len(grafo.vertices_alcancaveis(usuario))
    lista_inteiros.append(usuarios_saberiam_noticia)

print(*lista_inteiros)
