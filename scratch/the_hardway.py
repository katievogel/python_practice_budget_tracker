# pg 146
import hardwaystuff
mystuff = {'apples': 'I AM APPLES!'}
print(mystuff['apples']) #gets apple from dict
hardwaystuff.apple() #gets apple function from module
print(hardwaystuff.tangerine) #gets tangerine variable from module

class MyStuff(object): #object is a leftover from py2
    def __init__(self):
        self.tangerine = "And now a thousand years between"
    
    def apple(self):
        print("I AM CLASSY APPLES!")

# note: instantiate is a fancy way of saying create.
# to instantiate a class is to create a class
thing = MyStuff()
thing.apple()
print(thing.tangerine)

#what's happening when you instantiate a class?
#Python looks for MyStuff and sees it's a class you made
#Python makes an empty object with all the functions you've included in the class
#Python then looks for '__init__' -- if it exists it calls the function to initialize your new empty object
#__init__ also gives you 'self' which is the empty object. self can be like a placeholder for whatever name you give to your instantiated class
#in this case self.tangerine is a lyric you assigned it to, and also belongs to the initialized object
#Now python can take this new object and assign it to 'thing'
#It is using the class as blueprint to build a copy of that type of thing


#Getting things from things: 3 Ways
#dict style
# mystuff['apple']

# #module style
# hardwaystuff.apple()
# print(hardwaystuff.tangerine)

# #class style
# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)


