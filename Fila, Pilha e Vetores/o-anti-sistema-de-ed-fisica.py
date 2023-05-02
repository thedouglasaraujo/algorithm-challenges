def pilhaImaculada(pilha):
    for i in range(len(pilha) - 1):
        if int(pilha[i]) > int(pilha[i + 1]):
            return False
    return True

def novaLocacao(pilha, codigo):
    if pilhaImaculada(pilha) == True:
        for i in range(len(pilha)):
            if int(pilha[i]) >= codigo:
                pilha.insert(i, str(codigo))
                break
        return pilha
    else:
        return "A pilha está um caos."

pilha = input().split(",")
codigo = int(input())
saida = novaLocacao(pilha, codigo)
print(saida)