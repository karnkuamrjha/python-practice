""".
Q1. Create a List

Create the following three types of lists:

Empty list
List containing only integers
Mixed list containing string, integer, float, and Boolean.
"""

lst=[]
print(lst)

lst1=[1,2,3,4,5]
print(lst1)

lst2=['mango','orange',1,2,True,False]
print(lst2)


"""
Q2. Access List Items

Given:

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

Write Python code to:

1,Access "Apple" using positive indexing.
2.Access "Grapes" using negative indexing.
3.Access "Mango" using its index.
"""


fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

fruits1=fruits[0]
print(fruits1)


fruits2=fruits[-1]
print(fruits2)

fruits3=fruits[2]
print(fruits3)


"""
Q3. Modify a List

Given:

numbers = [10, 20, 30, 40]

Perform the following:

1.add 50 at the end using append().
2.Add 15 at index 1 using insert().
3.Remove 30 using remove().
4.Remove the last element using pop().

"""

numbers = [10, 20, 30, 40]

#1.add 50 at the end using append().
numbers.append(50)
print(numbers)

#2.Add 15 at index 1 using insert().
numbers.insert(1,15)
print(numbers)

#3.Remove 30 using remove().
numbers.remove(50)
print(numbers)

#4.Remove the last element using pop().
numbers.pop()
print(numbers)


"""
Q4. List Methods

Create a list:

numbers = [5, 2, 8, 2, 10, 2]

Use the following methods:

1.index()
2.count()
3.sort()
4.reverse()
5.clear()

Print the result after each operation.
"""

numbers = [5, 2, 8, 2, 10, 2]

#1.index()
print(numbers.index(10))

#2.count()
print(numbers.count(2))

#3.sort
numbers.sort()
print(numbers)

#4.reverse
numbers.reverse()
print(numbers)

#5.clear
numbers.clear()
print(numbers)


"""
Q5. List Slicing

Given:

numbers = [10, 20, 30, 40, 50, 60]

Write code to:

1.Get [20, 30, 40]
2.Get the first 3 elements.
3.Get the last 3 elements.
4.Get every second element.
5.Reverse the complete list using slicing.
"""

numbers = [10, 20, 30, 40, 50, 60]

#1.Get [20, 30, 40]
numbers1=numbers[1:4]
print(numbers1)

#2.Get the first 3 elements.
numbers2=numbers[0:3]
print(numbers2)

#3.Get the last 3 elements.
numbers3=numbers[-3:]
print(numbers3)

#4.Get every second element.
numbers4=numbers[1::2]
print(numbers4)

#5.Reverse the complete list using slicing.
numbers5=numbers[::-1]
print(numbers5)

"""
Q6. Iterate Over a List

Given:

students = ["Karan", "Rahul", "Amit", "Ravi"]

Use a for loop to print every student one by one.

"""

students = ["Karan", "Rahul", "Amit", "Ravi"]

for i in students:
    print(i)


"""
Q7. Use enumerate()

Given:

fruits = ["Apple", "Banana", "Mango"]

Use enumerate() to print the index and value.
"""

fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

'''
Q8. List Comprehension

Given:

numbers = [1, 2, 3, 4, 5, 6]

Use list comprehension to create:

1.A list containing squares of all numbers.
2.A list containing only even numbers.
3.A list containing "Even" or "Odd" for each number.
'''

numbers = [1, 2, 3, 4, 5, 6]

#1.A list containing squares of all numbers.
square=[x*x for x in numbers]
print(square)


#2.A list containing only even numbers.
even=[x for x in numbers if x%2==0 ]
print(even)

#3..A list containing "Even" or "Odd" for each number.
even_or_odd=['even number'if x%2==0 else "odd number" for x in numbers]
print(even_or_odd)


"""
Q9. List Comprehension with Function

Create a function:

def square(x):
    return x * x

Use list comprehension to call the function for every item in:

numbers = [1, 2, 3, 4, 5]

"""
def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]

box=[square(x) for x in numbers]

print(box)


'''
q10.Select Short Names

Given:

names = ["Karan", "Raj", "Amit", "Alexander", "Sam"]

Using list comprehension, create a new list containing names with 4 or fewer characters.
'''

names = ["Karan", "Raj", "Amit", "Alexander", "Sam"]

new_names=[x for x in names if len(x)<=4]
print(new_names)


"""
Q11. Convert Words to Uppercase

Given:

words = ["python", "java", "sql", "excel"]

Using list comprehension, create a new list where every word is converted to uppercase.

"""

words = ["python", "java", "sql", "excel"]
uppercase=[x.upper() for x in words]
print(uppercase)


"""
Q12. Get First Character

Given:

names = ["Karan", "Rahul", "Amit", "Ravi"]

Create a new list containing the first character of every name.
"""

names = ["Karan", "Rahul", "Amit", "Ravi"]

shortnames=[x[0] for x in names]
print(shortnames)


"""
Q13. Find Words Starting with "A"

Given:

words = ["Apple", "Banana", "Avocado", "Mango", "Apricot"]

Using list comprehension, create a list containing only words that start with "A".
"""

words = ["Apple", "Banana", "Avocado", "Mango", "Apricot"]

A=[x for x in words if x[0]=="A"]
print(A)


"""
q14.Convert Words to Their Length

Given:

words = ["Python", "Java", "SQL", "Programming"]

Using list comprehension and len(), create a list containing the length of each word.

"""

words = ["Python", "Java", "SQL", "Programming"]

length=[len(x) for x in words]
print(length)