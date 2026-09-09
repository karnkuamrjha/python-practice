#q1.Create a custom module calculator.py with functions for addition, subtraction, multiplication, and division, and import it into another Python file.(cal.py)
import cal

print(cal.addition(10, 5))
print(cal.subtraction(10, 5))
print(cal.multiplication(10, 5))
print(cal.division(10, 5))

#q2.Use the math module to find the square root, power, ceiling, and floor of given numbers.(math.py)
import math

#sqrt (1 parameter)
#pow (2 parameter)
#ceil (1 parameter)
#floor(1 parameter)


print(math.sqrt(16))
print(math.pow(2,3))
print(math.ceil(4.8))
print(math.floor(5))


#q3.Create a Python program using the random module to generate a random number between 1 and 100.(math.py)

import random

print(random.randint(1,100))


#q4.Use the os module to create a folder, check whether it exists, rename it, and then delete it.(os.py)
import os

os.mkdir('orange.py')

print(os.path.exists('os.py'))

print(os.rename('text.py', 'texts.py'))

os.remove('orange.py')


#q5.Create source.txt, write some text into it, and use shutil to copy the contents into destination.txt.

import os

fd=os.open('desition.txt',os.O_CREAT)
fs=os.open('sources.txt',os.O_CREAT)

os.close(fd)
os.close(fs)

import shutil


shutil.copy('sources.txt','desition.txt')


#q6.Create a CSV file named students.csv containing Name, Age, and Marks for five students using csv.writer() and writerow().

import csv
import os

fd=os.open('students.csv',os.O_CREAT)

os.close(fd)


#create

with open('students.csv','w',newline='')as file:
    writer=csv.writer(file)


    writer.writerow(["name","age","marks"])
    writer.writerow(["Karn", 20, 85])
    writer.writerow(["Rahul", 21, 90])
    writer.writerow(["Amit", 19, 78])
    writer.writerow(["Priya", 20, 92])
    writer.writerow(["Neha", 21, 88])

#read

with open('students.csv','r')as file:
    reader=csv.reader(file)

    for line in reader:
        print(line)



"""q7.Use the datetime and timedelta modules to display:

a.Current date and time
b.Date after 2 days
c.Date before 3 days

"""
from datetime import datetime,timedelta

#current date and time
now=datetime.now()

#date after 2 days
future=now+timedelta(days=2)

#date before 3 days
past=now-timedelta(days=3)

print(now)
print(future)
print(past)



#q8.Write a Python program using time.sleep() that prints "Start", waits 3 seconds, and then prints "End".
import time

print('start')
time.sleep(3)
print('end')


#q9.Use the json module to store a student's name, age, and marks in a JSON file, then read the file back.
import json
import os

fd=os.open('student.json',os.O_CREAT)

os.close(fd)


student={"student1":{"name": "Karn",
    "age": 24,
    "marks":90
},
"student2":{
    "name": "ashu",
    "age": 24,
    "marks":82
}
}
#write: used dump

with open('student.json','w')as file:
    json.dump(student,file)

#read: used load

with open('student.json','r')as file:
    read=json.load(file)

    print(read)


#q10.Use the re module to find all phone numbers from a given sentence using re.findall().
import re

number="my phone number is 1234567890"

result=re.findall(r"\d+",number)

print(number)


#q11.Write a program using the random module to generate 10 random numbers between 1 and 100. output
import random

for i in range(1,10):
    print(random.randint(1,100))



#q12.Create a Python program that stores student information in a CSV file, reads the information, and uses datetime to record the date when the student was added.

#step1 : create a csv file using os
import os
import csv
from datetime import datetime,date

fd=os.open('newsstudent.csv',os.O_CREAT)
os.close(fd)

#datetime
now=datetime.now()
today=date.today()
new=today.strftime("%d-%b-%y")


# step 2: write data in csv file using append

with open('newsstudent.csv','a',newline="")as file:
    writer=csv.writer(file)

   
    writer.writerow([input("enter the student name:"),input("enter the student roll no:"),input("enter the student class:"),input("enter the student sections:"),new])


#q13.Write a Python program that checks whether important files exist in a folder, gets the current date, creates a new name for each file by adding the date, and records the original and new filenames in a separate file.
import os

#create 3 files
fd=os.open('report.txt',os.O_CREAT)
fe=os.open('data.pdf',os.O_CREAT)
ff=os.open('notes.txt',os.O_CREAT)
fg=os.open('newsfolder.txt',os.O_CREAT)

os.close(fd)
os.close(fe)
os.close(ff)
os.close(fg)

import shutil
from datetime import datetime

desition="newfolder.txt"

important_files = ["report.txt", "notes.txt", "data.pdf"]

date = datetime.now().strftime("%d-%b-%Y")
j="karn"

for i in important_files:
    if os.path.exists(i):
        name,extion=os.path.splitext(i)
        j=i,"→ ",name,date,extion
        j="".join(j)                       # Convert the tuple to a string:
        with open('newsfolder.txt','a')as file:
            file.write(j+"\n")              #write file write another file in new line

print("Backup completed successfully.")


    