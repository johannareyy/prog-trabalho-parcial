#criando um objeto
class Teste0:
    x = 2
    y = 3


#criando um objeto dinamicamente (recebe seus atributos depois)
class Teste:        #primeira letra maiúscula
    def reset(self): #self é para relacionar o metodo com o objeto (obrigatório)
        self.x = 0
        self.y = 0

#ou pode ser tbm
# class Teste:
#     pass             #pass serve só para informar que pode seguir enfrente pq é uma classe vazia

ob1 = Teste()
ob1.x = 2
ob1.y = 3
ob1.nome = "Fui inserido"

print(ob1.x + ob1.y)
ob1.reset()
print(ob1.x + ob1.y)
print(ob1.nome)

#Construtores (N mt utilizado)
#outra forma de criar um objeto
class Cons:
    def __init__(self, x = 0, y = 0): #serve para iniciar com algum valor em certas variaveis pré-definidas no metodo
        self.move(x, y)
    
    def __del__(self):
        print('destructor')

    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0, 0)

cons = Cons(2, 4)
print(cons.x, cons.y)
del cons
#print(cons.x, cons.y) #é pra dar erro por ter apagado o obj

#Sobrecarga de Operadores
'''
class Sobrecarga():         #comentei tudo pq precisa fazer um exemplo para dar certo, isso é só a estrutura básica
    def __add__(self, c): # +
        #aqui dentro programa o significado que vc quer de somar algo.

    def __sub__(self, c): # -
        #aqui dentro programa o significado que vc quer de subtrair algo.
        
    def __mul__(self, c): # *
        #aqui dentro programa o significado que vc quer de multiplicar algo.
        
'''

#Heranca Simples
class Veiculo(object):
    estado = 'novo'

class Carro(Veiculo): #herdando estado do objeto pai (Veiculo).
    def dirigir(self):
        self.estado = "usado"

bmw = Carro()
print(bmw.estado) #bmw começa com o estado do objeto pai.
bmw.dirigir()
print(bmw.estado)   #após o método dirigir, muda seu estado.

#só outro exemplo de criar um objeto dinamicamente
class InsAberta():
    pass
novo = InsAberta()
novo.atributo = 'novo' # classes conseguem receber propriedade dinamicamente por isso é util poder fazer uma classe vazia

#Herança Múltipla
class English(object):
    def greet(self):
        print('Hi!')

class Portuguese(object):
    def greet(self):
        print('Oi!')

class Bilingual(English, Portuguese): #capacidade de herdar de mais de uma classe, seleciona propriedade da esquerda para a direita.
    pass

Bilingual().greet()                 #desse modo só imprime, n cria nenhum objeto

bilingue = Bilingual()              #criei um objeto para armazenar um valor
bilingue.teste = 'teste'
print (bilingue.teste)

#Polimorfismo
#super()
class Pai(object):
    x = 0
    def __init__(self):
        print('Construindo a classe Pai')
        self.x = 2

class Mae(object):
    def __init__(self):
        print('Construindo a classe Mãe')

    
class Filha(Pai):               #trocar Pai por Mae e testar
    def __init__(self):
        super().__init__()      #herda o construtor do pai ou métodos
    def move(self):
        super().move

filha = Filha()