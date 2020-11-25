class Construtor():
    def __init__(self, param = ''):
        self.param = param
class Destrutor():
    def __del__(self):
        print('Destruido')

cons = Construtor()
print(f'cons.param = {cons.param}')
cons2 = Construtor('Parametro')
print(f'cons2.param = {cons2.param}')
del cons
# print(cons)
dest = Destrutor()
del dest

