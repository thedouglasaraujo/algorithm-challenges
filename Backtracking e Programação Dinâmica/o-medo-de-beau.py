def backtrack(numero_inteiro, maneira_separar, separacoes):
    if numero_inteiro == 0:
        separacoes.append(list(maneira_separar))
    else:
        if maneira_separar == []:
            ultimo_elemento = 1
        else:
            ultimo_elemento = maneira_separar[-1]
        for i in range(ultimo_elemento, numero_inteiro+1):
            maneira_separar.append(i)
            backtrack(numero_inteiro-i, maneira_separar, separacoes)
            maneira_separar.pop()


numero_inteiro = int(input())
separacoes = []
maneira_separar = []
backtrack(numero_inteiro, maneira_separar, separacoes)
print(
    f"Uma sessão com {numero_inteiro} pessoas pode ter sua audiência nos seguintes subgrupos:")
for separacao in separacoes:
    print(separacao)
