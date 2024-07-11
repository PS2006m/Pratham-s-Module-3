'''
Write a Python program to print all unique values in a dictionary.
'''
a={'a':1,'b':2,'c':1,'d':3,'e':4,'f':0,'g':2}
b=[]
for i in a:
    count=0
    for j in a:
        if a.get(i)==a.get(j):
            count+=1
    if count>1:
        b.append(a.get(i))

for i in a:
    if a.get(i) not in b:
        print(a.get(i))
