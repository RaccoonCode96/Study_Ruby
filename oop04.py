class C:
    def __init__(self, v):
        self.value = v

    def show(self):
        print(self.value)


c1 = C(10)
print(c1.value)  # c1에 소속된 value라고 하는 인스턴스 변수의 값을 읽어와 -> 인스턴스 변수에 접근을 허용함
c1.value = 20  # 읽어 왔으면 쓰기도 가능함
print(c1.value)
c1.show()  # 메서드 안에서 지정하여 밖에서는 메서드를 통해서 접근하는것도 가능
