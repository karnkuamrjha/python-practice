#q1.Write a Python program to print \"Hello, World!\"."(already)

#q2. Write a Python program that takes a user input and prints it.(already)

#q3.Write a Python program to check if a number is positive, negative, or zero.(already)

#q4.Write a Python program to find the largest of three numbers.(already)

#q5.Write a Python program to calculate the factorial of a number.

i = int(input("Enter your number: "))

fact = 1

for num in range(i, 0, -1):
    fact = fact * num

print(fact)

#Question 6:** Create variables of different data types: integer, float, string, and boolean. Print their values and types.(already)

#question 7:** Write a Python program to swap the values of two variables.(already)

#Question 8:** Write a Python program to convert Celsius to Fahrenheit.

celcius=int(input("enter the celcius:"))

farehneit=(celcius*9/5)+32

print(farehneit)

#Question 9:** Write a Python program to concatenate two strings.(already)

#Question 10:** Write a Python program to check if a variable is of a specific data type.

a="mango"
b=type(a)

if b==int:
    print("the specfic data type is integers")
elif b==str:
    print("the specfic data type is strings")
elif b==bool:
    print("the specfic data type is boolean")
else:
    print("the specific data type is float")


#Question 11:** Write a Python program to perform arithmetic operations: addition, subtraction, multiplication, and division(already)

#Question 12:** Write a Python program to demonstrate comparison operators: equal to, not equal to, greater than, less than.(already)

#Question 13:** Write a Python program to demonstrate logical operators: and, or, not.

#Question 14:** Write a Python program to calculate the square of a number
i=int(input("enter your number:"))

square=i**i
print(square)

#Question 15:** Write a Python program to check if a number is even or odd.(already)

#Question 16:** Write a Python program to find the sum of the first n natural numbers.
i = int(input("Enter your number: "))

natural=1

for i in range(i, natural, -1):
    natural = natural +i

print(natural)


#Question 17:** Write a Python program to check if a year is a leap year.

year=int(input("enter the year :"))

if year%400==0:
    print("this year is leap year")
    if year%4==0:
        print("this is leap year")
    else:
        print("this is not leap year")
else:
    print("this is not lear year")


#Question 18:** Write a Python program to reverse a string.
string=input("enter your name")

new=(string[::-1])
print(new)

#Question 19:** Write a Python program to check if a string is a palindrome.
a=input("enter any things:")

b=a[::-1]

if a==b:
    print("this letter is pallindrome")
else:
    print("this is not pallindrome")


#Question 20:** Write a Python program to sort a list of numbers in ascending order
"""
lst = [10, 20, 30, 40, 50, 12, 18]

new=lst.sort()                                     #none
print(new)

"""

lst = [10, 20, 30, 40, 50, 12, 18]

lst.sort()

print(lst)
