"""
q1.How do you create a set? Create:

(a).An empty set
(b).A set with elements
(c).A set with different data types
"""
#a.empet set
a=set()
print(a)

#b.a set with elements
b={1,2,3,4,5,6}
print(b)
print(type(b))

#c.a set with different data types
c={"karn",True,1,2}
print(c)
print(type(c))


"""
q2. 1. Remove duplicates

Given a list:

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

Convert the list into a set and display only the unique numbers.
"""
numbers = [10, 20, 10, 30, 20, 40, 30, 50]

new=set(numbers)
print(new)

"""
q3.Add a student

Create a set:

students = {"Aman", "Rahul", "Priya"}

Add "Karan" to the set and print the updated set.
"""
students = {"Aman", "Rahul", "Priya"}

students.add("karn")
print(students)


"""
q4.Remove a product

Create:

products = {"Laptop", "Mouse", "Keyboard", "Monitor"}

Remove "Mouse" using remove() and print the set.
"""
products = {"Laptop", "Mouse", "Keyboard", "Monitor"}

products.remove("Mouse")
print(products)

"""
q5.Safe removal

Create:

cities = {"Delhi", "Mumbai", "Patna", "Kolkata"}
Try to remove "Chennai"
"""
#uses discard
cities = {"Delhi", "Mumbai", "Patna", "Kolkata"}

cities.discard("chennai")
print(cities)                         #chennai is not present it not give error


"""
q6.Check membership

Create:

employees = {"Aman", "Rahul", "Karan", "Priya"}

Ask the user to enter an employee name and check whether that employee is present in the set
"""
employees = {"Aman", "Rahul", "Karan", "Priya"}

new=input("enter the empolyee name:")

d=(new in employees)
print(d)


"""
q7. Common students

Two classes have these students:

class_a = {"Aman", "Rahul", "Karan", "Priya"}
class_b = {"Karan", "Priya", "Ravi", "Neha"}

Find the students who are present in both classes.
"""
#uses intersection for find common in both class(&)
class_a = {"Aman", "Rahul", "Karan", "Priya"}
class_b = {"Karan", "Priya", "Ravi", "Neha"}

both=class_a & class_b
print(both)


"""
q8. Students only in Class A

Using the same sets:

class_a = {"Aman", "Rahul", "Karan", "Priya"}
class_b = {"Karan", "Priya", "Ravi", "Neha"}

Find students who are in Class A but not Class B.

"""
#uses differences (-)
class_a = {"Aman", "Rahul", "Karan", "Priya"}
class_b = {"Karan", "Priya", "Ravi", "Neha"}

results=class_a-class_b
print(results)

#another techniques
class_a = {"Aman", "Rahul", "Karan", "Priya"}
class_b = {"Karan", "Priya", "Ravi", "Neha"}

new=class_a.difference(class_b)
print(new)

"""
q9. Combine two teams

Two football teams have:

team_a = {"Rahul", "Aman", "Karan"}
team_b = {"Karan", "Ravi", "Neha"}

Create a set containing all unique players from both teams.
"""
team_a = {"Rahul", "Aman", "Karan"}
team_b = {"Karan", "Ravi", "Neha"}

#used uniques
c=team_a | team_b
print(c)

#another technique
d=team_a.union(team_b)
print(d)

"""
q10.Difference update

Given:

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

Use difference_update() so that A contains only the elements that were originally in A and not in B.

"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7}

#difference
diff=A.difference(B)
print("difference of this is:",diff)

#differences update
update=A.difference_update(B)
print("difference update is:",update)   #output:none Because difference_update() changes the original set directly instead of creating and returning a new set.

#difference_updtae
A.difference_update(B)
print(A)                              #this gives difference update output


"""
q11. Symmetric difference update

Given:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

Use symmetric_difference_update() so that A contains elements that are not common between the two sets.

"""

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#symmetric difference
c=A.symmetric_difference(B)
print("the symmetric difference of :",c)


#symmetric difference update
A.symmetric_difference(B)
print(A)


"""
Real-world Question

A college has two clubs:

football_club = {"Aman", "Rahul", "Karan", "Priya", "Neha"}
coding_club = {"Karan", "Priya", "Ravi", "Aman", "Arjun"}

Write a program to find:

(a)Students in both clubs
(b)Students only in the football club
(c)Students only in the coding club
(d)Students in at least one club
(e)Students who are in exactly one club
(f)Check whether "Rahul" is in the coding club
(g)Add "Vikas" to the coding club
(h)Remove "Neha" from the football club

"""
football_club = {"Aman", "Rahul", "Karan", "Priya", "Neha"}
coding_club = {"Karan", "Priya", "Ravi", "Aman", "Arjun"}

#(a)Students in both clubs
#uses union
both=football_club.union(coding_club)
print("student in both clubs is:",both)


#(b)Students only in the football club
#uses differences
onlyfootball=football_club.difference(coding_club)
print("student only in football club is:",onlyfootball)

#(c)Students only in the coding club
#use difference
onlyconding=coding_club.difference(football_club)
print("student only in conding club is:",onlyconding)

#(d)(d)Students in at least one club
#uses union
atleast=football_club.union(coding_club)
print("student in at least one club:",atleast)

#(e)Students who are in exactly one club
#uses symmetric differences
exactly=football_club.symmetric_difference(coding_club)
print("exactly student in one club:",exactly)

#(f)Check whether "Rahul" is in the coding club
#uses membership
check=("Rahul" in coding_club)
print("rahul present in coding club:",check)

#(g)Add "Vikas" to the coding club
coding_club.add("vikas")
print(coding_club)

#(h)Remove "Neha" from the football club
football_club.remove("Neha")
print(football_club)


