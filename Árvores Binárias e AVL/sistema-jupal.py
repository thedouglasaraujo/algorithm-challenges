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
        self.atualizar_altura(recursive=False)
        self.atualizar_balanceamento(False)
        
        while self.fator_balanceamento < -1 or self.fator_balanceamento > 1: 
            if self.fator_balanceamento > 1:
                if self.no.esquerdo.fator_balanceamento < 0:
                    self.no.esquerdo.rotacionar_esquerda()
                    self.atualizar_altura()
                    self.atualizar_balanceamento()
                self.rotacionar_direita()
                self.atualizar_altura()
                self.atualizar_balanceamento()
            elif self.fator_balanceamento < -1:
                if self.no.direito.fator_balanceamento > 0:
                    self.no.direito.rotacionar_direita()
                    self.atualizar_altura()
                    self.atualizar_balanceamento()
                self.rotacionar_esquerda()
                self.atualizar_altura()
                self.atualizar_balanceamento()

    def atualizar_altura(self, recursive=True):
        if self.no: 
            if recursive: 
                if self.no.esquerdo: 
                    self.no.esquerdo.atualizar_altura()
                if self.no.direito:
                    self.no.direito.atualizar_altura() 
            self.altura = 1 + max(self.no.esquerdo.altura, self.no.direito.altura)
        else: 
            self.altura = -1

    def atualizar_balanceamento(self, recursive=True):
        if self.no:
            if recursive:
                if self.no.esquerdo:
                    self.no.esquerdo.atualizar_balanceamento()
                if self.no.direito:
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
        subarvore_esquerda = nova_raiz.esquerdo.no
        antiga_raiz = self.no
        self.no = nova_raiz
        antiga_raiz.direito.no = subarvore_esquerda
        nova_raiz.esquerdo.no = antiga_raiz

    def deletar(self, nome):
        if self.no != None:
            if self.no.nome == nome:
                if not self.no.esquerdo.no and not self.no.direito.no:
                    self.no = None
                elif not self.no.esquerdo.no:                
                    self.no = self.no.direito.no
                elif not self.no.direito.no:
                    self.no = self.no.esquerdo.no
                else:
                    successor = self.no.direito.no  
                    while successor and successor.esquerdo.no:
                        successor = successor.esquerdo.no
                    if successor:
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
    
    def no_minimo(self, no=None):
        if not no:
            no = self.no
        if not no.esquerdo.no:
            return no
        return self.no_minimo(no.esquerdo.no)
        
    def minimo(arvore):
        if not arvore.no:
            return None
        return arvore.no_minimo().nome
        
    def no_maximo(self, no=None):
        if not no:
            no = self.no
        if not no.direito.no:
            return no
        return self.no_maximo(no.direito.no)
        
    def maximo(arvore):
        if not arvore.no:
            return None
        return arvore.no_maximo().nome

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

      elif entrada == "ALTURA":
        altura = arvore.altura + 1
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
              if i == tamanho - 1:
                print(no)
              else:
                print(no, end=' ')
              i += 1
        receber_comando = False