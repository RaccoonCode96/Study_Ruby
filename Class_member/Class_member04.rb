# 계산기 예제를 통한 클래스 맴버 활용
# 각 인스턴스에 따른 히스토리 보기 기능

class Cal
    @@_history = []  # 배열을 만듦
    def initialize(v1,v2) 
        @v1 = v1
        @v2 = v2          
    end
    def add()
        result = @v1+@v2 
        @@_history.push("add : #{@v1}+#{@v2}=#{result}") # push는 배열에 끝 부분에 값을 추가해줌 
        # 루비에서 타입 변형을 하려면 result.to_s()를 해줘야 하는데 더 쉽게
        # 루비에서의 포맷팅 방법  #{변수} 로 가능   
        return result
    end
    def subtract()
        result = @v1-@v2 
        @@_history.push("subtract : #{@v1}-#{@v2}=#{result}")
        return result
    end
    def Cal.history() # 히스토리 클래스 
        for item in @@_history # 반복해서 뽑아서 보여줌
            p item
        end
    end
end

class CalMultiply < Cal
    def multiply()
        result = @v1*@v2 
        @@_history.push("multiply : #{@v1}*#{@v2}=#{result}")
        return result
    end
end

class CalDivide < CalMultiply
    def divide()
        result = @v1/@v2 
        @@_history.push("divide : #{@v1}/#{@v2}=#{result}")
        return result
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

p Cal.history()