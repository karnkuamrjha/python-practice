#1Write a program that asks the user to input a number and prints whether the number is positive and even, positive and odd, or negative.

i=int(input("enter your number:"))

if i>0:
    if i%2==0:
        print("this is even number")
    else:
        print("this ios odd number")
elif i==0:
    print("this is zero")
else:
    print("this is negetive number")


#2.Write a program that asks the user to input numbers until they input 0. The program should print the sum of all the input numbers.

total=0

while True:
    numbers=int(input("enter your numbers:"))

    if numbers==0:
        break

    total=numbers+total

print(total)


#q3.Write a program that prints all the numbers from 1 to 10 except 5 using a for loop and continue statement.

for i in range(1,11):
    if i==5:
        continue
    print(i)

#q4.Write a program that asks the user to input a number and prints all the even numbers from 1 to that number using a for loop

numbers = int(input("Enter a number: "))

for i in range(1, numbers + 1):
    if i % 2 == 0:
        print(i)

#q5.Write a program that calculates the sum of the digits of a number input by the user using a while loop.

number = int(input("Enter a number: "))

total = 0

while number > 0:
    digit = number % 10
    total = total + digit
    number = number // 10

print("Sum of digits:", total)


#q6.Write a program that checks if a number input by the user is a prime number using a for loop

numbers = int(input("Enter your number: "))

is_prime = True

for i in range(2, numbers):
    if numbers % i == 0:
        is_prime = False
        break

if is_prime and numbers > 1:
    print("Prime number")
else:
    print("Not a prime number")


#q7.Write a program that prints the first n Fibonacci numbers, where n is input by the user
numbers = int(input("Enter your number: "))

previous_numbers = 0
current_number = 1

for i in range(numbers):
    print(previous_numbers)

    new_numbers = previous_numbers + current_number
    previous_numbers = current_number
    current_number = new_numbers

    