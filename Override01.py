# 오버 라이딩 (overriding)
# 부모 객체와 자식객체의 기능이름이 같은 경우 자식 객체의 기능이 우선되어 지는 것 -> 기능이 올라 탔다. -> 오버 라이딩

class C1:
    def m(self):
        return 'parent'


class C2(C1):
    # pass  # 메서드가 존재하지 않는 클래스로 만들기 가능
    def m(self):  # 부모와 같이 만들어서 재정의 -> 오버라이딩
        # super().m()  # 원래의 부모의 메서드를 사용하고 싶을때
        return super().m() + ' child'


o = C2()
print(o.m())
