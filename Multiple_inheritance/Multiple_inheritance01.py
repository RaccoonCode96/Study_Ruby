# 다중 상속 (여러 부모의 기능을 상속하여 사용 가능) -> 단, 신중히 사용해야 한다.
# ruby에서는 다중상속을 지원하지 않음 하지만 루비의 mixin 기능으로 대체 가능
# 다중 상속의 문제점 : 두 부모의 메소드 이름이 같으면 어떻게 될까?

class C1():
    def c1_m(self):
        print("c1_m")

    def m(self):
        print("c1 m")


class C2():
    def c2_m(self):
        print("c2_m")

    def m(self):
        print("c2 m")


class C3(C2, C1):
    # def m(self):
    #     print("C3 m")
    pass


c = C3()
c.c1_m()
c.c2_m()
c.m()  # 부모 들이 같은 메소드 이름이 있으면 비슷하게 동작하지만 정확하게 동작하지 않아 심각한 문제 발생할 수 있다.
# 실행 순서는 상속 부모의 기입 순서에 따라 우선순위 적용
print(C3.__mro__)  # C3라는 클래스를 사용할때 우선 순위가 어떻게 되는지 보여줌
