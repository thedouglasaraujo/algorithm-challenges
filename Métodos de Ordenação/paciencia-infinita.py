def bubble_sort(lista, numero=-1):
    tamanho = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(tamanho):
        for j in range(tamanho-i-1):
            comparacoes += 1
            if numero != -1 and trocas+comparacoes == numero:
                return lista
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocas += 1
                if numero != -1 and trocas+comparacoes == numero:
                    return lista
    return comparacoes, trocas, lista


def selection_sort(lista, numero=-1):
    tamanho = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(tamanho):
        menor_elemento = i
        for j in range(i+1, tamanho):
            comparacoes += 1
            if numero != -1 and trocas+comparacoes == numero:
                return lista
            if lista[j] < lista[menor_elemento]:
                menor_elemento = j
        if menor_elemento != i:
            lista[i], lista[menor_elemento] = lista[menor_elemento], lista[i]
            trocas += 1
            if numero != -1 and trocas+comparacoes == numero:
                return lista
    return comparacoes, trocas


def insertion_sort(lista, numero=-1):
    tamanho = len(lista)
    comparacoes = 0
    trocas = 0
    for i in range(1, tamanho):
        current = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > current:
            comparacoes += 1
            if numero != -1 and trocas+comparacoes == numero:
                return lista
            lista[j+1] = lista[j]
            j -= 1
            trocas += 1
            if numero != -1 and trocas+comparacoes == numero:
                return lista
        if j != i-1:
            lista[j + 1] = current
            if numero != -1 and trocas+comparacoes == numero:
                return lista
        if j >= 0:
            comparacoes += 1
            if numero != -1 and trocas+comparacoes == numero:
                return lista
    return comparacoes, trocas


def shell_sort(lista, numero=-1):
    tamanho = len(lista)
    comparacoes = 0
    trocas = 0
    gap = tamanho//2
    while gap > 0:
        for i in range(gap, tamanho):
            temp = lista[i]
            j = i
            while j >= gap and lista[j-gap] > temp:
                comparacoes += 1
                if numero != -1 and trocas+comparacoes == numero:
                    return lista
                lista[j] = lista[j-gap]
                j -= gap
                trocas += 1
                if numero != -1 and trocas+comparacoes == numero:
                    return lista
            lista[j] = temp
            if j >= gap:
                comparacoes += 1
            if numero != -1 and trocas+comparacoes == numero:
                return lista
        gap //= 2
    return comparacoes, trocas, lista


def quick_sort(A, lo, hi, comparacoes=0, trocas=0):
    if lo >= 0 and hi >= 0 and lo < hi:
        p, comparacoes, trocas = partition(A, lo, hi, comparacoes, trocas)
        comparacoes, trocas = quick_sort(A, lo, p, comparacoes, trocas)
        comparacoes, trocas = quick_sort(A, p + 1, hi, comparacoes, trocas)
    return comparacoes, trocas


def partition(A, lo, hi, comparacoes=0, trocas=0):
    pivot = A[(hi + lo) // 2]
    i = lo
    j = hi
    while True:
        if i >= j:
            return j, comparacoes, trocas
        while A[i] < pivot:
            comparacoes += 1
            i += 1
        while A[j] > pivot:
            comparacoes += 1
            j -= 1
        trocas += 1
        A[i], A[j] = A[j], A[i]


lista = []

sequencia = input().split()
for numero in sequencia:
    lista.append(int(numero))

metodos = []
metodos.append(['Caça-Rato', bubble_sort(lista.copy())])
metodos.append(['Grafite', selection_sort(lista.copy())])
metodos.append(['Lacraia', insertion_sort(lista.copy())])
metodos.append(['Rivaldo', shell_sort(lista.copy())])
metodos.append(['Toninho', quick_sort(lista.copy(), 0, len(lista.copy()) - 1)])

somas = []
for i in metodos:
    print(f"{i[0]} ordena a lista com {i[1][0]} comparações e {i[1][1]} trocas.")
    somas.append(i[1][0] + i[1][1])

print("-VENCEDOR DA RODADA-")
minimo = min(somas)
indice = somas.index(minimo)
bubble = bubble_sort(lista.copy(), minimo)
insertion = insertion_sort(lista.copy(), minimo)
selection = selection_sort(lista.copy(), minimo)
shell = shell_sort(lista.copy(), minimo)
print(f"O vencedor da rodada é {metodos[indice][0]}, com {minimo} ações.")
print("-Toninho está a dormir...-")
print("Os outros estagiários retornam as seguintes listas com essa quantidade de ações:")
if metodos[indice][0] != "Caça-Rato":
    print(f"Com {minimo} ações, Caça-Rato ordena a lista assim: {bubble}")
if metodos[indice][0] != "Grafite":
    print(f"Com {minimo} ações, Grafite ordena a lista assim: {selection}")
if metodos[indice][0] != "Lacraia":
    print(f"Com {minimo} ações, Lacraia ordena a lista assim: {insertion}")
if metodos[indice][0] != "Rivaldo":
    print(f"Com {minimo} ações, Rivaldo ordena a lista assim: {shell}")
