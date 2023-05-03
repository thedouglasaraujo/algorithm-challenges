def trocar_posicao(i, j):
    aux = lista_heap[i]
    lista_heap[i] = lista_heap[j]
    lista_heap[j] = aux


def maxheap(i):
    esquerdo = 2 * i
    direito = (2 * i) + 1
    tamanho = len(lista_heap)
    if esquerdo < tamanho and lista_heap[esquerdo] > lista_heap[i]:
        maior = esquerdo
    else:
        maior = i
    if direito < tamanho and lista_heap[direito] > lista_heap[maior]:
        maior = direito
    if maior != i:
        trocar_posicao(i, maior)
        maxheap(maior)


def remover_maxheap():
    ultimo_elemento = lista_heap[-1]
    lista_heap[1] = ultimo_elemento
    tamanho = len(lista_heap)
    tamanho = tamanho - 1
    maxheap(1)


def heap_extremo(tipo):
    if len(lista_heap) == 1:
        return lista_heap[0]
    else:
        if tipo == "max":
            return lista_heap[1]
        elif tipo == "min":
            tamanho = len(lista_heap)
            menor_valor = lista_heap[tamanho//2]
            for i in range((tamanho//2 + 1), tamanho):
                menor_valor = lista_heap[i] if lista_heap[i] < menor_valor else menor_valor
            return menor_valor


sequencia_entrada = input().split()
constante = int(input())

lista_heap = [None]
for numero in sequencia_entrada:
    lista_heap.append(int(numero))

tamanho = len(lista_heap)
rodadas = 0
for i in range((tamanho//2), 0, -1):
    maxheap(i)

while len(lista_heap) > 1:
    maximo = heap_extremo("max")
    minimo = heap_extremo("min")
    k = maximo - abs(minimo * constante)
    if k > 0:
        rodadas += 1
        lista_heap[1] = k
    elif k <= 0:
        rodadas += 1
        lista_heap[0] = None
        remover_maxheap()
        lista_heap = lista_heap[:-1]
    maxheap(1)
print(f'{rodadas} rodadas, partindo para a próxima!')
