class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.esquerdo = None
        self.direito = None
        self.pai = None


class Arvore:
    def __init__(self):
        self.raiz = None

    def add(self, dado):
        if self.raiz is None:
            self.raiz = No(dado)
            print("0")
        else:
            nivel = self.adicionar_na_posicao(self.raiz, dado, 1)
            print(nivel - 1)

    def adicionar_na_posicao(self, no_atual, dado, nivel):
        if dado < no_atual.dado:
            if no_atual.esquerdo == None:
                no_atual.esquerdo = No(dado)
                no_atual.esquerdo.pai = no_atual
                return nivel + 1
            else:
                return self.adicionar_na_posicao(no_atual.esquerdo, dado, nivel + 1)
        elif dado > no_atual.dado:
            if no_atual.direito == None:
                no_atual.direito = No(dado)
                no_atual.direito.pai = no_atual
                return nivel + 1
            else:
                return self.adicionar_na_posicao(no_atual.direito, dado, nivel + 1)
        else:
            return nivel

    def nivel_no(self, no, nivel):
        if no == None:
            return 0
        if no.pai == None:
            return nivel-1
        return self.nivel_no(no.pai, nivel + 1)

    def buscar(self, dado):
        no_atual = self.raiz
        while no_atual != None:
            if no_atual.dado == dado:
                return no_atual
            elif dado < no_atual.dado:
                no_atual = no_atual.esquerdo
            else:
                no_atual = no_atual.direito
        return None

    def rotacionar_direita(self, no):
        pai = no.pai
        esquerdo = no.esquerdo
        no.esquerdo = esquerdo.direito
        if no.esquerdo != None:
            no.esquerdo.pai = no
        esquerdo.direito = no
        no.pai = esquerdo
        esquerdo.pai = pai
        if pai != None:
            if pai.esquerdo == no:
                pai.esquerdo = esquerdo
            else:
                pai.direito = esquerdo
        else:
            self.raiz = esquerdo

    def rotacionar_esquerda(self, no):
        pai = no.pai
        direito = no.direito
        no.direito = direito.esquerdo
        if no.direito != None:
            no.direito.pai = no
        direito.esquerdo = no
        no.pai = direito
        direito.pai = pai
        if pai != None:
            if pai.esquerdo == no:
                pai.esquerdo = direito
            else:
                pai.direito = direito
        else:
            self.raiz = direito

    def atualizar_nivel(self, no, nivel):
        if no != None:
            self.atualizar_nivel(no.esquerdo, nivel+1)
            self.atualizar_nivel(no.direito, nivel+1)
            no.nivel = nivel

    def mover_para_topo(self, no):
        if no.pai == None:
            return '0'
        elif no == self.raiz:
            return '0'
        while no.pai:
            if no.pai.esquerdo == no:
                self.rotacionar_direita(no.pai)
            else:
                self.rotacionar_esquerda(no.pai)
            if no.pai == None:
                self.raiz = no
        self.atualizar_nivel(self.raiz, 1)
        return self.nivel_no(no, 1)


busca_binaria = Arvore()
while True:
    try:
        comando, dado = input().split()
        if comando == 'ADD':
            no = No(int(dado))
            busca_binaria.add(int(dado))
        elif comando == 'SCH':
            no = busca_binaria.buscar(int(dado))
            if no is not None:
                nivel_antes_mover = busca_binaria.nivel_no(no, 1)
                print(nivel_antes_mover)
                busca_binaria.mover_para_topo(no)
            if no is None:
                print('-1')
    except EOFError:
        break
