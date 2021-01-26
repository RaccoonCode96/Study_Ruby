# set, get메서드

class C:
    def __init__(self, v):
        self.value = v

    def show(self):
        print(self.value)

    def getValue(self):
        return self.value

    def setValue(self, v):
        self.value = v


c1 = C(10)
print(c1.getValue())
c1.setValue(20)
print(c1.getValue())


# 직접 읽고 쓰고도 가능하고 메서드를 지정하는 방식으로 인스턴스변수를 가져오고 쓰기도 가능
# getValue , setValue 네임들은 보통 관습적으로 이렇게 사용하여 통일함 -> 네이밍컨벤션
# 굳이 파이썬은 이렇게 지정안하고도 할수 있는데 왜 하는가?
