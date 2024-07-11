'''
Write a Python program to remove an empty tuple(s) from a list of tuples.
'''
a=[(1,2),(),(3,4,5),()]
for i in a:
    if len(i)==0:
        a.remove(i)
print(a)
