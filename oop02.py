# 클래스 만들기
# 계산기 만들기
# 2. 클래스 만들어보기
class Cal(object):
    def __init__(self, v1, v2):
        print(v1, v2)
        self.v1 = v1
        # 첫번째 매개변수를 꼭 정의해야함(뭐가 되든 상관 없고) python에서 는 @가 self이고 인스턴스가 self로 들어옴
        self.v2 = v2

    def add(self):          # 메소드 첫번째 인자가 인스턴스를 가르킴
        return self.v1+self.v2

    def subtract(self):
        return self.v1-self.v2


# 1. 클래스 사용해보기
c1 = Cal(10, 10)
# Cal이라는 클래스를 복제한 인스턴스를 return해주는 역할 -> c1에 담아서 c1을 통해 인스턴스를 가르킬수 있음
print(c1.add())  # 10 ,10 더한 결과 리턴
print(c1.subtract())  # 10 ,19 을 뺀 결과 리턴

c2 = Cal(30, 20)
print(c2.add())
print(c2.subtract())
