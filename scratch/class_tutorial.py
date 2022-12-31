import unittest
from unittest import TestCase

class Person():
    name: str
    age: int

    def __init__(self, name: str, age: int):   # constructor
        self.name = name
        self.age = age

class TestPerson(TestCase):
    def test_person_constructor(self):
        katie1 = Person('Katie', 39)
        self.assertEqual(katie1.age, 39)
        self.assertEqual(katie1.name, 'Katie')
        dustin = Person('Dustin', 37)
        self.assertEqual(dustin.age, 37)
        self.assertEqual(dustin.name, 'Dustin')

        dustin = Person('Dustin', 37)
        dustin = Person(name = 'Dustin', age = 37)
        dustin = Person(name = None, age = None)
        dustin = Person(None, None)

if __name__ == '__main__':
    unittest.main()

# def initialize2(o, name, age):
#     o.name = name
#     o.age = age

# katie1 = Person()

# Person.initialize(katie1, "Katie Getz", 39)
# Person.initialize("Katie Getz", 39)
# initialize2(katie1, "Katie new name", 39)

# katie1 = Person()
# katie1.initialize("Katie Vogel", 39)


# katie1 = Person("Katie Vogel", 39)

# dustin1 = Person()
# dustin1.initialize("Dustin Getz", 37)

#katie1 = Person("Katie Vogel", 39)
