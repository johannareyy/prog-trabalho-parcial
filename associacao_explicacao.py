class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addNums(self):
        self.a + self.b

class B(object):
    def __init__(self, c, d):
        self.c = c
        self.d = d

    def addAllNums(self, Aa, Ab):
        x = self.c + self.d + Aa + Ab
        return x

objetoa = A(2, 6)
objetob = B(5, 9)

print (objetob.addAllNums(objetoa.a, objetoa.b))