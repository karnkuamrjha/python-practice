#q1.Create a lambda function to add two numbers.

add=lambda x,y:x+y 

print(add(5,7))


#q2.Create a lambda function to find the larger of two numbers.

largernumber=lambda x,y:x if x>=y else y

print(largernumber(5,7))


#q3.Create a lambda function to check whether a number is positive or negative.
#don directly used elif used 2 if conditions(nested)

check_number=lambda x:"postive number" if x>0 else "negtive number" if x<0 else "zero"

i=int(input("enter the number:"))

print(check_number(i))


#q4.Create a lambda function to calculate the cube of a number.

cube=lambda x:x**3 

i=int(input("enter the number:"))

print(cube(i))


#q5.Create a lambda function to calculate the total price after adding 10% tax.

total_price=lambda x,y:(x*y)-(x*y*10)/100

x=int(input("enter the price of product:"))
y=int(input("enter the quantinty of product:"))

print(total_price(x,y))



