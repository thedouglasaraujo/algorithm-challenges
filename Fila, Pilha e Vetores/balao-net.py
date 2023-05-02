class No:
    def __init__(self, elemento, anterior, proximo):
        self.elemento = elemento
        self.anterior = anterior
        self.proximo = proximo

class Lista:
    def __init__(self):
        self.no_inicial = None
        self.no_final = None
        
    def add(self, elemento):
        novo_no = No(elemento, None, None)
        if self.no_inicial == None:
            self.no_inicial = self.no_final = novo_no
        else:
            novo_no.proximo = self.no_inicial
            self.no_inicial.anterior = novo_no
            self.no_inicial = novo_no

    def rem(self, elemento):
        no_atual = self.no_inicial
        while no_atual != None:
            if no_atual.elemento == elemento:
                if no_atual == self.no_inicial:
                    self.no_inicial = no_atual.proximo
                if no_atual == self.no_final:
                    self.no_final = no_atual.anterior
                if no_atual.anterior:
                    no_atual.anterior.proximo = no_atual.proximo
                if no_atual.proximo:
                    no_atual.proximo.anterior = no_atual.anterior
                break
            no_atual = no_atual.proximo
    
    def find(self, elemento):
        no_atual = self.no_inicial
        if no_atual.elemento != elemento:
          while no_atual != None:
              if no_atual.elemento == elemento:
                  if no_atual == self.no_final:
                      self.no_final = no_atual.anterior
                  if no_atual.anterior:
                      no_atual.anterior.proximo = no_atual.proximo
                  if no_atual.proximo:
                      no_atual.proximo.anterior = no_atual.anterior
                  no_atual.proximo = self.no_inicial
                  self.no_inicial.anterior = no_atual
                  self.no_inicial = no_atual
                  break
              no_atual = no_atual.proximo
    
    def exib(self):
        no_atual = self.no_inicial
        while no_atual:
            print(no_atual.elemento)
            no_atual = no_atual.proximo

historico = Lista()
run =  True
while run == True:
    comando = input().split()
    if comando[0] == "ADD":
        historico.add(comando[1])
    elif comando[0] == "REM":
        historico.rem(comando[1])
    elif comando[0] == "FIND":
        historico.find(comando[1])
    elif comando[0] == "EXIB":
        historico.exib()
    elif comando[0] == "END":
        run = False
