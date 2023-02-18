

class ForwardRangeIterator():
    def __init__(self, current, stop):
        self.current = current
        self.stop = stop

    def __next__(self): 
        if self.current < self.stop:
            this = self.current
            self.current += 1
            return this
        else:
            raise StopIteration()

class BackwardsRangeIterator():
    def __init__(self, current, stop=0):
        self.current = current
        self.stop = stop

    def __next__(self):
        if self.current > self.stop:
            this = self.current
            self.current -= 1
            return this
        else:
            raise StopIteration

class KRange():
    def __init__(self, current, stop):
        self.current = current
        self.stop = stop
    
    def __iter__(self): return ForwardRangeIterator(self.current, self.stop)
    def __reversed__(self): return BackwardsRangeIterator(self.stop, self.current)




# def dassert(a, b):
#     if a == b: print("pass")
#     else: print(f"fail: {a}")

# print("running tests")
# dassert([x for x in KRange(0, 3)], [0, 1, 2])
# dassert([x for x in reversed(KRange(0, 3))], [2, 1, 0])

# def katie_list(iter):
#     acc = []
#     try:
#         while True:
#             acc.append(next(iter))
#     except StopIteration:
#         pass
#     return acc