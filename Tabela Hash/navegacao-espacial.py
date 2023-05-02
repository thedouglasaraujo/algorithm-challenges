class NaveEspacial:
    def __init__(self, quantidade_espacos):
        self.quantidade_espacos = quantidade_espacos
        self.dado = [None]*quantidade_espacos

    def add(self, dado_x):
        for i in range(self.quantidade_espacos):
            index = (dado_x + i) % self.quantidade_espacos
            if self.dado[index] == None:
                self.dado[index] = dado_x
                return 'E: ' + str(index)
        return 'Toda memoria utilizada'

    def sch(self, dado_d):
        for i in range(self.quantidade_espacos):
            index = (dado_d + i) % self.quantidade_espacos
            if self.dado[index] == dado_d:
                return 'E: ' + str(index)
            elif self.dado[index] == None:
                return 'NE'
        return 'NE'

    def cap(self, memoria):
        if self.dado[memoria] == None:
            return 'D'
        else:
            return 'A: ' + str(self.dado[memoria])


n = int(input())
c = int(input())
dados = NaveEspacial(n)
for i in range(c):
    operacao, numero = input().split()
    if operacao == 'ADD':
        dado_x = int(numero)
        resultado = dados.add(dado_x)
        if resultado != None:
            print(resultado)
    elif operacao == 'SCH':
        dado_d = int(numero)
        resultado = dados.sch(dado_d)
        if resultado != None:
            print(resultado)
    elif operacao == 'CAP':
        memoria = int(numero)
        resultado = dados.cap(memoria)
        if resultado != None:
            print(resultado)
