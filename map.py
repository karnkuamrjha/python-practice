"""
q1.Use map() with a normal function to double every number in this list:
numbers = [2, 4, 6, 8, 10]
"""
numbers = [2, 4, 6, 8, 10]

result=map(lambda x:x*2 ,numbers)

print(list(result))


"""
q2.Use map() with a normal function to find the cube of every number:
numbers = [1, 2, 3, 4, 5]

"""
numbers = [1, 2, 3, 4, 5]

result=map(lambda x:x*x*x,numbers)

print(list(result))

"""
q3.Use map() to convert these strings into integers:
numbers = ["10", "20", "30", "40"]
"""
numbers = ["10", "20", "30", "40"]

result=map(lambda x:int(x),numbers)

print(list(result))
print(type(result))

"""
4.Use map() with two lists to add corresponding elements:
a = [10, 20, 30]
b = [1, 2, 3]
"""
a = [10, 20, 30]
b = [1, 2, 3]

def corrsponding(a,b):
    return a+b

result=map(corrsponding,a,b)

print(list(result))



"""
q5.You have a dictionary of student marks. Use map() with a normal function to add 5 marks to every student:
marks = {
    "Rahul": 50,
    "Aman": 60,
    "Karan": 70
}
"""
marks = {
    "Rahul": 50,
    "Aman": 60,
    "Karan": 70
}


def add(x):
    return x+5


result=map(add,marks.values())
print(list(result))



"""
q6.Shopping Prices

You have a list of product prices:

prices = [100, 250, 50, 500, 120, 300]

Use map() with a lambda function to add 18% GST to every price.
"""
prices = [100, 250, 50, 500, 120, 300]


after=map(lambda x:x-(x*18)/100,prices)

print(list(after))



