
class Cal(object):
    _history = []

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        result = self.v1+self.v2
        Cal._history.append(
            "add : {0}+{1}={2}".format(self.v1, self.v2, result))
        return result

    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result

    @classmethod
    def history(cls):
        for item in Cal._history:  # 외부에서 사용안하고 내부에서만 사용하므로 _를 붙임
            print(item)


class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result


class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result


c1 = CalMultiply(10, 10)
print(c1.multiply())
print(c1.add())
print(c1.subtract())

c2 = CalDivide(20, 10)
print(c2.multiply())
print(c2.add())
print(c2.subtract())
print(c2.divide())

Cal.history()
