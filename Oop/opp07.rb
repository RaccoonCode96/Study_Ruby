# Ruby와 python의 속성
# 루비와 파이썬 특성에 따른 인스턴스 변수의 접근에 대한 반대 방법 
# set, get 메서드 없이도 error없이 실행 가능할 것인가?
# 필요에 의해서 set,get 써도 좋지만 속성을 통해서 외부에서 인스턴스 변수에 접근 가능하다. 

class C
    # attr_reader :value # value라는 인스턴스 변수를 읽기 가능한 속성으로 지정하겠다.(읽기 가능하게만 함)
    # attr_writer :value # 쓰기 가능한 속성으로 지정함
    attr_accessor :value # accessor 는 읽기과 쓰기 모두 가능하게 해줌  
    def initialize(v)
        @value = v
    end
    def show()
        p @value
    end
end

c1 = C.new(10)
p c1.value() # 외부에서 접근하는 인스턴스 변수인 value는 속성, attribute 이다.
c1.value = 20 # 속성읽기 가능만으로는 실행이 불가함(attr_writer)
p c1.value()


# 루비에서 읽기와 쓰기에서 나누어 놨을까? -> 읽기 전용데이터로 사용하게 하고 싶은 경우가 있어서