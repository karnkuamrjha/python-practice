#q1.Create a dictionary with the first 10 positive integers as keys and their squares as values. Print the dictionary.

num=[1,2,3,4,5,6,7,8,9,10]

square={num:num*num for num in num}

print(square)

#easy technique
n={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25,
    6:36,
    7:49,
    8:64,
    9:81,
    10:100
}

print(n)

#q2.Print the value of the key 5 and the keys of the dictionary created in Assignment 1
n={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25,
    6:36,
    7:49,
    8:64,
    9:81,
    10:100
}

#get techniques used
print(n.get(5))

#using key
print(n[5])



#q3.Add a new key-value pair (11, 121) to the dictionary created in Assignment 1 and then remove the key-value pair with key 1. Print the modified dictionary.
n={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25,
    6:36,
    7:49,
    8:64,
    9:81,
    10:100
}

#adding(11:121)

n[11]=121
print(n)

#remove 4 using del

del n[4]
print(n)

#remove using pop
n.pop(3)
print(n)


#q4.Iterate over the dictionary created in Assignment 1 and print each key-value pair
n={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25,
    6:36,
    7:49,
    8:64,
    9:81,
    10:100
}

for key,value in n.items():
    print(key,":",value)



#q5.Create two dictionaries: one with keys as the first 5 positive integers and values as their squares, and another with keys as the next 5 positive integers and values as their squares. Merge these dictionaries into a single dictionary and print it.
first={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}

second={
    6:36,
    7:49,
    8:64,
    9:81,
    10:100
}

#merge the dictonary
third=first|second
print(third)


#q6.Create a nested dictionary representing a student with keys 'name', 'age', 'grades', where 'grades' is another dictionary with keys 'math', 'science', and 'english'. Print the nested dictionary
student_info={
    "student":
    {
        "name":"sumit",
        "age":22,
        "grades":90
    },
    "grades":
    {
        "math":84,
        "science":83,
        "english":96

    }

}

print(student_info)



#q7.Create a dictionary where the keys are the first 5 positive integers and the values are lists containing the first 5 multiples of the key. Print the dictionary.
multiple={
    1:[1,2,3,4,5],
    2:[2,4,6,8,10],
    3:[3,6,9,12,15],
    4:[4,8,12,16,20],
    5:[5,10,15,20,25]
}

print(multiple)

#q8.Create a dictionary where the keys are the first 5 positive integers and the values are tuples containing the key and its square. Print the dictionary
multiple={
    1:(1,2,3,4,5),
    2:(2,4,6,8,10),
    3:(3,6,9,12,15),
    4:(4,8,12,16,20),
    5:(5,10,15,20,25)
}

print(multiple)


#q9.Create a dictionary with the first 5 positive integers as keys and their squares as values. Convert the dictionary to a list of tuples and print it
num={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}

#one by one
for key,value in num.items():
    print([(key,value)])

#all
result=list(num.items())
print(result)


#q10.Create a dictionary with the first 10 positive integers as keys and their squares as values. Create a new dictionary containing only the key-value pairs where the key is even. Print the new dictionary
n={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25,
    6:36,
    7:49,
    8:64,
    9:81,
    10:100
}


results={key:value for key,value in n.items() if key%2==0}
print(results)

 
#another technique

for key,value in n.items():
    if key%2==0:
        print(key,value)


#q11.Create a dictionary with the first 5 positive integers as keys and their squares as values. Create a new dictionary with keys and values swapped. Print the new dictionary

n={
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}

new_dictonary={value:key for key,value in n.items()}
print(new_dictonary)


#q12.Create a default dictionary where each key has a default value of an empty list. Add some elements to the lists and print the dictionary.

keys=[1,2,3]

t=dict.fromkeys(keys,"empty list")

print(t)

#new values also then
empty=[2,4,6]

t=dict.fromkeys(keys,empty)
print(t)


#q13.Create a dictionary representing a book with keys 'title', 'author', 'year', and 'genre'. Convert the dictionary to a JSON string and print it.

import json

books={
    "tittle of the book is":"the boys",
    "author":"karn",
    "year of publish book":2026,
    "genre":"boys"
}

#convert dictonary to json


new=json.dumps(books)
print(new)



#q14.Write a function that takes a string and returns a dictionary with the count of each character in the string. Print the dictionary.
strings=input("enter the name:")
def count_characters(text):
    return{char:text.count(char)for char in text}
print(count_characters(strings))



