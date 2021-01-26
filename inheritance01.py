# 상속
# 상속은 객체의 기능을 그대로 가져와서 기능을 추가하는 느낌

class Class1(object):
    def method1(self):
        return 'm1'


c1 = Class1()
print(c1.method1())
print()


# 상속을 사용하는 법

class Class3(Class1):  # Class3는 Class1을 상속하여 기능을 사용한다.
    def method2(self): return 'm2'


c3 = Class3()
# c3라는 인스턴스의 클래스를 찾는다. -> 그 클래스 안에서 method1이 있는지 확인해보고 없으면 -> 부모 클래스에 method1이 있는지 확인하고 return
print(c3.method1())
print(c3.method2())
print()


# 상속 없이 해결하는 법(복사해서 새로운 클래스로 지정해서 기능을 추가함)

class Class2(object):
    def method1(self): return 'm1'
    def method2(self): return 'm2'


c2 = Class2()
print(c2.method1())
print(c2.method2())

# Class1의 기능을 사용하면서 새로운 기능도 쓸수 있음 -> 하지만 중복이 심해짐 -> 중복 제거 -> 가독성, 유지보수 등이 좋음
# 그래서 상속이 필요함
