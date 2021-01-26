# 클래스 멤버 만들기
class Cs
    def Cs.class_method() # Cs.를 붙여서 Cs라는 클래스의 멤버라는 것을 분명히 해야함
        p 'Class method'
    end
    def instnace_method()
        p 'Instnace_method'
    end
end

i = Cs.new()
Cs.class_method() # class_method()는 Cs라는클래스 소속인 클래스 멤버라는 것임 
i.instnace_method() # instance_method는 i 라는 인스턴스의 소속인 인스턴스 멤버라는 것임
# Cs.instnace_method() # error
# i.class_method() # error
# 클래스와 클래스 메소드의 합으로
# 인스턴스와 인스턴스 메소드의 합으로 구성 해야 한다.