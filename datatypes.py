#q1.Create variables to store your name, age, height, and whether you are a student, and print their data types.
a=input("enter your name:")
b=int(input("enter your age:"))
c=float(input("enter your height:"))
d=bool(input("you are student or not:"))

print(type(a),)
print(type(b),)
print(type(c))
print(type(d))
print(a)
print(b)
print(c)
print(d)


#q2.Create two integer variables and perform addition, subtraction, multiplication, and division.
first=int(input("enter your first number:"))
second=int(input("enter your second number:"))

additions=first+second
substractions=first-second
multiplications=first*second
division=second/first
print(additions)
print(substractions)
print(multiplications)
print(division)

#q3.Take a number as a string, convert it into an integer, and add 10 to it.
a="10"
b=int(a)+int(10)
print(b)


#q4.Create a string "" and use slicing to print "Python" and "Programming" separately.

a="Python Programming"
b=print(a[0:6])
c=print(a[7:18])


#q5.Create a string " Hello Python " and remove the extra spaces using strip().

a=" Hello Python "
print(a.strip())

#q6.Create a string "I love Java" and use replace() to change "Java" to "Python".

a="I love Java"
print(a.replace("Java","python"))

#q7.Create a list of 5 numbers and try to access an index that does not exist. Observe the error.
"""
a=[1,2,3,4,5,6,7]
print(a[8])

"""
#list index error


#q8.Create a dictionary containing name, age, and city. Try to access a key that does not exist and observe the error.
"""
a={'name':"karn","age":22,"city":"katihar"}
print(a['class'])

"""

#q9.Create two strings containing your first name and last name, then concatenate them to create your full name.

first_name=input("enter your first name:")
last_name=input("enter your last name:")
full_name=first_name+" "+last_name
print(full_name)

#q10.Create variables for name, age, and marks and display them using an f-string.
name=input("enter your name:")
age=int(input("enter your age:"))
marks=int(input("enter your marks:"))

full=(f'my name is {name} my age is {age} and my marks is {marks}')
print(full)