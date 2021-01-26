class C1
    def m()
        return 'parent'
    end
end

class C2 < C1
    def m()
        return super()+ ' child' 
    end
end

o = C2.new()
p o.m() 
# 파이썬에 super는 부모클래스를 의미하고 
# 루비에 super는 현재 소속되어 있는 함수와 같은 이름을 가진 부모 메소드를 가르킴