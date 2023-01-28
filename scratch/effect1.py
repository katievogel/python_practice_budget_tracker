from typing import Any, List


# def foo(xs: List[Any]) -> int: pass

# def constant42(xs: List[Any]) -> int: return 42
# def count(xs: List[Any]) -> int: return len(xs)
# def first_int(xs: List[Any]) -> int: pass
# def foo(xs: List[Any]) -> int: return None

# def foo(xs: List[int]) -> int: return xs[0]
# foo([])





def count(xs: List[Any]) -> int: 
    print("Counting")
    return len(xs)



def count(xs):
    print("Counting")
    return len(xs)

q = 100
acc = 0
def runningTally(xs):
    #acc = 0
    #acc += len(xs) + q
    print(f"inner\n...locals: ${locals().keys()} \n...globals: ${globals().keys()}")
    return len(xs) + q


acc = [1,2,3,4,5]

def do_y() -> list[int]:
    acc.append(0)
    return acc

# Example side effects include 
# modifying a non-local variable, 

b = 10
def add_to_b():
    global b 
    b = b+1 #this is the side effect
    return b

# modifying a static local variable, 

class Banana():
    color = "yellow"
    def __init__(self, weight):
        self.weight = weight
    
    def peel(self): 
        print(f"Peeling this banana, color: {self.color}, weight: {self.weight} ounces.")

    def magic(self):
        Banana.color = "green"


# modifying a mutable argument passed by reference,

def foo(xs): return xs.append(0)
acc = []
print(foo(acc))
print(foo(acc))

def fooPure(xs): xs + [0]




#  performing I/O or 

print("katie") # console I/O
# file I/O
# network I/O

# statements - order matters
print("a"); print("b"); print("c") # cannot be reordered

("a" + "0") + ("b" + "1") + ("c" + "2") # python can reorder them without changing result

# calling other functions with side-effects.


#print(count(range(10)))




class SortedList():

    _list: list = None

    def __iter__(self): return self
    def __getitem__(self, i): pass
    def __next__(self): pass
    def __count__(self): pass
