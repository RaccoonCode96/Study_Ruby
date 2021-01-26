# 계산기 객체를 이용한 상속 활용

class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2

# 상속을 통한 곱하기 나누기 기능 추가


class CalMultiply(Cal):
    def multiply(self):
        return self.v1*self.v2


class CalDivide(CalMultiply):
    def divide(self):
        return self.v1/self.v2


# CalMultiply 클래스에 생성자가 없지만 부모의 Cal클래스의 생성자를 통해서 c1의 인스턴스 변수에 할당이 되어 인스턴스가 됨

c1 = CalMultiply(10, 10)
print(c1.multiply())
print(c1.add())
print(c1.subtract())

c2 = CalDivide(20, 10)
print(c2.multiply())
print(c2.add())
print(c2.subtract())
print(c2.divide())

# 실제로 여러가지 프로그램이 만들어 지다 보면 상속에서 같은 기능들이 발생할 수도 있으며 그런 것들이 충돌하며 모순이 생기도 함
# 그래서 어떤 코딩이 좋은 것인지는 발전하면서 생각해 나가야 함 (너무 많은 지식에 노출되지 않도록 길을 잘 찾아 가야함-> 안그러면 코딩을 못함)
