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

