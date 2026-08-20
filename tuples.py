"""
Q1. Creating Tuples

Create the following:

a.Empty tuple
b.Tuple with elements
c.Mixed tuple
d.Single-element tuple

Also check their types using type() and isinstance().

"""
#empty tuples
empty=()
print(tuple)
print(type(empty))
print(isinstance(empty,tuple))


#tuple with elements
tuple1=(1,2,3,4,5)
print(tuple1)
print(type(tuple1))
print(isinstance(tuple1,tuple))

#tuple with mixed elements
tuple2=("name","karn",True,1,2,3)
print(tuple2)
print(type(tuple2))
print(isinstance(tuple2,tuple))

#single element tuple
tuple3=(1)
print(tuple3)
print(type(tuple3))
print(isinstance(tuple3,tuple))   #false

tuple4=(1,)
print(tuple4)
print(type(tuple4))
print(isinstance(tuple4,tuple))     #true

"""
Q2. Tuple Accessing & Slicing

Create a tuple of 10 elements and:

a.Access the first element
b.Access the last element
c.Access elements using negative indexing
d.Slice the first 5 elements
e.Reverse the tuple
"""
tuple=(1,2,3,4,5,6,7,8,9,10)

#acess first elements
tuple1=tuple[0]
print(tuple1)

#acess last elements
tuple1=tuple[-1]
print(tuple1)

#acess element using negtive indexing
tuple1=tuple[-2]
print(tuple1)

#slice the first 5 elements
tuple1=tuple[:5]
print(tuple1)

#reverse tuple
tuple1=tuple[::-1]
print(tuple1)

"""
Q3. Tuple Operations

Create two tuples and perform:

a.Concatenation using +
b.Repetition using *
c.Check whether an element exists using in
d.Find the length using len()
"""
a=(1,2,3,4,5,6,7,8,9,10)
b=(11,12,13,14,15,16,17,18,19,20)

#Concatenation using +
c=a+b
print(c)

#Repetition using *
c=a*3
print(c)

#Check whether an element exists using in

d=(11 in a)         #false
print(d)

e=(10 in a)         #true
print(e)

#Find the length using len()
d=len(a)
print(d)

"""
Q4. Tuple Methods

Create a tuple containing duplicate values and use:

count()
index()

Also explain what each method does.
"""
a=(1,2,3,1,4,5,6,6,9,15,9,11,9)

#count
b=a.count(9)
print(b)

#index
b=a[9]
print(b)

"""
Q5. Tuple Packing & Unpacking

Create a tuple containing:

name = "Karn"
age = 24
course = "B.Tech"

Perform:

a.Tuple packing
b.Normal unpacking
c.Unpacking using *

"""
name = "Karn"
age = 24
course = "B.Tech"

#packing

identity=name,age,course

print(identity)


#noraml unpacking
name,age,course=identity
print(name)
print(age)
print(course)

#unpacking with*
name,*age=identity
print(name)
print(age)

"""
Q6. Nested Tuple

Create a nested tuple containing information about 3 students.

Example:

students = (
    ("Karn", 24, "B.Tech"),
    ("Rahul", 23, "BCA"),
    ("Aman", 22, "BBA")
)

Then:

a.Access "Karn"
b.Access 24
c.Iterate over the nested tuple
d.Print every student's information

"""
students = (
    ("Karn", 24, "B.Tech"),
    ("Rahul", 23, "BCA"),
    ("Aman", 22, "BBA")
)

#a.Access "Karn"
print(students[0][0])

#b.acess 24
print(students[0][1])

#iterate over the nested tuple

students = (
    ("Karn", 24, "B.Tech"),
    ("Rahul", 23, "BCA"),
    ("Aman", 22, "BBA")
)
for student in students:
    for item in student:
        print(item)

#print every student informations
for student in students:
    print(student)

"""
Q7. List to Tuple Conversion

Create a list of 5 fruits.

a.Convert the list into a tuple.
b.Check its type.
c.Access its elements.
d.Try changing one element and observe what happens.

"""
a=[1,2,3,4,5,6,7,8,9,10]

#a.convert list into tuple
b=tuple(a)
print(b)

#check its type
print(type(a))
print(type(b))

#acess the elements
c=b[2]
print(c)

#try changing one elements
#b[2]=6                      #TypeError: 'tuple' object does not support item assignment because tuple is imutable
#print(b)


"""
Q8. Practical Challenge 

Create a tuple containing the marks of a student in 5 subjects:

marks = (78, 85, 92, 67, 88)

Perform the following:

a.Find the total marks
b.Find the average
c.Find the highest mark
d.Find the lowest mark
e.Count how many times 85 occurs
f.Find the position of 92
g.Check whether 90 is present

"""
marks = (78, 85, 92, 67, 88)

#a.find total marks
b=sum(marks)
print(b)

#b.find the average
c=sum(marks)/len(marks)
print(c)

#c.heighest marks
d=max(marks)
print(d)

#e.lowest marks
e=min(marks)
print(e)

#f.find the postion of 92
f=marks.index(92)
print(f)

#g.check whether is 90 is present
g=(90 in marks)
print(g)
