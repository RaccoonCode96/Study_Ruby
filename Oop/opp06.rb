# get, set을 사용하는 이유

class Cal
    def initialize(v1,v2) 
        # p v1, v2
        @v1 = v1
        @v2 = v2           
    end
    def add()      
        return @v1+@v2
    end
    def subtract()
        return @v1-@v2
    end
    def setV1(v)
        if v.is_a?(Integer) # v.is_a? : v에 담겨 있는 어떤 인스턴스가 integer 인지?
        @v1 = v
        end
    end
    def getV1()
        return @v1
    end
end

c1 = Cal.new(10,10)
p c1.add() 
p c1.subtract()
c1.setV1(20)
p c1.add() 
c1.setV1('one')
p c1.add() 
