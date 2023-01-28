from typing import List, Sequence, Sized
from types import NoneType

def foo(xs: List[int]) -> int:
    return len(xs)

print(foo(list(range(3))))


def something(int) -> NoneType: 
    print(int)
    return None


print(foo(something(42)))