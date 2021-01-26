# 객체 지향 프로그래밍 (Object Oriented Programming)

# 지난시간
# 모듈 -> 함수 수납 -> 복잡도 단순화

# Oject
# class + instnace
# class : 모듈처럼 일정의 그룹핑을 할수 있는 수납 공간이지만, 모듈과 다르게 함수 및 연관변수들을 담을 수 있다. 

# class를 복제하여 instance를 만든다. 
# -> 각 intance는 class의 똑같은 변수와 똑같은 함수를 품지만, 변수의 값만 각각 바뀌어 품고 있는 공통된 함수를 이용해 결과를 낸다.

# instance : 

# 포유류(class) : 사람, 고양이, 개 (instnace)

# 객체 지향 프로그래밍의 사례

# 문자열 tom이 객체다
# name = 'tom'
name1 = String.new('tom') # 문자열을 만드는 방법이 이렇게 하나 더 있다.
# Stirng 은 클래스고 .new(값) -> new가 실행되면서 전체가 instance가 된다. -> name이라는 변수이름에 할당하면 instance화 된 tom을 사용할 수 있다.
name2 = String.new('jerry') # 문자열을 만드는 방법이 이렇게 하나 더 있다.
puts name1.reverse()
puts name2.reverse()
# name1 변수가 가르키는 인스턴스에는 tom이라는 값이 저장되어 있는데 name1에 들어 있는 reverse라는 함수를 실행시키면 tom의 값을 뒤집어 return해주는 것이다.
puts name1.upcase()
puts name1.size()
puts name1.length()

# 객체에 소속되어 있는 함수를 메소드라고 한다. 객체 안에서 사용될 때
# 기본적으로 많은 메소드들이 담겨 있다.

# array class의 경우
names = Array.new()
names.push('tom')
names.push('jerry')
names.push('snoopy')
puts names
print names
puts names.join('-') # join 메서드는 값들을 -로 연결해줌 

# 객체지향을 왜 사용하는가?
# 데이터가 많아지고 복잡해 지면서 정리하여 필요할때 쓰기 위해서

