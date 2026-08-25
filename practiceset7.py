#q1.Define a recursive function to calculate the nth Fibonacci number using memoization. Test the function with different inputs.
def fabroic(n,memo={}):
    if n<=1:
        return n

    if n in memo:
        return memo[n]

    memo[n]=fabroic(n-1,memo)+fabroic(n-2,memo)

    return memo[n]

print(fabroic(5))
print(fabroic(10))
print(fabroic(15))


#q2.Define a function that takes two arguments, a and b, where b is a dictionary with a default value of an empty dictionary. The function should add a new key-value pair to the dictionary and return it. Test the function with different inputs.
def add_item(a, b={}):
    b[a] = "value"
    return b

print(add_item("name"))
print(add_item("age", {"name": "Karn"}))


#q3.Define a function that takes a variable number of keyword arguments and returns a dictionary containing only those key-value pairs where the value is an integer. Test the function with different inputs
def m(**kwargs):
    return{k:v for k,v in kwargs.items() if isinstance(v,int)}

print(m(k=10,v=20))
print(m(k=25,v="karn"))



#q4.Define a function that takes another function as a callback and a list of integers. The function should apply the callback to each integer in the list and return a new list with the results. Test with different callback functions.
numbers=[1,2,3,4,5]

def square(x):
    return x*x

Result=map(square,numbers)

print(list(Result))




#q5.Define a function that returns another function. The returned function should take an integer and return its square. Test the returned function with different inputs

def functions(return_function):
    return return_function

def return_function(x):
    return x*x

print(return_function(10))
print(return_function(20))


#q6.Define a higher-order function that takes two functions, a filter function and a map function, along with a list of integers. The higher-order function should first filter the integers using the filter function and then apply the map function to the filtered integers. Test with different filter and map functions.

numbers = [1, 2, 3, 4, 5]

def even(x):
    return x % 2 == 0

def square(x):
    return x * x

def process(filter_function, map_function, numbers):
    filtered = filter(filter_function, numbers)
    result = map(map_function, filtered)

    return list(result)

print(process(even, square, numbers))


#q7.Define a function that composes two functions, f and g, such that the result is f(g(x)). Test with different functions f and g

def f(x):
    return x+1

def g(x):
    return x*2

def r(x):
    return f(g(x))


print(r(3))
print(r(5))


#q8.Use the functools.partial function to create a new function that multiplies its input by 2. Test the new function with different inputs.

from functools import partial

multiply=lambda x:x*2 

print(multiply(4))


#q9.Define a curried function that takes three arguments, one at a time, and returns their product. Test the function by providing arguments one at a time
def curried(x):
    def inner1(y):
        def outer1(z):
            return x*y*z
        return outer1
    return inner1


print(curried(2)(3)(4))
print(curried(5)(6)(7))


#q10.define a function that takes a list of mixed data types (integers, strings, and floats) and returns three lists: one containing all the integers, one containing all the strings, and one containing all the floats. Test with different inputs."


