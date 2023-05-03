def busca_largura(tamanho_lista):
    visitados = []
    fila = [usuario]

    while len(fila) != 0:
        user = fila.pop(0)
        if user not in visitados and len(visitados) != tamanho_lista:
            visitados.append(user)
            fila.extend(grafo[user])
    return visitados[1:]


numero_usuarios = int(input())
usuario = int(input())
valor_investido = int(input())

grafo = {}

for i in range(numero_usuarios):
    entrada = input().split()
    user = int(entrada[0])
    seguidores = [int(x) for x in entrada[2:]]
    grafo[user] = seguidores

tamanho_lista = (len(grafo[usuario])+1)
tamanho_lista += int(valor_investido/5.25)

usuarios_alcancados = busca_largura(tamanho_lista)

usuarios_atingidos = []
for user in usuarios_alcancados:
    usuarios_atingidos.append(str(user))
print(usuarios_atingidos)
