# 계산기 예제에서 override 활용

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
        for item in Cal._history:
            print(item)

    def info(self):
        return "Cal => v1 : %d, v2 : %d" % (self.v1, self.v2)


class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "CalMultiply => %s" % (super().info())


class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result

    def info(self):
        return "CalDivdie => %s" % (super().info())


c0 = Cal(30, 60)
print(c0.info())
c1 = CalMultiply(10, 10)
print(c1.info())
c2 = CalDivide(20, 10)
print(c2.info())
