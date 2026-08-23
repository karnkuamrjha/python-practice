"""
Q1.Create a Dictionary

Create a dictionary named student containing the following information:

(A).Name
(B).Age
(C).Course
(D).Marks

Print the dictionary.
"""
student={
    "name:":"karn kumar jha",
    "age:":22,
    "course:":"b.tech",
    "marks:":90
}

print(student)

"""
Q2. Access Dictionary Elements

Create a dictionary of a student and access:

(A).Name using []
(B).Age using get()
(C).All keys using keys()
(D).All values using values()
"""

student = {
    "name": "Karan",
    "age": 24,
    "marks": 85
}

print(student["name"])


print(student.get("age"))

print(student.keys())

print(student.values())


"""
Q3. Add and Modify Elements

Create a dictionary:

student = {
    "name": "Karan",
    "age": 24
}

Add a "marks" key and modify the "age" value.
"""
student = {
    "name": "Karan",
    "age": 24
}

#add a marks key with values
student["marks"]=90
print(student)

#update age value
student["age"]=22
print(student)


"""
Q4. Delete Dictionary Elements

Create a dictionary containing five key-value pairs. Delete:

(A).One element using del
(B).One element using pop()
(C).All elements using clear()
"""
student = {
    "name": "Karan",
    "age": 24,
    "marks":90
}

#DEL ONE ELEMENT

del student["name"]
print(student)

#del one element using pop
student.pop("age")
print(student)

#del all element using clear
student.clear()
print(student)

"""
Q5. Dictionary Methods

Create a dictionary and demonstrate the use of:

(a).keys()
(b).values()
(c).items()
(d).get()
(e).update()
(f).pop()
(g).popitem()
(h).copy()

"""
student={
    "name:":"karn kumar jha",
    "age":22,
    "course":"b.tech",
    "collage:":"noida international university",
    "section:":"B"
}

#keys
print(student.keys())

#values
print(student.values())

#items
print(student.items())

#get
print(student.get("name:"))

#update
student.update({"city:":"katihar"})
print(student)

#pop     --------------       Removes a specific key-value pair
student.pop("section:")
print(student)

#popitem    ------    Removes the last inserted key-value pair
student.popitem()
print(student)

#copy
new_student=student.copy()
print(new_student)

"""
Q6. Iterate Over a Dictionary

Create a dictionary of five students and use for loops to:

(A).Print all keys.
(B).Print all values.
(C).Print all key-value pairs.

"""
student={
    "name":"karn kumar jha",
    "age":22,
    "course":"b.tech",
    "collage":"noida international university",
    "section":"B"
}

#iterate key
for key in student:
    print(key)

#iterate value
for value in student.values():
    print(value)

#iterate item
for key,value in student.items():
    print(key,":",value)


"""
Q7. Shallow Copy

Create a dictionary containing student information. Create a shallow copy using copy() and modify the copied dictionary.

Show that the original dictionary remains unchanged.
"""
student={
    "name":"karn kumar jha",
    "age":22,
    "course":"b.tech",
    "collage":"noida international university",
    "section":"B"
}


#shallow copy
new_student=student.copy()

new_student["name"]="rohit kumar"
new_student["age"]=23

print("information of roll no 1 :",student)
print("information of roll no 2:",new_student)


"""
Q8. Nested Dictionary

Create a nested dictionary containing information about three students, including:

Name
Age
Marks

Access the name and marks of any one student.

"""

student_information={
    "students1":{
        "name":"karn",
        "age":22,
        "marks":95
    },
    "students2":{
            "name":"rohit",
            "age":23,
            "marks":84
},
"students3":{
            "name":"suresh",
            "age":24,
            "marks":89
}
}

print(student_information["students1"]["name"])
print(student_information["students3"]["marks"])


"""
Q9. Dictionary Comprehension

Create a dictionary containing numbers from 1 to 10 and their squares using dictionary comprehension.
"""

number=[1,2,3,4,5,6]

square={number:number*2 for number in number}
print(square)

"""
q10.Merge Two Dictionaries

Create two dictionaries containing different student information and merge them into one dictionary using:

update()
| operator
"""
studen1={
    "name":"karn",
    "age":22,
    "marks":90
}

student2={
    "course":"b.tech",
    "age":23,
    "section":"b"
}

#update                                  #age:23 because there are two age key and key is unique they used update key 

studen1.update(student2)
print(studen1)


#** operator                            

student3={
    **studen1,
    **student2
}

print(student3)


#| operator
student4=studen1 | student2
print(student4)




"""
Q11. Student Management System

Create a student management dictionary for 5 students.

Each student should have:

Student ID
Name
Age
Course
Marks

Your program should allow you to:

(a).Add a new student.
(b).Display all students.
(c).Search for a student using Student ID.
(d).Modify a student's marks.
(e).Delete a student.
(f).Calculate and display the average marks.
(g).Display students who scored more than 75 marks.
"""

student_management_system={
    "student1":{
        "student id":1234567,
        "name":"karn",
        "age":22,
        "marks":90
    },
    "student2":{
        "student id":2345689,
        "name":"rohit",
        "age":23,
        "marks":84
    },
    "student3":{
        "student id":4567890,
        "name":"suresh",
        "age":24,
        "marks":89
    },
    "student4":{
        "student id":5678901,
        "name":"hardhik",
        "age":22,
        "marks":76
    },
    "student5":{
        "student id":7890123,
        "name":"nikhil",
        "age":25,
        "marks":87
}
}

#add new student
student_management_system["student6"]={
    "student id":1456789,
    "name":"prince",
    "age":23,
    "marks":85
}

print(student_management_system)

#display all student
for student,details in student_management_system.items():
    print(student,":",details)


#Search for a student using Student ID.

search_id=int(input("enter the student id:"))

for student,details in student_management_system.items():

    if details["student id"]==search_id:
        print("student",student)
        print("name:",details["name"])
        print("age:",details["age"])
        print("marks:",details["marks"])
        break
    else:
        print("student not found")


#modify student marks

student_management_system["student5"]["marks"]=93
print(student_management_system)

#delete a student

student_management_system.pop("student4")
print(student_management_system)


#calculate and display the average marks
total=0
count=0



for student,details in student_management_system.items():
    total=total+details["marks"]
    count=count+1
average=total/count
print(average)
print(count)
print(total)



#display student who scored 75 marks
for student,details in student_management_system.items():
    if details['marks']>75:
        print(student," : ",details["name"])
    

   