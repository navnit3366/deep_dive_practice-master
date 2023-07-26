import sys
print(f"Lecture 1: Variables and Reference counter")
# memory management Deep Dive Python 3
10  # 10 is an object with value 10
a = 10  # 10 is an object , a refers to the memory location of 10
if id(a) == id(10):
    print("same")

b = [1, 2, 3] # 1st
c = b  # 2nd
d = c  # 3rd
id(d)  # after getting the address id function releases its pointer as a result it doesn't get counted
# get ref count counts the reference of an object
print(sys.getrefcount(d))  # This function refers the object 10 by using 'a' pointer too # 4th

print(f"Lecture 2: Garbage Collection\n\n")




