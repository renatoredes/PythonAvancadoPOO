# documentação: https://docs.python.org/pt-br/3/tutorial/classes.html#:~:text=class%20MyClass%3A%0A%20%20%20%20%22%22%22A%20simple%20example%20class%22%22%22%0A%20%20%20%20i%20%3D%2012345%0A%0A%20%20%20%20def%20f(self)%3A%0A%20%20%20%20%20%20%20%20return%20%27hello%20world%27

'''
Exemplo de classe em Python

1. Classe
2. Construtor (__init__)
3. Método acelerar
4. Método frear
5. Objetos (carro1 e carro2)

Observações: Todo Método começa com a palavra self 
Em Python, self é uma convenção para o primeiro parâmetro em métodos de uma 
classe. Não é uma palavra-chave, mas é comumente utilizada para representar a 
instância da própria classe. Ele permite o acesso aos atributos e métodos da instância, 
facilitando a manipulação interna de seus membros.
'''


class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"{self.modelo} acelerando. Velocidade atual: {
              self.velocidade} km/h")

    def frear(self, decremento):
        self.velocidade -= decremento
        print(f"{self.modelo} freando. Velocidade atual: {
              self.velocidade} km/h")


# Criando objetos da classe Carro
carro1 = Carro(modelo="Fusca", cor="Azul")
carro2 = Carro(modelo="Civic", cor="Prata")
carro3 = Carro(modelo="Fiat Toro", cor="Branca")

# Utilizando métodos dos objetos
carro1.acelerar(20)
carro2.acelerar(15)
carro3.acelerar(50)

carro1.frear(5)
carro2.frear(10)
carro3.frear(35)

# Explicação: Construtor
'''
O construtor é chamado quando um novo objeto da classe é criado. Ele inicializa os atributos 
modelo, cor e velocidade.

Construtor (__init__):

def __init__(self, modelo, cor):
    self.modelo = modelo
    self.cor = cor
    self.velocidade = 0

'''

# Explicação: Método acelerar

'''
O método acelerar recebe um incremento e atualiza a velocidade do carro. 
Uma mensagem é impressa indicando a aceleração.

def acelerar(self, incremento):
    self.velocidade += incremento
    print(f"{self.modelo} acelerando. Velocidade atual: {self.velocidade} km/h")
'''

# Explicação: Método frear

'''
O método frear recebe um decremento e atualiza a velocidade do carro.
Uma mensagem é impressa indicando a frenagem.

def frear(self, decremento):
    self.velocidade -= decremento
    print(f"{self.modelo} freando. Velocidade atual: {self.velocidade} km/h")

'''

# Objetos (carro1 e carro2):

'''
Os objetos carro1 e carro2 são instâncias da classe Carro. Eles são criados utilizando
o construtor da classe com argumentos específicos.
Estes são os principais elementos da classe Carro
desempenha um papel específico na definição da classe e na criação de objetos.

carro1 = Carro(modelo="Fusca", cor="Azul")
carro2 = Carro(modelo="Civic", cor="Prata")

'''
# Explicação Incremento e Decremento += e -=
'''
+= e -=
São operadores de atribuição combinada em Python. Eles são utilizados para 
atualizar o valor de uma variável de forma concisa.

1. += Atribuição de Adição
Exemplo: a += b é equivalente a a = a + b.

2. -= Atribuição de Subtração
Exemplo: a -= b é equivalente a a = a - b.

Eles são uteis quando você deseja modificar o valor de uma variável 
com base em seu valor atual, Exemplo:

a = 10
b = 5

# Usando +=
a += b  # Agora, a é 15 (10 + 5)

# Usando -=
a -= 3  # Agora, a é 12 (15 - 3)

'''
