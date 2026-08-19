#q1.Take a number and check whether it is positive, negative, or zero.

num=int(input("enter your number:"))

if num > 0:
    print("the number is a postive number")
elif num==0:
    print("the number is zero")
else:
    print("the number is negetive")


#q2.Take a number and check whether it is even or odd.(already)

#q3.Take a person's age and check whether they are child, teenager, or adult.

age=int(input("enter your age:"))

if age > 13:
    print("you are teenage boys")
elif age>= 20:
    print("you are adult")
else:
    print('you are a child')


#q4.Take two numbers and print the greater number.

a=int(input("enter you first number:"))
b=int(input("enter your second number:"))

if a>=b:
    print("the greater number is",a)
else:
    print("the greater number is",b)


#q5.Take three numbers and find the largest number.

a=int(input("enter you first number:"))
b=int(input("enter your second number:"))
c=int(input("enter your third numbers:"))

if a>=b and a>=c:
    print("the greater number is",a)
elif c>=b and c>=a:
    print("the greter number is",c)
else:
    print("the greter number is",b)


"""
q6.Take marks and display the grade:

90+ → A
75–89 → B
60–74 → C
40–59 → D
Below 40 → Fail

"""
marks=int(input("enter your marks:"))

if marks>=90:
    print("your grade is A")
elif marks>=75:
    print("your grade is B")
elif marks>=60:
    print("your grade is C")
elif marks>=40:
    print("your grade is d")
else:
    print("you are fail to exam ")


#q7.Take a username and password and check whether the login details are correct.

username="karn"
password="#boys"

getusername=input("enter your username:")
getpassword=input("enter your password:")

if getusername==username and getpassword==password:
    print("your login details is correct and page will be open")
elif getusername==username:
    print("your username is correct but password is wrong")
else:
    print("you login details is incorrect try next time")


#q8.Take a temperature and display whether the weather is cold, normal, or hot.

temperature = float(input("enter your temperture:"))

if temperature < 15:
    print("Cold")
elif temperature <= 30:
    print("Normal")
else:
    print("Hot")


#q9.Take an amount of money and calculate a discount based on different price ranges using if-elif-else.


bill_amount=int(input("enter your total amount:"))

b=30*bill_amount/100
c=20*bill_amount/100
d=10*bill_amount/100

e=bill_amount-b
f=bill_amount-c
g=bill_amount-d


if bill_amount>=3000:
    print("you get 30% off and your bill amount now is:",e)
elif bill_amount>=2000:
    print("you get 20% off and your bill amount now is:",f)
elif bill_amount>=1500:
    print("you get 10% off and you bill amount now is :",g)
else:
    print("you not get any % off you bill amount is",bill_amount)


#q10.Take a number representing a month (1–12) and print the month name using conditional statements.

month=int(input("enter your month number:"))


if month==1:
    print("january")
elif month==2:
    print("ferbuary")
elif month==3:
    print("march")
elif month==4:
    print("april")
elif month==5:
    print("may")
elif month==6:
    print("june")
elif month==7:
    print("july")
elif month==8:
    print("august")
elif month==9:
    print("september")
elif month==10:
    print("october")
elif month==11:
    print("november") 
elif month==12:
    print("december")
else:
    print("this is not month number please give number between 1-12")  