'''
Write a Python program to find the repeated items of a tuple.
'''
a=(1,2,3,4,3,2)
b=[]
for i in a:
    if i in b:
        print(i)
    b.append(i)
