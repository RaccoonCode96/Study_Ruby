class C
    def initialize(v)
        @value = v
    end
    def show()
        p @value
    end
end

c1 = C.new(10)
# p c1.value() # value라는 메소드를 찾기 때문에 error 남 -> 즉, 루비에서 인스턴스 변수에 접근이 불가능 함
# c1.value = 20 # 메소드 밖에서 직접적으로 인스턴스 변수에 접근이 불가능함
c1.show() # 인스턴스 변수에 접근하려면 메서드 안에서 지정하여 밖에서는 메서드를 통해서 접근 가능

