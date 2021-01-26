# Ruby와 python의 속성
# 인스턴스 변수의 접근에 대한

class C:
    def __init__(self, v):
        self.__value = v

    def show(self):
        print(self.__value)


c1 = C(10)
# print(c1.__value)  # python에서는 기본적으로 외부에서 인스턴스 변수에 접근 가능하다.
# 그럼 외부에서 수정 불가능하게 하고 싶은 경우, 숨기고 싶은 변수 이름앞에 __를 붙임
# 외부에서 접근 불가~ (같은 이름으로 불러도 __가 붙으면 인스턴스 외부에서 접근 불가능 함)

c1.show()  # 메소드 안에서는 인스턴스 변수 접근이 가능함
