# 모듈 연결 확인
# 모듈의 위치 동일하게 만들기
# require './Tom' ()괄호로 묶어도 상관 없고
# require_relative 'module/tom'
require_relative './jerry'
require './module/tom'

puts(Tom.a())
puts(Jerry.a())