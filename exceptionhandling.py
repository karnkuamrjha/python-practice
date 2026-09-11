#q1.Write a Python program to handle ZeroDivisionError when dividing two numbers.

try:
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    result=a/b
    print(result)
except ZeroDivisionError :
    print("please don't divided by zero ")


#q2.Write a program that takes a number from the user and handles ValueError if the user enters text instead of a number.

try:
    a=int(input("enter the number:"))
except ValueError:
    print("the number should be valid number")

#q3.Write a program to open a file and handle FileNotFoundError if the file does not exist.

try:
    a=input("plaese enter the file name:")
    file=open(a,"r")
    print(file.read())
    file.close()
except FileNotFoundError as f:
    print("ERROR:",f)


#q4.Write a program to access an invalid list index and handle IndexError.

a = ['mango', 'orange', 'papaya']

try:
    b = int(input("Which list item do you want to access by index: "))
    print(a[b])

except ValueError:
    print("Please enter a valid number.")

except IndexError:
    print("This index is not present in the list.")


#q5.Write a program to access a dictionary key that does not exist and handle KeyError.

a={'name':'karn',"age":23,"city":"katihar"}

try:
    b=input("enter what you want:")
    print(a[b])
except KeyError:
    print("this is not present in your dictonary")


#q6.Write a program that uses a variable that is not defined and handles NameError.

try:
   a=local
   print(a)
except NameError as n:
   print("ERROR",n)   


#q7.Write a program that performs an invalid operation between different data types and handles TypeError.

try:
    a='abc'
    b=123
    print(a+b)
except TypeError as t:
    print('ERROR',t)


#q8.Write a program using multiple except blocks to handle ValueError, ZeroDivisionError, and TypeError.

try:
    a=int(input("enter the number:"))
    b=int(input('enter the another number:'))
    result=a/b
    print(result)
except ValueError:
    print('give a valid number')
except ZeroDivisionError:
    print("not divided by 0")
except TypeError:
    print("not two different datatypes")


#q9.Write a program using try, except, else, and finally to perform a calculation and display appropriate messages.

try:
    a=int(input("enter the number"))
    b=int(input("enter the another number:"))
    c=a+b
    d=a-b
    e=a*b
    f=a/b
except ValueError:
    print("give a valid number")
except ZeroDivisionError:
    print("not divided by zero")
except Exception as e:
    print("ERROR",e)
else:
    print("ADDITION OF 2 NUMBER IS:",c)
    print("substraction of 2 number is:",d)
    print("multiplication of 2 number is:",e)
    print("divison of 2 number is:",f)
finally:
    print("the calculation will be done")


#Write a program using except Exception as e to display the error message for an unexpected exception.

try:
    a=int(input("enter the first number:"))
    b=int(input('enter 2 number:'))
    result=a/b
except ZeroDivisionError :
    print("not divided by zero")
except Exception as e:
    print("ERROR",e)
