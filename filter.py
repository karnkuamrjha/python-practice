"""
1.Use filter() with a normal function to find all even numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def n(x):
    return x%2==0

result=filter(n,numbers)

print(list(result))


"""
2.Use filter() to find numbers greater than 50:
numbers = [20, 55, 40, 75, 90, 30]
"""
numbers = [20, 55, 40, 75, 90, 30]

def find(x):
    return x>50

print(list(filter(find,numbers)))


"""
3.Use filter() with a lambda function to find numbers that are positive:
numbers = [-5, 10, -2, 8, 0, 15]

"""
numbers = [-5, 10, -2, 8, 0, 15]

result=filter(lambda x:x>0,numbers)

print(list(result))


"""
4.Use filter() to find students who passed (marks ≥ 50):
marks = [35, 60, 45, 80, 25, 70]
"""
marks = [35, 60, 45, 80, 25, 70]

student=filter(lambda x:x>=50,marks)

print(list(student))

"""

5.Use filter() with a lambda function and multiple conditions to find numbers that are greater than 10 AND even:
numbers = [4, 12, 15, 18, 21, 24, 7]

"""
numbers = [4, 12, 15, 18, 21, 24, 7]

result=filter(lambda x:x>10 and x%2==0,numbers)

print(list(result))


"""
6.Given this dictionary, use filter() to find students who scored 60 or more:
marks = {
    "Rahul": 55,
    "Aman": 75,
    "Karan": 60,
    "Ravi": 45
}
"""
marks = {
    "Rahul": 55,
    "Aman": 75,
    "Karan": 60,
    "Ravi": 45
}

def score(x):
    return x[1]>60

result=filter(score,marks.items())

print(list(result))


"""
7.Employee Salaries

You have employee salaries:

salary = [25000, 40000, 18000, 55000, 30000]

Use filter() to find employees whose salary is greater than ₹30,000.
"""

salary = [25000, 40000, 18000, 55000, 30000]

result=filter(lambda x:x>30000,salary)

print(list(result))