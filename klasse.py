import math
class Mathe:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def pytagoras(self):
        return math.sqrt(self.a**2 + self.b**2) 
    def summe(self):
        return self.a + self.b

mathe1 = Mathe(3,4)
print(mathe1.pytagoras())
print(mathe1.summe())

mathe2 = Mathe(2,3)
print(mathe2.pytagoras())
print(mathe2.summe())
