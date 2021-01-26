require_relative 'lib'
obj = Lib::A.new() # 모듈에 속한 클래스를 가져올 경우 ::을 씀
p obj.a()