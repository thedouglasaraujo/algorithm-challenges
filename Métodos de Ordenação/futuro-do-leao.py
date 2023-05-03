def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerdo = merge_sort(lista[:meio])
    direito = merge_sort(lista[meio:])
    cont1 = 0
    cont2 = 0
    listas_juntas = []
    while cont1 < len(esquerdo) and cont2 < len(direito):
        if esquerdo[cont1] < direito[cont2]:
            listas_juntas.append(esquerdo[cont1])
            cont1 += 1
        else:
            listas_juntas.append(direito[cont2])
            cont2 += 1
    listas_juntas += esquerdo[cont1:]
    listas_juntas += direito[cont2:]
    return listas_juntas


def mediana(sport, future_club):
    lista_ordenada = merge_sort([int(x) for x in sport + future_club])
    tamanho = len(lista_ordenada)
    meio = tamanho // 2
    if tamanho % 2 == 0:
        mediana = (lista_ordenada[meio-1] + lista_ordenada[meio]) / 2
        return f"{mediana:.2f}"
    else:
        mediana = lista_ordenada[meio]
        return f"{mediana:.2f}"


salario_sport = input().split()
salario_novo_clube = input().split()
mediana = mediana(salario_sport, salario_novo_clube)
print(
    f"O salário sugerido por Juba na primeira negociação será de {mediana} mil reais.")
