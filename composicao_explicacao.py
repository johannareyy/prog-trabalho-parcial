class A(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addNums(self):
        self.a + self.b

class B(object):
    def __init__(self, d, e):
        self.d = d
        self.e = e
        self.A = A(2, 6)

    def addAllNums(self):
        x = self.d + self.e + self.A.a + self.A.b
        return x

objetob = B(5, 9)

print(objetob.addAllNums()) 