class Tabela:
    def __init__(self):
        self.tabela = [None] * 11

    def hashing(self, chave):
        return int(chave) % 11

    def add(self, chave):
        i = self.hashing(chave)
        if self.tabela[i] == None:
            self.tabela[i] = [chave]
        else:
            self.tabela[i].append(chave)

    def get(self, chave):
        index = self.hashing(chave)
        if self.tabela[index] != None:
            return self.tabela[index]
        else:
            return []


def cafe_pass(cpf, numero_aleatorio):
    digitos_multiplicados = [int(digito) * 10 for digito in cpf]
    tabela_hash = Tabela()

    for numero in digitos_multiplicados:
        tabela_hash.add(numero)

    for chave in range(11):
        if tabela_hash.tabela[chave] != None:
            if len(tabela_hash.tabela[chave]) == 1:
                continue
            else:
                multiplicacao = tabela_hash.tabela[chave][0] * \
                    len(tabela_hash.get(chave))
                tabela_hash.tabela[chave] = [multiplicacao]

    numeros_verificados = []
    for i in range(11):
        if tabela_hash.tabela[i] != None:
            if numero_aleatorio - tabela_hash.tabela[i][0] in numeros_verificados:
                return "UP Permission"
            if tabela_hash.tabela[i][0] not in numeros_verificados:
                numeros_verificados.append(tabela_hash.tabela[i][0])
    return "NOT Permission"


n = int(input())
for i in range(n):
    cpf, numero_aleatorio = input().split()
    print(cafe_pass(cpf, int(numero_aleatorio)))
