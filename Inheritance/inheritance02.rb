class Cal
    def initialize(v1,v2) 
        @v1 = v1
        @v2 = v2          
    end
    def add()      
        return @v1+@v2
    end
    def subtract()
        return @v1-@v2
    end
end

class CalMultiply < Cal
    def multiply()
        return @v1*@v2
    end
end

class CalDivide < CalMultiply
    def divide()
        return@v1/@v2
    end
end

c1 = CalMultiply.new(10, 10)
p c1.add()
p c1.multiply()
p c1.subtract()

c2 = CalDivide.new(20, 10)
p c2.add()
p c2.multiply()
p c2.subtract()
p c2.divide()