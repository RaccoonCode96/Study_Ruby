# 클래스 안의 클래스 메서드와 변수간에 관계

class Cs:
    count = 0  # 메소드 밖 클래스 안에 정의하면 클래스의 소속인 변수로 인식

    def __init__(self):
        Cs.count += 1  # 메소드 안에서 접근할 때는 Cs.를 붙여야 한다.

    @classmethod
    def getCount(cls):  # cls는 메소드가 소속된 클래스를 나타냄 -> 여기에서는 Cs
        return Cs.count


i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()

print(Cs.getCount())  # getCount 메서드가 인스턴스가 몇개 생성 되었는지 알려줌
