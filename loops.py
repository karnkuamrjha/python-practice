#q1.Write a Python program using a for loop to print numbers from 1 to 20.

for i in range(1,21):
    print(i)


#q2.Write a Python program using a for loop to print all even numbers between 1 and 50.

for i in range(1,51):
    if i%2==0:
        print(i)

#q3.Write a Python program using a while loop to print numbers from 10 down to 1.

i=10

while i>=1:
    print(i)
    i=i-1

#q4.Write a Python program using a for loop to calculate the sum of numbers from 1 to 100.

sum=0

for i in range(1,101):
    sum=sum+i
    print(sum)


#q5.Write a Python program using a while loop to print the multiplication table of a number entered by the user.


number=int(input("enter any number you want multiplications:"))

i=1
while i<=10:
    print(i*number)
    i=i+1


#q6.Write a Python program using break to search for a particular number in a list and stop the loop when the number is found.

numbers = [10, 20, 30, 40, 50, 60, 70]

my_number = int(input("Enter your number: "))

for number in numbers:
    if number == my_number:
        print("The number successfully detected")
        break
else:
    print("Try another number")


#q7.Write a Python program using continue to print numbers from 1 to 20 but skip all multiples of 3.

for i in range(1,21):
    if i%3==0:
        continue
    print(i)


#q9.Write a Python program using a nested loop to print a 5 × 5 star pattern.

for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()


#q10.Write a Python program using a for loop to count how many vowels are present in a given string.

count = 0

sentences = input("Enter your sentence: ")

vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentences:
    if char in vowels:
        count = count + 1

print("The number of vowels:", count)
    