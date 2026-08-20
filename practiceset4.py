#q1.Create a nested tuple representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
tuple=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

print(tuple)
tuple1=tuple[1][2]
print(tuple1)


#q2.Create a tuple with duplicate elements and count the occurrences of an element. Find the index of the first occurrence of an element in the tuple.
tuple=(1,2,3,1,4,2,5,6,2,8)

tuple1=tuple.count(2)
print(tuple1)

tuple3=tuple.index(2)
print(tuple3)


#q3.Create a tuple with 5 elements and unpack it into 5 variables. Print the variables.
a=(1,2,3,4,5)

b,c,d,e,f=a
print(b)
print(c)
print(d)
print(e)
print(f)


#q4.reate a tuple containing 3 tuples, each with 3 elements. Print the tuple of tuples.

playerinformation = (
    ("rahul bheke", 36, "mohan bagan"),
    ("pramveer singh", 18, "northeast united"),
    ("karn kumar jha", 22, "banaras bhagpat")
)

print(playerinformation)

#q5.Create a tuple with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a tuple. Print the resulting tuple.
numbers = (1, 2, 3, 4, 5)

print(numbers)

# Convert tuple into list
numbers_list = list(numbers)

print(numbers_list)

# Append 6
numbers_list.append(6)

print(numbers_list)

# Convert list into tuple
resulting_tuple = tuple(numbers_list)

print(resulting_tuple)


#q6.Create a tuple with the characters of a string. Join the tuple elements into a single string. Print the string

a="hello"

#convert string to tuple
b=tuple(a)
print(b)

#join tuples
j="".join(b)
print(j)

#q7. Create a dictionary with tuple keys and integer values. Print the dictionary.
playerinformation={
    ("rahul bheke"):36,
    ("pramveer singh"):19,
    ("karn kumar jha"):22
}

print(playerinformation)

#q8.Create a nested tuple and iterate over the elements, printing each element.
a=(
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

for b in a:
    for c in b:
        print(c)


#q9.Create a tuple with duplicate elements. Convert it to a set to remove duplicates and print the resulting set.
a=(1,2,3,1,4,5,1,8)

#convert tuple into set
b=set(a)
print(b)
print(type(b))

#remove duplicates (set automatically remove duplicated value )


#q10.Write functions that take a tuple and return the minimum, maximum, and sum of the elements. Print the results for a sample tuple

def find_maximum(x):
    return max(x)

def find_minimum(x):
    return min(x)

def find_sum(x):
    return sum(x)

x=(1,2,3,4,5,6,7)

minimum=find_maximum(x)
maximum=find_maximum(x)
sum_number=find_sum(x)

print("minimum of:",minimum)
print("maximum of:",maximum)
print("sum of:",sum_number)

