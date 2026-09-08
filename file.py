#q1. Create a text file and write your name, age, and city into it. Then read and display the file.

file=open('file.txt','r')

dat=file.read()

print(dat)

file.close()


#q2.Create a file containing 5 student names and read the file line by line.

file=open('file.txt','r')

data=file.read()

for fil in data:
   print(fil)


#q3.Write a program to count the number of lines in a text file.

file=open('file.txt','r')

data=file.read()

print(data.count("name"))


#q4.Create a file and write 10 numbers into it. Then read the file and calculate their sum.(uses sum)

file=open('file.txt','r')

data=file.read().split()

numbers=[int(x) for x in data]

print(sum(numbers))

file.close()

#q5.Create a file and write 10 numbers into it. Then read the file and find the largest number.(use max)

file=open('file.txt','r')

data=file.read().split()

numbers=[int(x) for x in data]

print(max(numbers))

file.close()

#q6.Create a file and write 10 numbers into it. Then read the file and find the smallest number.(use min)

file=open('file.txt','r')

data=file.read().split()

num=[int(x) for x in data]

print(min(num))


#q7.Create a file and write 10 numbers into it. Then read the file and calculate their average.

file=open('file.txt','r')

data=file.read().split()

num=[int(x) for x in data]
#sum of number
a=sum(num)
#count of number
b=len(num)

#find average
avg=a/b
print(avg)


#q8.Create a file and write 10 numbers into it. Then read the file and calculate the difference between the largest and smallest number.
file=open('file.txt','r')

data=file.read().split()

num=[int(x) for x in data]

#find heighest number
high=max(num)

#find lowest number
low=min(num)

#differences of two number
difference=high-low
print(difference)


#q9.Create a file and write 10 numbers into it. Then read the file and count how many numbers are even and how many are odd.
file=open('file.txt','r')

data=file.read().split()

num=[int(x) for x in data]
even=0
odd=0

for new in num:
   if new%2==0:
    print(new,"---","even number")
    even=even+1
   else:
    print(new,"---","odd number")
    odd=odd+1

print("the total number of even is:",even)
print("the total number of odd is",odd)


#q10.Create a file and write 10 numbers into it. Read the numbers and subtract all numbers from the first number.

file = open("file.txt", "r")

data = file.read().split()
num = [int(x) for x in data]

a = num[0]
b = num[1:]

for r in b:
    a = a - r

print(a)

file.close()


#q11.Create a file and write 10 numbers into it. Read the numbers and calculate their total multiplication.
file = open("file.txt", "r")

data = file.read().split()
num = [int(x) for x in data]

a=num[0]
b=num[1:]

for r in b:
    a=r*a

print(a)


#q12.Create a file and write 10 numbers into it. Read the numbers and calculate the multiplication of only the even numbers.

file = open("file.txt", "r")

data = file.read().split()
num = [int(x) for x in data]

a = 1

for r in num:
    if r % 2 == 0:
        a = a * r

print(a)

file.close()


#q13.Create a file containing a paragraph and count the number of words in the file.
file=open('newfile.txt','r')

data=file.read()

length=len(data)

print("count number of word with space:",length)


#not count space

new = len(data.replace(' ',""))

print("number of words without space:", new)



#q14.Write a program to append new student names to an existing file without overwriting the old names.
#ahwin name add in the student 
file=open("newfile.txt",'a')

file.write("ashwin")



#q15.Create a list of 5 sentences and use writelines() to write them into a file, with each sentence on a new line.
list=['roll no 1---aaksh\n'
,'roll no 2 --- ashwin\n'
,'roll no 3---karn\n'
,'roll no 4 - vikram\n',
'roll no 5---yash']

with open('newfile.txt','w')as file:
    file.writelines(list)



#q16.Create a file using "w+", write some text, use seek(0), and then read the complete file.
file=open('file.txt','w+')

file.write("hello world")

file.seek(0)

data=file.read()

print(data)

file.close()


#q17.Create a binary file using "wb" and write some bytes into it. Then use "rb" to read and display the bytes.


file = open("bytes.txt", "wb+")

file.write(bytes([0, 1, 2, 3, 4]))

file.seek(0)

data = file.read()

file.close()

print(data)


#q18.Write a program using seek() that reads a file from position 5 instead of from the beginning.

file=open('file.txt','a+')

file.write("hello world")

file.seek(5)

data=file.read()

print(data)

file.close()

#q19.Student Record System: Create a Python program that stores student names, roll numbers, and marks in a file. Allow the user to add new students without deleting existing records, and then read and display all student records.
student = {
    "name": input("Enter student name: "),
    "roll_no": int(input("Enter roll number: ")),
    "marks": int(input("Enter marks: "))
}


#add new student
file=open('practice.txt','a')

file.write(str(student)+"\n")

file.close()

#read file

file=open('practice.txt','r')

data=file.read()

print('\nstudent records:')
print(data)

file.close()


#q20.Employee Record System: Create a Python program that stores employee name, employee ID, department, and salary in a file using a dictionary. Allow the user to add new employees without deleting existing records, and then read and display all employee records.

empolyee={
    "empolyee id":input("enter the empolyee id:"),
    "empolyee name":input("enter the empolyee name:"),
    "department name":input("enter the departnment name:"),
    "salary":input("enter the salary:")
}

#write files
file=open('empolyee.txt','a')

file.write(str(empolyee)+"\n")

file.close()

#read files

file=open('empolyee.txt','r')

data=file.read()


print(data)

file.close()


