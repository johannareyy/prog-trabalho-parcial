class Pessoa():
    def __init__(self, nome = '', idade = 0, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return
        if self.falando:
            print(f'{self.nome} jã está falando.')
            return
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def __del__(self):
        print("A Pessoa foi destruida.")

teste = Pessoa('Joãozinho', 20)
teste.comer('maçã')
teste.comer('maçã')
teste.parar_comer()
teste.parar_comer()
teste.comer('maçã')
teste.falar('POO')
