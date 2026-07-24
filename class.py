'''
Create a class called Dog.

Requirements:

Attributes:
name
age
Method:
bark()

Output:

Dog Name: Bruno
Age: 3
Bruno says Woof!


'''




class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
        
    def bark(self):
        print(f'Dog Name: {self.name}\n Age: {self.age} \n {self.name} says Woof!')
        
        
my_dog = Dog('Bruno', 3)

my_dog.bark