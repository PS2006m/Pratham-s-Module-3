'''
Write a Python program to check whether an element exists within a
tuple.
'''
a=(1,2,3,4,5,6)
number=4
for i in a:
    if i==number:
        print("Exists")
        break
else:
    print("Doesn't Exists")
