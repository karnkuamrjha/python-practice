#q1. Create a text file and write your name, age, and city into it. Then read and display the file.

file=open('file.txt','r')

dat=file.read()

print(dat)

file.close()


#q2.Create a file containing 5 student names and read the file line by line.

file=open('file.txt','r')

data=file.read()

for fil in data:
   print(fil)


#q3.Write a program to count the number of lines in a text file.

file=open('file.txt','r')

data=file.read()

print(data.count("name"))


#q4.Create a file and write 10 numbers into it. Then read the file and calculate their sum.(uses sum)

file=open('file.txt','r')

data=file.read().split()

numbers=[int(x) for x in data]

print(sum(numbers))

file.close()

#q5.Create a file and write 10 numbers into it. Then read the file and find the largest number.(use max)

file=open('file.txt','r')

data=file.read().split()

numbers=[int(x) for x in data]

print(max(numbers))

file.close()

#q6.Create a file and write 10 numbers into it. Then read the file and find the smallest number.(use min)

file=open('file.txt','r')

data=file.read().split()

num=[int(x) for x in data]

print(min(num))


#q7.Create a file and write 10 numbers into it. Then read the file and calculate their average.

file=open('file.txt','r')

data=file.read().split()

num=[int(x) for x in data]
#sum of number
a=sum(num)
#count of number
b=len(num)

#find average
avg=a/b
print(avg)


#q8.Create a file and write 10 numbers into it. Then read the file and calculate the difference between the largest and smallest number.
file=open('file.txt','r')

data=file.read().split()

num=[int(x) for x in data]

#find heighest number
high=max(num)

#find lowest number
low=min(num)

#differences of two number
difference=high-low
print(difference)


#q9.Create a file and write 10 numbers into it. Then read the file and count how many numbers are even and how many are odd.
file=open('file.txt','r')

data=file.read().split()

num=[int(x) for x in data]
even=0
odd=0

for new in num:
   if new%2==0:
    print(new,"---","even number")
    even=even+1
   else:
    print(new,"---","odd number")
    odd=odd+1

print("the total number of even is:",even)
print("the total number of odd is",odd)




