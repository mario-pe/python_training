class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

    def cos_tam_cos_tam(self):
        print('start')
        self.c = 6
        print(self.c)
        print('koniec')


f = Fib(max=5)
print(f.__iter__().a)
for i in f:
    print(i)