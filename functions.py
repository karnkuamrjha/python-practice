#q1. Create a function that takes a person's name as a parameter and prints "Hello, <name>".

def person(name):
    print("hello",name)

new=input("enter your name:")
person(new)


#q2.Create a function that takes two numbers and returns their sum.
def sum(a,b):
    return a+b

print(sum(10,20))



#q3.Create a function that takes a number and checks whether it is even or odd using % 2.

def check(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
    
num=int(input("enter the number:"))

print(check(num))



#q4.Create a function that takes a number and returns its square.

def numbers(a):
    return a*a

a=int(input("enter the numbers:"))

print(numbers(a))



#q5.Create a function that takes name, age, and city and prints all three.

def people(name,age,city):
    print(name,age,city)

#postional arguments

people("karn",22,"katihar")


#keyword arguments
people(age=23,name="karn",city="katihar")


#q6.Create a function greet() with a default name "Guest". If a name is given, print that name.
def greet(name="guest"):
    print ("hello my name is:",name)

greet("kunal")
greet()


#q7.Create a function using *args that accepts any number of numbers and returns their sum.
def add(*args):
    return sum(args)

print(add(10, 20))
print(add(10, 20, 30, 40))


#8.Create a function that accepts name, age, and course using keyword arguments.
def person(name,age,course):
    print(name,age,course)

person(name="karn",course="b.tech",age=23)


#q9.Create a function that takes two numbers, returns their multiplication, and store the returned value in a variable.
def mul(a,b):
    return a*b

result=print(mul(10,15))


#q10.Create a function using **kwargs that accepts a student's name, age, course, and city and prints the dictionary.

def student(**kwargs):
    print(kwargs)

student(name="karn",age=23,course="b.tech",city="katihar")



"""
q11.Shopping Bill 
Create a function that takes product price and quantity and returns the total bill.

Example:

Price = 500
Quantity = 3
Total = 1500
"""
def shopping_bill(price,quantinty):
    return price*quantinty


price=int(input("enter the price of the product:"))
quantinty=int(input("enter the quantinty of the product:"))

print(shopping_bill(price,quantinty))
