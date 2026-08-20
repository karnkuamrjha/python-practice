#1.Create a list of the first 20 positive integers. Print the list.
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(a)


#q2.Print the first, middle, and last elements of the list created in Assignment 1
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#first
b=a[0]
print(b)

#last
c=a[-1]
print(c)

#middle
d=a[9]
print(d)


#q3. Print the first five elements, the last five elements, and the elements from index 5 to 15 of the list created in Assignment 1.
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


#Print the first five elements
e=a[0:5]
print(e)

#print last 5 elements
f=a[-5:]
print(f)

#print 5 to 15 index
g=a[5:15]
print(g)


#q4.Create a new list containing the squares of the first 10 positive integers using a list comprehension. Print the new list.
a=[1,2,3,4,5,6,7,8,9,10]

b=[x*x for x in a]
print(b)


#q5.Create a new list containing only the even numbers from the list created in Assignment 1 using a list comprehension. Print the new list
a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

even=[x for x in a if x%2==0]

print(even)


#q6.Create a list of random numbers and sort it in ascending and descending order. Remove the duplicates from the list and print the modified list
a=[1,2,3,4,5,6,7,8,9,10,14,4,13,14,20,16,17,17,19,20]

#assending order
a.sort(reverse=False)
print(a)


#descending order
a.sort(reverse=True)
print(a)

#remove duplicate
print(list(set(a)))


#Q7.Create a nested list representing a 3x3 matrix and print the matrix. Access and print the element at the second row and third column.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
matrix2=matrix[1][2]
print(matrix2)


#q8.Create a list of dictionaries where each dictionary represents a student with keys 'name' and 'score'. Sort the list of dictionaries by the 'score' in descending order and print the sorted list.
marks=[
    {"name":"karn","marks":96},
    {"name":"rahul","marks":23},
    {"name":"amit","marks":56}
]

marks.sort(key=lambda x:x['marks'])
print(marks)


#q9.Write a function that takes a 3x3 matrix (nested list) as input and returns its transpose. Print the original and transposed matrices.

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

orginal_matrix=print(matrix)

transpose_matrix=[[row[i] for row in matrix]for i in range(3)]
print(transpose_matrix)


#q10.Write a function that takes a nested list and flattens it into a single list. Print the original and flattened lists.
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

flat_list=[item for row in matrix for item in row]
print(flat_list)

#q11.Create a list of the first 10 positive integers. Remove the elements at indices 2, 4, and 6, and insert the element '99' at index 5. Print the modified
n=[1,2,3,4,5,6,7,8,9,10]

#remove 2,4,6 index
n.pop(2)
n.pop(4)
n.pop(6)
print(n)


#inser 99 at index 5

n.insert(5,99)
print(n)


#q12.create two lists of the same length. Use the `zip` function to combine these lists into a list of tuples and print the result.
a=[1,2,3,4,5,6,7,8,9,10]
b=[11,12,13,14,15,16,17,18,19,20]

c=list(zip(a,b))

print(c)


#q13.Write a function that takes a list and returns a new list with the elements in reverse order. Print the original and reversed lists.

def reverse(x):
    return x[::-1]

numbers=[1,2,3,4,5,6,7,8,9,10]

result=reverse(numbers)

print(result)


#q14.Write a function that rotates a list by n positions. Print the original and rotated lists.

def rotate(x):
    return x[2:]+x[:2]

number=[1,2,3,4,5]

result=rotate(number)
print(result)


#q15.Write a function that takes two lists and returns a new list containing only the elements that are present in both lists. Print the intersected list

a = [1,2,3,4,5,6,7,8,9,10]

b = [11,12,3,6,8,15,16,7,10,20]

common = [x for x in a if x in b]

print(common)




