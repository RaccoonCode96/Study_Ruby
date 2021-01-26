class Cs:
    @staticmethod  # 위에 장식자 넣어주기 (규칙이므로 꼭 저이름대로 넣어줘야 함)
    def static_method():
        print("Static method")

    @classmethod  # 위에 장식자 넣어주기 (규칙이므로 꼭 저이름대로 넣어줘야 함)
    def class_method(cls):  # self 처럼 클래스 메소드에서는 cls로 첫번째 인자를 줌
        print("Class method")

    def instance_method(self):
        print("instance_method")


i = Cs()
Cs.static_method()  # 클래스 소속이므로 Cs.
Cs.class_method()  # 클래스 소속이므로 Cs.
i.instance_method()  # 인스턴스 소속이므로 i.
# python에서 클래스 멤버에 두가지 종류로 static, class 두가지 임


# Ruby는 클래스 멤버를 구분하기 위해서 '클래스.' 을 붙여주고
# Python 에서는 @staticmethod 나 @classmethod 를 붙여주고 추가적으로 class_method에는 첫번째 인자로 'cls'를 넣어준다
# 둘다 클래스 멤버, 인스턴스 멤버를 사용하는 경우에는 각각에 맞게 똑같이 써준다.
