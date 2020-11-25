class Construtor():
    def __init__(self, param = ''):
        self.param = param
class Destrutor():
    def __del__(self):
        print('Exemplo')

cons = Construtor()
# print(f'cons.picareta = {cons.picareta}')
cons2 = Construtor('Parametro')
# print(f'cons2.picareta = {cons2.picareta}')
del cons
# print(cons)
dest = Destrutor()
del dest

