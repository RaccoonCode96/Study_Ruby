# 함수 정의시 괄호 생략 가능하고 호출시 괄호 생략도 가능
def f1
    return "f1"
  end
  
  puts(f1) # 결과 f1

# 매개변수를 받는 경우의 괄호 생략 가능

def f2 k
    return k
end

puts(f2 "hello world!")
puts f2 "No parenthesis!"

# 함수 정의시 return의 생략

def f3 k
    a = 1
    b = 1
    a + b + k
end

puts f3 2