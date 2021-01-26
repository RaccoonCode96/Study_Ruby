#  믹스인 mixin
# 객체와 모듈관의 관계, 함수를 어떻게 사용할 것 인가?
# 믹스하고 싶은 함수들을 모듈화 시켜서 다른 클래스에서 include를 통해서 사용 가능하다.

module M1
    def m1_m
        p "m1_m"
    end
end

module M2
    def m2_m
        p "m2_m"
    end
end


class C
    include M1, M2
end

c = C.new()
c.m1_m()
c.m2_m()