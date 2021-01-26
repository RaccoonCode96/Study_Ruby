# 로그인 모듈 연결 해보기
# 경로 주의하고, 파일 이름으로 연결해야함
require "./module/login"
# 호출시에는 지정했던 모듈 이름으로 호출
puts(Auth.real_login())