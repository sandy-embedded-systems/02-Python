'''
11. Meet the Person: Calculate Age from Date of Birth

Scenario:
Log Session a birthday tracker! Determine someone’s age from their date of birth.

What you’ll learn:
Handling dates and calculating with them
Real-world use of classes

Task:
Make a Person class and compute age.

Example:
For a person born on 2000-05-25 (today is 2026-03-01):

Expected Output:
Alice is 25 years old.
'''

from datetime import date

class Person:
    def __init__(self, name, year, month, day):
        self.name = name
        self.dob = date(year, month, day)

    def calculate_age(self):
        today = date(2026, 3, 1)
        age = today.year - self.dob.year
        return age

p = Person("Alice", 2000, 5, 25)
print(f"{p.name} is {p.calculate_age()} years old.")

'''
12. The Ultimate Calculator: Basic Arithmetic by OOP
Scenario:
Build your own pocket calculator with class-based design.

What you’ll learn:
Encapsulating operations in methods
Using OOP for real utilities

Task:
Log Session a Calculator class with methods for add, subtract, multiply, and divide.

Example:
Adding 4 and 5, then dividing 10 by 2:

Expected Output:
9
5.0
'''
class Calculator:
    def __init__(self,v1=0,v2=0):
        self.num1=v1
        self.num2=v2
    def add(self):
        return self.num1+self.num2
    def sub(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return (self.num1/self.num2 if self.num2!=0 else None)
cal=Calculator(4,5)
print(cal.add(),cal.divide(),sep='\n')

'''
13. The Shape Family: Hierarchies for Area and Perimeter

Scenario:
Simulate a graphics editor: various shapes with their own formulas.

What you’ll learn:
Creating class hierarchies
Overriding methods for specialized behavior

Task:
Write a Shape base class, then subclasses for Circle, Triangle, and Square, each with its own area/perimeter.

Example:
If you create a Triangle with base 6 and height 4 and call area():

Expected Output:
12.0
'''

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side * self.side

t = Triangle(6, 4)
print(t.area())


'''
14. Binary Find Tree: Smart Organization

Scenario:
Organize data for fast searching, like contacts or scores.

What you’ll learn:
Implementing data structures as classes
Recursion in OOP

Task:
Build a BST class with methods for insertion and search.

Example:
Insert numbers and search for 5.

Expected Output:
True or False (depending on search)
'''


'''
15. Stack in Python: Undo That Move!

Scenario:
Log Session a feature like "undo" in a drawing app.

What you’ll learn:
How to build a stack (LIFO) using classes
Using lists for stack operations

Task:
Implement a Stack class with push and pop methods.

Example:
Push 10, then 20; pop an element.

Expected Output:
20
'''

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

s = Stack()
s.push(10)
s.push(20)
print(s.pop())


'''
16. The Linked List: Chain Reaction

Scenario:
Store and process data efficiently, like songs in a playlist.

What you’ll learn:
Building a linked list from scratch
Understanding nodes and pointers

Task:
Write a LinkedList class with insert, delete, and display.

Example:
Add 10, then 20, and display list.

Expected Output:
10 -> 20
'''


'''
17. Shopping Cart: OOP for Online Stores

Scenario:
Simulate adding/removing items and computing the bill in an online store.

What you’ll learn:
Real-world application of classes
Encapsulation and methods

Task:
Design a ShoppingCart class with add, remove, and total methods.

Example:
Add "Book" (2 × 200) and "Pen" (5 × 20); show total.

Expected Output:
500
'''

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, name, quantity, price):
        self.items[name] = (quantity, price)

    def total(self):
        total = 0
        for quantity, price in self.items.values():
            total += quantity * price
        return total

cart = ShoppingCart()
cart.add("Book", 2, 200)
cart.add("Pen", 5, 20)
print(cart.total())


'''
18. Enhanced Stack: Show Me What’s Inside

Scenario:
See the current state of the stack—great for debugging.

What you’ll learn:
Extending existing classes
Useful methods for state visibility

Task:
Add a display method to your Stack class to show its elements.

Example:
Push 1, then 2; display stack.

Expected Output:
[1, 2]
'''

class StackEnhanced:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def display(self):
        print(self.items)

se = StackEnhanced()
se.push(1)
se.push(2)
se.display()


'''
19. Queue It Up: Fair Turn for All

Scenario:
Manage waiting lines—like people in a ticket queue.

What you’ll learn:
Implementing a queue (FIFO) in Python
Real-world queue management

Task:
Build a Queue class with enqueue and dequeue methods.

Example:
Enqueue 10, then 20; dequeue once.

Expected Output:
10
'''

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

q = Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())

'''
20. The Banking System: Managing Accounts with OOP
Scenario:
Simulate a simple bank system: create accounts, deposit, withdraw, and check balances.

What you’ll learn:
Using classes for real-life simulations
Method design and data encapsulation

Task:
Log Session a BankAccount class with methods for deposit, withdraw, and balance check.

 
Example:
Start with balance 1000, deposit 500, withdraw 300, show balance.

Expected Output:
1200
'''
import random
class BankAccount:
    def __init__(self):
        self.__balance=0
        print("Enter password:")
        self.__password=input()
    def deposite(self,amt):
        if isinstance(amt,int):
            if amt<=0:
                print("Amount cannot be negative:")
            else: 
                self.__balance+=amt
                print("Deposite success")
        else:
            print("Deposite Faield")
            print("Amount shoud be a number")
    def withdraw(self,amt):
        if isinstance(amt,int):
            if amt<=0:
                print("withdraw failed")
                print("Amount cannot be negative:")
            else:
                if amt<self.__balance:
                    self.__balance-=amt
                    print("Withdraw success: ")
                else:
                    print("Not sufficient balence")
        else:
            print("Amount shoud be a number")
    def show_balance(self):
        pswd=input("Enter your password:")
        if pswd==self.__password:
            print("Available balance:",self.__balance)
        else:
            print("Authentication Failed")

my_acc=BankAccount()
while True:
    chance=int(input("1.deposite\n2.withdraw\n3.show balance\nselect your choice:"))
    if chance==1:
        my_acc.deposite(1000)
    elif chance==2:
        my_acc.withdraw(500)
    elif chance==3:
        my_acc.show_balance()
    else:
        print("invalid option")
