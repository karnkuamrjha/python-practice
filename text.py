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
    

    