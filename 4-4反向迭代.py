class Countdown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

    def __reversed__(self):
        n = self.start
        while n>0:
            yield n
            n -= 1

# 如果有__reversed__这个函数，那么就不会调用__iter__
for rr in reversed(Countdown(30)):
    print(rr)


for i in Countdown(30):
    print(i)