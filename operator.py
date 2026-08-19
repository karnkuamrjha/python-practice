#q1.Create two numbers and use arithmetic operators to calculate addition, subtraction, multiplication, division, modulus, and exponentiation.

first_number=int(input("enter your first number:"))
second_number=int(input("enter your second number:"))

addition=first_number+second_number
substractions=first_number-second_number
multiplications=first_number*second_number
division=second_number/first_number
modulus=second_number%first_number
expontential=first_number**second_number
floordivision=second_number//first_number
print("addition of two number is:",addition)
print("substraction of two number is:",substractions)
print("multiplication of two number is:",multiplications)
print("division of two number is:",division)
print("modulus of two number is:",modulus)
print("expotential of two number is:",expontential)
print("floor divison of two number is:",floordivision)

#q2.Take a person's age and use a comparison operator to check whether they are 18 or older.

age=int(input("enter your age:"))

if age>=18:
    print("right to vote")
else:
    print("not right to vote because you are very younger to vote it")


#q3.Create two numbers and use comparison operators to check which number is greater, smaller, or equal.

first_number=int(input("enter your first number:"))
second_number=int(input("enter your second number:"))

greater=first_number>second_number
smaller=first_number<second_number
equal=first_number==second_number
not_equal_to=first_number!=second_number

print("first number is grether than second number is:",greater)
print("first number is lower than second number is:",smaller)
print("first number is equal to second number is:",equal)
print("first number is not equal to second number:",not_equal_to)


#q4.Take a number and use the modulus (%) operator to check whether it is even or odd.

a=int(input("enter your number:"))

if a%2==0:
    print("number is even ")
else:
    print("number is odd")


#q5.Create two Boolean variables and use logical operators (and, or, not) with them.

age=True
driving_licence=False

first=(age and driving_licence)
second=(age or driving_licence)
third=not(age and driving_licence)
print(first)
print(second)
print(third)


#q6.Take a student's marks and use a ternary operator to print "Pass" if marks are 40 or above, otherwise "Fail".

marks=int(input("enter your marks:"))

results="pass"if marks>=40 else "fail"

print(results)


#q7.Create a variable and use assignment operators (+=, -=, *=, /=) to change its value.

score=int(input("enter how much points:"))

score +=1
print("team a +1 points",score)
score -=1
print("team a -1 points",score)
score *=2
print("team a *2 points ",score)
score /=2
print("team a /2 points",score)


#q8.Take two numbers and use floor division (//) to find how many complete groups can be made.

members=int(input("enter your total member in this show:"))
group=int(input("enter your total group in this show:"))

number_of_player_in_a_group=members//group
print(number_of_player_in_a_group)


#q9.Create two strings and use the in and not in operators to check whether a particular word or character exists in them.

a=input("enter the fruits do you like:")
b=input("enter your colour you like:")

c=("banana" in a)
d=("red" in b)

print("my guess you favourite fruitr is banan:",c)
print('my guess your favourite colour is red:',d)


#q10.Create two variables with the same value and use is and is not to understand identity comparison. 
a=['apple','banana'] 
b=['apple','banana'] 
print(a is b) #false :because both are same but object is differents 
print(a is not b) #true because opposite of it 

a==b 
print(a is b)       #false:because both are same but object are different
print(a is not b)   #true

b==a
print(a is b)       #false:because both are same but object are different
print(a is not b)   #true
