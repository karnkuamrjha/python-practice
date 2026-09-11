#exception handling

a=10
b=0

#print(a/b)    error:division by zero

#how to solve this error using exception handling
a=10
b=int(input("enter the number"))

try:
    print(a/b)
except ZeroDivisionError:
    print('cannot divided by zero giving another number')


#alias use

a=int(input("enter the number:"))
b=int(input("enter the another number:"))

try:
    print(a/b)
except ZeroDivisionError as e:
    print("error:",e)



#2.file not found error

#file=open('karn.py','r')              #FileNotFoundError


#method 1:
try:
    file=open('karn.py','r')
    print(file.read())
except FileNotFoundError:
    print('giving another file this file is not in this computer')

#method 2 used alias

try:
    file=open('karn.py','r')
    print(file.read())
except FileNotFoundError as f:
    print('error',f)


#3.valueeror

#age=int('abc')                        ValueError


try:
    age=int('abc')
    print(age)
except ValueError as g:
    print('error',g)


#4.typeerror

"""
a="karn"                            TypeError
b=123
c=a+b
d=type(c)
"""

#solve it typeerror using try and except
try:
    a='karn'
    b=123
    print(a+b)
except TypeError as t:
    print("error",t)


#5.indexerror

"""numbers=[10,20,30]                    IndexError

print(numbers[4])"""

#solve index error

try:
    numbers=[10,20,30]
    print(numbers[4])
except IndexError as h:
    print("error",h)



#6.keyeeror
"""
name={'karn':23,'ankit':24}                  keyerror

print(name['rahul'])

"""

try:
    name={'karn':23,'ankit':24}
    print(name['rahul'])
except KeyError as k:
    print("error",k)


#7.nameerror

#print(mirchi)                           NameError


try:
    print(mirchi)
except NameError as n:
    print("error",n)


#attributeerror   

"""name="karn"                      AttributeError

print(name.append('kumar'))
"""

name='karn'
try:
    name.append("kumar")
except AttributeError as a:
    print("error",a)



#what happend when eeror is different as used exception error is different

#a=int('abc')               ValueError

"""
try:
    a=int('abc')
    print(a)
except ZeroDivisionError as z:
    print("error",ZeroDivisionError)

when your error is valueeror and use zerodivison error the valueeror also show 

"""

#use general except for anyone---any type of error exception handle every error.

try:
    a=int('abc')
    print(a)
except Exception as e:
    print("error",e)


#multiple exception use

try:
     number = int(input("Enter a number: "))
     result = 100 / number
     print(result)
except ValueError:
    print("please enter a valid number")
except ZeroDivisionError :
    print("number not divided by zero")
except Exception as e:
    print("error",e)



#try,except,else

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)
    print("Operation successful")


#try,except,else,finally

try:
    number=int(input("enter the number:"))
    result=100/number
except ValueError:
    print("give valid number")
except ZeroDivisionError:
    print('not give 0 as a number')
except Exception as e:
    print("error",e)
else:
    print('result',result)
finally:
    print('the result will be come ')