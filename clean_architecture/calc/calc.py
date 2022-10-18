from functools import reduce


class Calc:
    # def add(self, a, b, c=0):
    #     # return 9
    #     return a + b + c

    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def multiply_many(self, *args):
        # def multiply_many_2(a, b):
        #     return a * b
        return reduce(lambda x, y: x * y, args)

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"

    def multiply_many(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)


s = range(100)
print(*s)
print(sum(s))
