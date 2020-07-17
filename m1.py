class MyNum:
    def __init__(self,num):
        self.num=num

    def __add__(self, nr):
        return MyNum(self.num + nr)

    # def __radd__(self, nr):
    #     return MyNum(self.num + nr)

    def __mul__(self, other):
        return MyNum(self.num * other)

    def __str__(self):
        return str(self.num)

print(calc)