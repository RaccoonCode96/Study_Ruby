# get, set을 사용하는 이유

class Cal(object):
    def __init__(self, v1, v2):  # 생성자에 유입되는 값도 미리 방지
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2

    def add(self):
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2

    def setV1(self, v):
        if isinstance(v, int):  # isinstance : 첫번째 인자가 두번째 인자의 인스턴스라면 true를 아니면 false를 return
            self.v1 = v  # false가 되면서 실행이 되지 않고 패스 -> 방지 가능

    def getV1(self):
        return self.v1


c1 = Cal(10, 10)
print(c1.add())
print(c1.subtract())
# c1.v1 = 'one'
# c1.v2 = 30
c1.setV1 = 'one'
c1.getV1 = 30
print(c1.add())  # type 오류가 난다. 문자와 숫사 합이 안됨
print(c1.subtract())
# 입력값이 숫자이길 바람 -> 하지만 입력자는 그걸 모르고 언제든지 문자를 기입가능함 -> 중대한 문제가 생김
