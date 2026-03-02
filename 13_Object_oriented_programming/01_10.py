'''
1. Crafting Your First Python Object: The Power of Instance Attributes

Scenario:
Imagine you're building a digital notebook. You want each note to have its own title and content.

What you’ll learn:
How to define classes and create objects with unique data
The magic of instance attributes in organizing information

Task:
Design a Note class with title and content as instance attributes.
Log Session two different note objects and print their details.

Example:
Suppose you create notes like “Meeting Notes” and “Grocery List”.

Expected Output:
Meeting Notes : Discuss project status with team.
Grocery List : Eggs, Milk, Bread
'''

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

note1 = Note("Meeting Notes", "Discuss project status with team.")
note2 = Note("Grocery List", "Eggs, Milk, Bread")

print(f"{note1.title} : {note1.content}")
print(f"{note2.title} : {note2.content}")


'''
2. The Mysterious Empty Class: Why Bother?

Scenario:
You're designing a game and want to reserve a class for future magical creatures—but for now, it's empty.

What you’ll learn:
Why and how to define an empty class
Using pass and setting up blueprints for future code

Task:
Log Session an empty MagicCreature class and show that you can still make objects from it.

Example:
You make a new MagicCreature object and print its type.

Expected Output:
<class '__main__.MagicCreature'>
'''

class MagicCreature:
    pass

creature = MagicCreature()
print(type(creature))


'''
3. Family Traits: Inheritance in Action with Vehicles and Buses

Scenario:
You’re modeling a transportation system. Buses are vehicles, so shouldn’t they share common features?

What you’ll learn:
Inheriting attributes and methods from a parent class
The principle of code reuse and extension

Task:
Log Session a Vehicle class and a Bus class that inherits from it. Demonstrate shared behavior.

Example:
Suppose you make a Bus object and call its move() method.

Expected Output:
Vehicle is moving
'''

class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bus(Vehicle):
    pass

b = Bus()
b.move()


'''
4. Shape Shifters: Mastering Class Inheritance

Scenario:
Imagine you’re building a drawing tool. You have a general Shape, but want to specialize it into Circle and Square.

What you’ll learn:
The basics of inheritance
How subclasses can extend or override parent class functionality

Task:
Log Session a Shape class with a method called draw(). Inherit and customize in Circle and Square.

Example:
If you create a Circle and ask it to draw():

Expected Output:
Drawing a circle
'''

class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Square(Shape):
    def draw(self):
        print("Drawing a square")

c = Circle()
c.draw()


'''
5. One for All: The Magic of Class Attributes

Scenario:
All students in a school belong to the same institution. How can you ensure this is reflected in every student object?

What you’ll learn:
Class (static) attributes: properties shared by all instances
When and why to use them

Task:
Define a Student class where every student has the same school_name.

Example:
If you create two students and print their school_name:

Expected Output:
Central High School Central High School
'''

class Student:
    school_name = "Central High School"

s1 = Student()
s2 = Student()

print(s1.school_name, s2.school_name)


'''
6. Is That What I Think It Is? Type Checking Objects

Scenario:
You’re building a dynamic form. You need to know if a user input is a string, number, or something else.

What you’ll learn:
How to use type() and why it’s useful
Avoiding type errors in your code

Task:
Check and print the type of various objects.

Example:
You create an integer and a string and check their types.

Expected Output:
<class 'int'>
<class 'str'>
'''

a = 10
b = "Python"

print(type(a))
print(type(b))


'''
7. Are You One of Us? Checking Class Membership

Scenario:
You want to make sure a Bus object can access special parking. But only if it’s really a Vehicle.

What you’ll learn:
Using isinstance() to check an object’s class or parent classes
Dynamic type safety

Task:
Check if a Bus object is an instance of Vehicle.

Example:
You check with isinstance() for a Bus object.

Expected Output:
True
'''

class Vehicle:
    pass

class Bus(Vehicle):
    pass

b = Bus()
print(isinstance(b, Vehicle))


'''
8. True Descendants: Subclass Checking

Scenario:
You’re building a plugin system and want to know if a new class is a valid type of plugin.

What you’ll learn:
The use of issubclass()
Class relationships in Python

Task:
Check if Bus is a subclass of Vehicle.

Example:
You use issubclass() with Bus and Vehicle.

Expected Output:
True
'''

class Vehicle:
    pass

class Bus(Vehicle):
    pass

print(issubclass(Bus, Vehicle))


'''
9. Polymorphism in the Real World: Area of Shapes

Scenario:
You’re making a geometry tool. Different shapes need to compute area, but each does it differently.

What you’ll learn:
Polymorphism: different classes, same interface
Practical OOP design patterns

Task:
Log Session a Shape base class with an area() method, then implement it differently in Circle and Square.

Example:
If you create a Square with side 4 and call area():

Expected Output:
16
'''

class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

sq = Square(4)
print(sq.area())


'''
10. All About Circles: Area and Perimeter

Scenario:
Designing a map app? You’ll want to know the area covered by a circular pond!

What you’ll learn:
Implementing methods with calculations
Understanding encapsulation

Task:
Build a Circle class with area() and perimeter() methods.

Example:
For a circle of radius 3:

Expected Output:
28.27
18.85
'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    
    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

c = Circle(3)
print(c.area())
print(c.perimeter())