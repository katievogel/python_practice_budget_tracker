

class KatieIterable:
    x = 0
    def __iter__(self): 
        return self
    
    def __next__(self): 
        if self.x < 10:
            self.x += 1
            return self.x
        else:
            raise StopIteration()

    # def __getitem__(self, k): 
    #     return k

def katie_list(iter):
    acc = []
    try:
        while True:
            acc.append(next(iter))
    except StopIteration:
        pass
    return acc