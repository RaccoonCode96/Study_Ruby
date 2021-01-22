# block 특성

# times 함수
# 5번 반복해라 {}를
5.times() {puts "5times"}
puts
2.times() {puts "2times"}
# times 는 함수고 {}부분은 코드블록이라고 함
puts
# upto함수
# 1씩 증가시켜서 3이 5가 될때까지 반복해라
3.upto(5) {puts "3 to 5 upto"}
puts
f1 = 0
3.upto(5) {f1+=1}
puts(f1)
puts
3.upto(5) {|i| puts i}
puts
f2 = 0
a = 3
a.upto(5) {|k| f2+=k}
puts(f2)


5.times() {|i| puts i}
3.upto(5) {|i| puts i}

puts
puts
puts
i = 0
while i < 5
    puts i
    i += 1
end