#q1.Create a variable to store your name and print it.
a=input("enter your name:")
print(a)

#q2.Create two variables to store two numbers and print their sum.
a=int(input("enter first number:"))
b=int(input("enter second number:"))

c=a+b
print(c)

#q3.Create variables for name, age, and city, then print all three.
name=input("enter your name:")
age=int(input("enter you age:"))
city=input("enter your city name:")

all_of_them=(f'my name is {name} my age is {age} i am from {city}')
print(all_of_them)

#q4.Create a variable price = 100. Change its value to 150 and print it.
price=100
print(price)
price=150
print(price)

#q5.Create a variable containing your age and calculate your age after 5 years.
mycurentage=int(input("enter your current age:"))
after5yearsage=int(5)+mycurentage
print(after5yearsage)

#q6.Create two variables and swap their values.
a=10
b=15

a,b=b,a
print(a)
print(b)

#q7.Create a variable containing a number as a string and convert it into an integer.
a="15"
print(type(a))
b=int(a)
print(b)
print(type(b))

#q8.Create variables of integer, float, string, and boolean types and print their types using type().
a="karn"
b=15
c=1.57
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


#q9.Create a variable marks and check whether the student has passed or failed using if-else.
a=int(input("enter your student total marks:"))
if a<=150:
    print("student is fail or giving reexam ")
else:
    print("student passed the exam ")


#q10.Create variables for product price and quantity and calculate the total bill.
productaname=input("enter 1 product name:")
productaprice=int(input("enter 1st product price:"))
quantinty1product=int(input("enter 1st product quantinty:"))

productbname=input("enter 2 product name:")
productbprice=int(input("enter 2nd product price:"))
quantinty2product=int(input("enter 2nd product quantinty:"))

productcname=input("enter 3 product name:")
productcprice=int(input("enter 3rd product price:"))
quantinty3product=int(input("enter 3rd product quantinty:"))

productdname=input("enter 4 product name:")
productdprice=int(input("enter 4th product price:"))
quantinty4product=int(input("enter 4th product quantinty:"))

productename=input("enter 5 product name:")
producteprice=int(input("enter 5th product price:"))
quantinty5product=int(input("enter 5th product quantinty:"))

final_bill=productaprice*quantinty1product+productbprice*quantinty2product+productcprice*quantinty3product+productdprice*quantinty4product+producteprice*quantinty5product
print(final_bill)

