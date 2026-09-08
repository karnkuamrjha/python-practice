empolyee={
    "empolyee id":input("enter the empolyee id:"),
    "empolyee name":input("enter the empolyee name:"),
    "department name":input("enter the departnment name:"),
    "salary":input("enter the salary:")
}

#write files
file=open('empolyee.txt','a')

file.write(str(empolyee)+"\n")

file.close()

#read files

file=open('empolyee.txt','r')

data=file.read()


print(data)

file.close()