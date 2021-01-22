# block array
# each 함수 
# 배열 안에 있는 것을 하나하나 꺼내는 함수
arr1 = ['a', 'b', 'c']
arr1.each() {|i| puts i}
# 위아래 같은 내용의 코드
for value in arr1
    puts(value)
end
puts
puts
puts
# delete_if 함수
# 배열에서 ture에 해당하는 값을 없앤다.
arr2 = [1, 3, 55, 63, 34, 52]
# 50보다 큰수를 없애자
arr2.delete_if() {|item|
    item > 50
}
puts arr2
arr2.delete_if() do |item|
    item > 50
end
puts arr2
# 코드가 길어지면 {} 중괄호 말고 do end 사용을 권장함


