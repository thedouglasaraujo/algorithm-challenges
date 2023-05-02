class No:
  def __init__(self, nome, valor):
    self.nome = nome
    self.valor = valor
    self.proximo = None

class Fila:
  def __init__(self):
    self.primeiro = None
    self.ultimo = None

  def esta_vazia(self):
    return self.primeiro is None

  def inserir(self, nome, valor):
    novo_no = No(nome, valor)
    if self.ultimo:
      self.ultimo.proximo = novo_no
    self.ultimo = novo_no
    if self.esta_vazia():
      self.primeiro = self.ultimo

  def remover(self):
    if self.esta_vazia():
      return None
    no_removido = self.primeiro
    self.primeiro = no_removido.proximo
    if not self.primeiro:
      self.ultimo = None
    return no_removido
    
  def remover_ultimo(self):
    if self.esta_vazia():
      return None
    if self.primeiro == self.ultimo:
      no_removido = self.primeiro
      self.primeiro = None
      self.ultimo = None
      return no_removido
    atual = self.primeiro
    while atual.proximo != self.ultimo:
      atual = atual.proximo
    no_removido = self.ultimo
    atual.proximo = None
    self.ultimo = atual
    return no_removido

fila1 = Fila()
fila2 = Fila()
total1 = 0.0
total2 = 0.0
receber_comando = True

while receber_comando:
  comando = input()

  if comando[0:6] == "ENTROU":
    x, nome, caixa, valor = comando.split()
    caixa = int(caixa)
    valor = float(valor)
    if caixa == 1:
      fila1.inserir(nome, valor)
      print(f"{nome} entrou na fila 1")
    elif caixa == 2:
      fila2.inserir(nome, valor)
      print(f"{nome} entrou na fila 2")

  elif comando[0:7] == "PROXIMO":
    x, caixa = comando.split() 
    caixa = int(caixa)

    if caixa == 2 and fila2.esta_vazia():
      if not fila1.esta_vazia():
          fila2.inserir(fila1.ultimo.nome, fila1.ultimo.valor)
          fila1.remover_ultimo()
              
    elif caixa == 1 and fila1.esta_vazia():
      if not fila2.esta_vazia():
          fila1.inserir(fila2.ultimo.nome, fila2.ultimo.valor)
          fila2.remover_ultimo()
     
    if caixa == 2:
      if not fila2.esta_vazia():
        no_removido = fila2.remover()
        total2 += no_removido.valor
        print(f"{no_removido.nome} foi chamado para o caixa 2")        
    elif caixa == 1:
      if not fila1.esta_vazia():
        no_removido = fila1.remover()
        total1 += no_removido.valor
        print(f"{no_removido.nome} foi chamado para o caixa 1")

  elif comando == "FIM":
    receber_comando = False
    print(f"Caixa 1: R$ {total1:.2f}, Caixa 2: R$ {total2:.2f}")