# 계산기 예제에 다중상속 활용

class CalMultiply():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def multiply(self):
        return self.v1*self.v2


class CalDivide():
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def divide(self):
        return self.v1/self.v2


class Cal(CalMultiply, CalDivide):

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2


c = Cal(100, 10)
print(c.add())
print(c.divide())
print(c.multiply())
