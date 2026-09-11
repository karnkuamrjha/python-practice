import os

#create a directory
os.mkdir('students')

#create nested directory
os.makedirs('collage/placements')

#join path

folder = "Students"
file = "marks.txt"

path = os.path.join(folder, file)

print(path)

#file exists or not

#step 1:os.path.exists

if os.path.exists("map.py"):
    print("file is exists")
else:
    print("file is not exists")


#step 2:os.path.isfile

if os.path.isfile("map.py"):
    print("file is exists")
else:
    print("file is not exists")


#step 3:pathlib.path.exists
from pathlib import Path

file=Path('map.py')

if file.exists():
    print("file is exists")
else:
    print("file is not exists")


#step4:pathlib.path.is_file
file=Path('map.py')

if file.is_file():
    print("file is exists")
else:
    print("file is not exists")


#check directory present or not
path="map.py"
gives='students'
music='files'

print(os.path.isdir(path))   #map.py is file not directory it gives false.
print(os.path.isdir(gives)) #Because os.path.isdir(path) checks the actual path stored in path. It does not know that you intend it to be a subdirectory.
print(os.path.isdir(music))


#check subdirectory in files
path=os.path.join("filesanddirectory",'students')

print(os.path.isdir(path))      #students present in filesanddirectory then give:true


g=os.path.join('files',"students")

print(os.path.isdir(g))        #false:becuse files has no subdirectory name is students



#getting absolute path
path='map.py'

absolute=os.path.abspath(path)

print(absolute)      #/home/karn/Desktop/python/map.py :this is absolute path of map.py

