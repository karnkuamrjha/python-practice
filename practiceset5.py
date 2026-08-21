#q1.Create a new set containing the squares of the first 10 positive integers using a set comprehension. Print the new set.

a = {1,2,3,4,5,6,7,8,9,10}

b = {x*x for x in a}

print(b)                 #output:{64, 1, 4, 36, 100, 9, 16, 49, 81, 25} because set is unorder 



#q2.Create a new set containing only the even numbers from the set created in Assignment 1 using a set comprehension. Print the new set.

a = {1,2,3,4,5,6,7,8,9,10}

new={x for x in a if x%2==0}
print(new)

#q3.Create two sets: one with the first 5 positive integers and another with the first 3 positive integers. Check if the second set is a subset of the first set and if the first set is a superset of the second set. Print the results."
first={1,2,3,4,5}
second={1,2,6}

print(second.issubset(first))        #subset:subset check if all element present in another set

print(first.issuperset(second))      #superset check if its contanins all element of the sets


#q4.Create a frozenset with the first 5 positive integers. Print the frozenset
num=frozenset([1,2,3,4,5])
print(num)

#set to frozen set
n={1,2,3,4,5}

new=frozenset(n)
print(new)


#q5.Create a set with the first 5 positive integers. Convert it to a list, append the number 6, and convert it back to a set. Print the resulting set
n={1,2,3,4,5}

#convert into list
a=list(n)
print(a)

#append 6
a.append(6)
print(a)

#convert list into set
resulting_set=set(a)
print(resulting_set)


#q6.Create a dictionary with set keys and integer values. Print the dictionary
#normal set key not used used frozen set key

data={
    frozenset({1}):3,
    frozenset({2}):4,
    frozenset({3}):6
}
print(data)


#q7.Create a set and iterate over the elements, printing each element
a={1,2,3,4,5}

for x in a:
    print(x)


#q8.Create a set and remove elements from it until it is empty. Print the set after each removal
a={1,2,3,4,5}


while a:
    a.pop()
    print(a)


#q9.Create two sets and update the first set with the symmetric difference of the two sets. Print the modified first set
a={1,2,3,4,5}
b={1,2,7}

first_set=a.symmetric_difference(b)
print(first_set)


#q10.Create a set and test if certain elements are present in the set. Print the results.
a={'karn',"kunal","ravi","sunny","adarash"}

name=input("enter the name of the person:")

if (name in a):
    print(f'{name} is presnet in the a set')
else:
    print(f'{name} is not present in the a set ')


#q11.Create a set containing tuples, where each tuple contains two elements. Print the set.
a={(1,2),(2,3),(4,5)}
print(a)