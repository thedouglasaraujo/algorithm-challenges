class NaveEspacial:
    def __init__(self, quantidade_espacos):
        self.quantidade_espacos = quantidade_espacos
        self.dado = [None]*quantidade_espacos

    def add(self, dado_x):
        for i in range(self.quantidade_espacos):
            index = (dado_x + i) % self.quantidade_espacos
            if self.dado[index] == None:
                self.dado[index] = dado_x
                print(f'E: {index}')
                return
        print('Toda memoria utilizada')

    def sch(self, dado_d):
        for i in range(self.quantidade_espacos):
            index = (dado_d + i) % self.quantidade_espacos
            if self.dado[index] == dado_d:
                print(f'E: {index}')
                return
            elif self.dado[index] == None:
                print('NE')
                return
        print('NE')

    def cap(self, memoria):
        if self.dado[memoria] == None:
            print('D')
        else:
            print(f'A: {self.dado[memoria]}')
            
n = int(input())
c = int(input())
dados = NaveEspacial(n)
for i in range(c):
    operacao, numero = input().split()
    if operacao == 'ADD':
        dado_x = int(numero)
        dados.add(dado_x)
    elif operacao == 'SCH':
        dado_d = int(numero)
        dados.sch(dado_d)
    elif operacao == 'CAP':
        memoria = int(numero)
        dados.cap(memoria)