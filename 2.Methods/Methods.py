
string = "hello"
x = 1
print(string.upper())

class Dog:

    def bark(self):
        print("bark")

    def meow(self):
        return "meow"
    
    def add_one(self, x):
        return x+1

d = Dog()
d.bark()
print(type(d))
print(type(d.add_one(4)))
print(type(d.meow()))
