'''# 1) 
# a) Usando seus conhecimentos atuais em POO, vamos criar uma classe conta com os parâmetros "agencia", "numero" e "saldo"
class conta:
    agencia = ''
    numero = ''
    saldo = 0.0
# b) Agora crie os métodos para saque e depósito na classe conta
#--> MÉTODOS DE INSTÂNCIA (alteram o estado de um objeto)
    #função saque
    def saque(self, valor):
      self.saldo -= valor

    #self significa referência do objeto
    def deposito(self, valor):
        self.saldo += valor

# __init__ --> MÉTODO CONSTRUTOR
class conta:
    def __init__ (self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
    def saque(self, valor):
      self.saldo -= valor
    def deposito(self, valor):
        self.saldo += valor

conta1 = conta(1235, 1216, 400)

print(f"Agência: {conta1.agencia}; Número: {conta1.numero}; Saldo: {conta1.saldo}")


#2) 
#classe carro (deve conter marca, modelo, ano e preço)
#métodos: 
#aumentar preço em 10%
#diminuir preço em 10%
#aumentar preço de acordo com porcentagem informada
#diminuir preço de acordo com porcentagem informada
#após isso, crie um objeto nessa classe e imprima seus dados (PS.: Execute antes do print algum dos métodos listados acima)
#--> usando método construtor:
class carro:
  def __init__(self, marca, modelo, ano, preco):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.preco = preco

  def aum10(self):
    self.preco *= 1.1
  def dim10(self):
    self.preco *= 0.9
  def aumpre(self, valor):
    self.preco *= 1+(valor/100)
  def dimpre(self, valor):
    self.preco *= 1-(valor/100)

carro1 = carro("fiat", "uno", 2010, 1000)
carro1.dim10()
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}\nPreço: {carro1.preco}")

#--> usando listas:
class carro:
    marca = ''
    modelo = ''
    ano = 0
    preco = 0
carro1 = carro()
carro1.marca = "Ford"
carro1.modelo = "Eco Sport"
carro1.ano = 2005
carro1.preco = 80000.0

carro2 = carro()
carro2.marca = "Fiat"
carro2.modelo = "Uno Mille"
carro2.ano = 1999
carro2.preco = 5000.0

carros = []
carros.append(carro1)
carros.append(carro2)

for carro in carros:
    print(carro.marca)
    print(carro.modelo)
    print(carro.ano)
    print(carro.preco)
    print("===============")'''
