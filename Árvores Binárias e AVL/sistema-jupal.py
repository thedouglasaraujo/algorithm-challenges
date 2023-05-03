class No_arvore():
    def __init__(self, nome):
        self.nome = nome
        self.esquerdo = None
        self.direito = None


class Arvore_avl():
    def __init__(self):
        self.no = None
        self.altura = -1
        self.fator_balanceamento = 0

    def imprimir_arvore(self, nivel=0):
        if self.no != None:
            print(f"{self.no.nome}", end="")
            if self.no.esquerdo.no != None or self.no.direito.no != None:
                print(f" ajuda", end="")
                if self.no.esquerdo.no != None:
                    print(f" {self.no.esquerdo.no.nome}", end="")
                if self.no.direito.no != None:
                    print(f" e {self.no.direito.no.nome}", end="")
                print()
                if self.no.esquerdo.no != None:
                    self.no.esquerdo.imprimir_arvore(nivel+1)
                if self.no.direito.no != None:
                    self.no.direito.imprimir_arvore(nivel+1)
            else:
                print(" não ajuda ninguém")

    def imprimir_subarvore(self, no, nivel=0):
        if no != None:
            print(f"{no.nome}", end="")
            if no.esquerdo.no != None or no.direito.no != None:
                print(f" ajuda", end="")
                if no.esquerdo.no != None:
                    print(f" {no.esquerdo.no.nome}", end="")
                if no.direito.no != None:
                    print(f" e {no.direito.no.nome}", end="")
                print()
                if no.esquerdo.no != None:
                    self.imprimir_subarvore(no.esquerdo.no, nivel+1)
                if no.direito.no != None:
                    self.imprimir_subarvore(no.direito.no, nivel+1)
            else:
                print(" não ajuda ninguém")

    def inserir(self, nome):
        n = No_arvore(nome)
        if not self.no:
            self.no = n
            self.no.esquerdo = Arvore_avl()
            self.no.direito = Arvore_avl()
        elif nome < self.no.nome:
            self.no.esquerdo.inserir(nome)
        elif nome > self.no.nome:
            self.no.direito.inserir(nome)
        self.balanceamento()

    def buscar(self, nome):
        if not self.no:
            return None
        elif self.no.nome == nome:
            return self.no
        elif nome < self.no.nome:
            return self.no.esquerdo.buscar(nome)
        else:
            return self.no.direito.buscar(nome)

    def balanceamento(self):
        self.atualizar_altura(recursivo=False)
        self.atualizar_balanceamento(False)
        while self.fator_balanceamento < -1 or self.fator_balanceamento > 1:
            if self.fator_balanceamento > 1:
                if self.no.esquerdo.fator_balanceamento < 0:
                    self.no.esquerdo.rotacionar_esquerda()
                    self.atualizar_altura()
                    self.atualizar_balanceamento()
                self.rotacionar_direita()
                self.atualizar_balanceamento()
                self.atualizar_altura()
            elif self.fator_balanceamento < -1:
                if self.no.direito.fator_balanceamento > 0:
                    self.no.direito.rotacionar_direita()
                    self.atualizar_balanceamento()
                    self.atualizar_altura()
                self.rotacionar_esquerda()
                self.atualizar_altura()
                self.atualizar_balanceamento()

    def atualizar_altura(self, recursivo=True):
        if self.no != None:
            if recursivo == True:
                if self.no.esquerdo != None:
                    self.no.esquerdo.atualizar_altura()
                if self.no.direito != None:
                    self.no.direito.atualizar_altura()
            self.altura = 1 + max(self.no.esquerdo.altura,
                                  self.no.direito.altura)
        else:
            self.altura = -1

    def atualizar_balanceamento(self, recursivo=True):
        if self.no != None:
            if recursivo == True:
                if self.no.esquerdo != None:
                    self.no.esquerdo.atualizar_balanceamento()
                if self.no.direito != None:
                    self.no.direito.atualizar_balanceamento()
            self.fator_balanceamento = self.no.esquerdo.altura - self.no.direito.altura
        else:
            self.fator_balanceamento = 0

    def rotacionar_direita(self):
        nova_raiz = self.no.esquerdo.no
        subarvore_esquerda = nova_raiz.direito.no
        antiga_raiz = self.no
        self.no = nova_raiz
        antiga_raiz.esquerdo.no = subarvore_esquerda
        nova_raiz.direito.no = antiga_raiz

    def rotacionar_esquerda(self):
        nova_raiz = self.no.direito.no
        subarvore_direita = nova_raiz.esquerdo.no
        antiga_raiz = self.no
        self.no = nova_raiz
        antiga_raiz.direito.no = subarvore_direita
        nova_raiz.esquerdo.no = antiga_raiz

    def deletar(self, nome):
        if self.no != None:
            if self.no.nome == nome:
                if self.no.esquerdo.no == None and self.no.direito.no == None:
                    self.no = None
                elif self.no.esquerdo.no == None:
                    self.no = self.no.direito.no
                elif self.no.direito.no == None:
                    self.no = self.no.esquerdo.no
                else:
                    successor = self.no.direito.no
                    while successor != None and successor.esquerdo.no != None:
                        successor = successor.esquerdo.no
                    if successor != None:
                        self.no.nome = successor.nome
                        self.no.direito.deletar(successor.nome)
            elif nome < self.no.nome:
                self.no.esquerdo.deletar(nome)
            elif nome > self.no.nome:
                self.no.direito.deletar(nome)
            self.balanceamento()

    def percorrer(self):
        nos_restantes = []
        if not self.no:
            return nos_restantes
        nos_restantes.extend(self.no.esquerdo.percorrer())
        nos_restantes.append(self.no.nome)
        nos_restantes.extend(self.no.direito.percorrer())
        return nos_restantes

    def minimo(arvore):
        if not arvore.no:
            return None
        no = arvore.no
        while no.esquerdo.no:
            no = no.esquerdo.no
        return no.nome

    def maximo(arvore):
        if not arvore.no:
            return None
        no = arvore.no
        while no.direito.no:
            no = no.direito.no
        return no.nome


arvore = Arvore_avl()
receber_comando = True
while receber_comando == True:
    entrada = input()
    if entrada[0] == "D" or entrada[0] == "I":
        comando, nome = entrada.split()
        if comando == "INSERIR":
            arvore.inserir(nome)
            if arvore.buscar(nome):
                print(f"{nome} INSERIDO")

        elif comando == "DELETAR":
            if arvore.buscar(nome) == None:
                print(f"{nome} NAO ENCONTRADO")
            else:
                arvore.deletar(nome)
                print(f"{nome} DELETADO")

    elif entrada == "VER":
        arvore.imprimir_arvore()

    elif entrada[0:3] == "VER" and len(entrada) > 3:
        comando, nome = entrada.split()
        res = arvore.imprimir_subarvore(arvore.buscar(nome))

    elif entrada == "ALTURA":
        altura = arvore.altura+1
        print(f'ALTURA: {altura}')

    elif entrada == "MINIMO":
        minimo = arvore.minimo()
        if minimo == None:
            print("ARVORE VAZIA")
        else:
            print(f'MENOR: {minimo}')

    elif entrada == "MAXIMO":
        maximo = arvore.maximo()
        if maximo == None:
            print("ARVORE VAZIA")
        else:
            print(f'MAIOR: {maximo}')

    elif entrada == "FIM":
        nos_restantes = arvore.percorrer()
        tamanho = len(nos_restantes)
        if tamanho == 0:
            print("ARVORE VAZIA")
        else:
            i = 0
            while i != tamanho:
                for no in nos_restantes:
                    if i == tamanho-1:
                        print(no)
                    else:
                        print(no, end=' ')
                    i += 1
        receber_comando = False
        