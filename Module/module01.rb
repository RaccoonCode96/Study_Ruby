# 함수
def tom_a()
    return "a"
end

def jerry_a()
    return 'b'
end
# 모듈화
module Tom # 첫글자 무조건 대문자
    module_function() # 모듈이름.함수 형태로 만들어 주는 함수(루비 내장 함수)
    def a()
        return "a"
    end
end

module Jerry
    module_function()
    def a()
        return 'b'
    end
end

puts(Tom.a())
puts(Jerry.a())

# 모듈 파일 분리법
# tom.rb , jerry.rb 로 파일 생성해서 module 집어 넣기

