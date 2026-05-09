# O'zgaruvchilar, Tiplar va Xotira

class Xotira:
    def __init__(self, nom, qiymat):
        self.nom = nom
        self.qiymat = qiymat

    def o'zgartir(self, yangi_qiymat):
        self.qiymat = yangi_qiymat

    def o'qish(self):
        return self.qiymat

class O'zgaruvchi:
    def __init__(self, nom, qiymat, xotira):
        self.nom = nom
        self.qiymat = qiymat
        self.xotira = xotira

    def o'zgartir(self, yangi_qiymat):
        self.xotira.o'zgartir(yangi_qiymat)
        self.qiymat = yangi_qiymat

    def o'qish(self):
        return self.xotira.o'qish()

class Tiplar:
    def __init__(self):
        self.int = 0
        self.float = 0.0
        self.str = ""

    def o'zgartir_int(self, qiymat):
        self.int = qiymat

    def o'zgartir_float(self, qiymat):
        self.float = qiymat

    def o'zgartir_str(self, qiymat):
        self.str = qiymat

    def o'qish_int(self):
        return self.int

    def o'qish_float(self):
        return self.float

    def o'qish_str(self):
        return self.str

# Test qismi
xotira = Xotira("Xotira", 10)
o'zgaruvchi = O'zgaruvchi("O'zgaruvchi", 10, xotira)
tip = Tiplar()

print(o'zgaruvchi.o'qish())  # 10
print(tip.o'qish_int())  # 0
print(tip.o'qish_float())  # 0.0
print(tip.o'qish_str())  # ""

o'zgaruvchi.o'zgartir(20)
print(o'zgaruvchi.o'qish())  # 20

tip.o'zgartir_int(30)
print(tip.o'qish_int())  # 30

tip.o'zgartir_float(40.5)
print(tip.o'qish_float())  # 40.5

tip.o'zgartir_str("Hello, World!")
print(tip.o'qish_str())  # Hello, World!
