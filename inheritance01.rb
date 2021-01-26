# 상속
# 상속은 객체의 기능을 그대로 가져와서 기능을 추가하는 느낌

# 상속 구현

class Class1
    def method1()
        return 'm1'
    end
end

c1 = Class1.new()
p c1, c1.method1()

class Class3 < Class1 # < 기호를 통해서 Class3는 Class1을 상속 받는다. 큰쪽이 부모
    def method2()
        return 'm2'
    end
end

c3 = Class3.new()
p c3, c3.method1()
p c3, c3.method2()

# 중복을 제거하고 부모 클래스의 재사용을 높인다.


