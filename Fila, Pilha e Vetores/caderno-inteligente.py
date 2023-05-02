def verificando_itens(item1, item2):
    if item1 in pilha and item2 in pilha:
        index1 = pilha.index(item1)
        index2 = pilha.index(item2)
        if index1 < index2:
            pilha[pilha.index(item1)] = "a"
            pilha[pilha.index(item2)] = "b"
        else:
            return False
    else:
        return False


entrada = input()
pilha = []

for i in entrada:
    pilha.append(i)

while (verificando_itens('F', 'V') != False) and ('F' in pilha) and ('V' in pilha):
    verificando_itens('F', 'V')

if 'F' not in pilha and 'V' not in pilha:
    print("Correto.")
elif 'V' in pilha:
    posicao = pilha.index('V')
    print(f"Incorreto, devido a capa na posição {posicao+1}.")
elif 'F' in pilha:
    posicao = pilha.index('F')
    print(f"Incorreto, devido a capa na posição {posicao+1}.")
