# set, get메서드

class C
    def initialize(v)
        @value = v
    end
    def show()
        p @value
    end
    def getValue()
        return @value
    end
    def setValue(v)
        @value = v
    end
end

c1 = C.new(10)
# p c1.value()
p c1.getValue()
# p c1.value = 20
c1.setValue(20)
c1.show()

# 직접 읽고 쓰고는 불가능하지만 메서드를 지정하는 방식으로 인스턴스변수를 가져오고 쓰기가 가능
# getValue , setValue 네임들은 보통 관습적으로 이렇게 사용하여 통일함 -> 네이밍컨벤션