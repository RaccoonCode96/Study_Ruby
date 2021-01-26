# 클래스 안의 클래스 메서드와 변수간에 관계

class Cs
    @@count = 0 # 기준이 될수 있는 최초값 설정
    def initialize()
        # @count # 인스턴스 변수 사용
        @@count += 1 # 클래스 변수 사용시 (initaialize를 실행시킬때 마다 @@count 변수를 1씩 증가 시킴)
    end
    def Cs.getCount() # 클래스 변수를
        return @@count
    end
end

i1 = Cs.new()
i2 = Cs.new()
i3 = Cs.new()
i4 = Cs.new()

p Cs.getCount() # getCount 메서드가 인스턴스가 몇개 생성 되었는지 알려줌
